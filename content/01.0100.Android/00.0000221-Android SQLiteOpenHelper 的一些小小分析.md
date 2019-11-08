# Android SQLiteOpenHelper 的一些小小分析
- Android,sqlite,数据库,

就目前而言，SQLiteOpenHelper 的 onCreate() 方法是在第一次调用getWritableDatabase() 方法的时候被调用。


写一个子类，继承于SQLiteOpenHelper，使用的时候调用他的构造方法。构造方法有两个。

    public SQLiteOpenHelper(Context context, String name, CursorFactory factory, int version) {
        this(context, name, factory, version, new DefaultDatabaseErrorHandler());
    }

    public SQLiteOpenHelper(Context context, String name, CursorFactory factory, int version,
            DatabaseErrorHandler errorHandler) {
        if (version < 1) throw new IllegalArgumentException("Version must be >= 1, was " + version);
        if (errorHandler == null) {
            throw new IllegalArgumentException("DatabaseErrorHandler param value can't be null.");
        }

        mContext = context;
        mName = name;
        mFactory = factory;
        mNewVersion = version;
        mErrorHandler = errorHandler;
    }

一般使用第一个。

下面是getWritableDatabase() 方法的源码

    public synchronized SQLiteDatabase getWritableDatabase() {
        if (mDatabase != null) {
            if (!mDatabase.isOpen()) {
                // darn! the user closed the database by calling mDatabase.close()
                mDatabase = null;
            } else if (!mDatabase.isReadOnly()) {
                return mDatabase;  // The database is already open for business
            }
        }

        if (mIsInitializing) {
            throw new IllegalStateException("getWritableDatabase called recursively");
        }

        // If we have a read-only database open, someone could be using it
        // (though they shouldn't), which would cause a lock to be held on
        // the file, and our attempts to open the database read-write would
        // fail waiting for the file lock.  To prevent that, we acquire the
        // lock on the read-only database, which shuts out other users.

        boolean success = false;
        SQLiteDatabase db = null;
        if (mDatabase != null) mDatabase.lock();
        try {
            mIsInitializing = true;
            if (mName == null) {
                db = SQLiteDatabase.create(null);
            } else {
                db = mContext.openOrCreateDatabase(mName, 0, mFactory, mErrorHandler);
            }

            int version = db.getVersion();
            if (version != mNewVersion) {
                db.beginTransaction();
                try {
                    if (version == 0) {
                        onCreate(db);
                    } else {
                        if (version > mNewVersion) {
                            onDowngrade(db, version, mNewVersion);
                        } else {
                            onUpgrade(db, version, mNewVersion);
                        }
                    }
                    db.setVersion(mNewVersion);
                    db.setTransactionSuccessful();
                } finally {
                    db.endTransaction();
                }
            }

            onOpen(db);
            success = true;
            return db;
        } finally {
            mIsInitializing = false;
            if (success) {
                if (mDatabase != null) {
                    try { mDatabase.close(); } catch (Exception e) { }
                    mDatabase.unlock();
                }
                mDatabase = db;
            } else {
                if (mDatabase != null) mDatabase.unlock();
                if (db != null) db.close();
            }
        }
    }

下面是getReadableDatabase()方法的源码

     public synchronized SQLiteDatabase getReadableDatabase() {
        if (mDatabase != null) {
            if (!mDatabase.isOpen()) {
                // darn! the user closed the database by calling mDatabase.close()
                mDatabase = null;
            } else {
                return mDatabase;  // The database is already open for business
            }
        }

        if (mIsInitializing) {
            throw new IllegalStateException("getReadableDatabase called recursively");
        }

        try {
            return getWritableDatabase();
        } catch (SQLiteException e) {
            if (mName == null) throw e;  // Can't open a temp database read-only!
            Log.e(TAG, "Couldn't open " + mName + " for writing (will try read-only):", e);
        }

        SQLiteDatabase db = null;
        try {
            mIsInitializing = true;
            String path = mContext.getDatabasePath(mName).getPath();
            db = SQLiteDatabase.openDatabase(path, mFactory, SQLiteDatabase.OPEN_READONLY,
                    mErrorHandler);
            if (db.getVersion() != mNewVersion) {
                throw new SQLiteException("Can't upgrade read-only database from version " +
                        db.getVersion() + " to " + mNewVersion + ": " + path);
            }

            onOpen(db);
            Log.w(TAG, "Opened " + mName + " in read-only mode");
            mDatabase = db;
            return mDatabase;
        } finally {
            mIsInitializing = false;
            if (db != null && db != mDatabase) db.close();
        }
    }

从上面的源码可以看出

1 。 这个类是对Context.openOrCreateDatabase() 的封装（Google官网本来就是那么说的，有点废话了）。

2 。 在大部分情况下，getReadableDatabase() 和 getWritableDatabase() 效果是一样的。返回的是同一个mDatabase对象。特殊情况是指内存空间不足，不能继续往数据库里写东西类似的情况。如果调用getWritableDatabase()方法，会抛出一个异常。如果调用getReadableDatabase()的话，会尝试返回一个只读的Database对象。当然还是可能抛异常。

3 。 onCreate()方法在第一次调用getWritableDatabase()方法的时候被调用。当然如果第一次调用getReadableDatabase()方法也会调用onCreate()方法。