# SQLiteDatabase query() 和 rawQuery() 的区别
- 2014-11-24 05:13:39
- Android
- android,sqlitedatabase,query,rawquery,

<!--markdown-->刚才在 CSDN 上看见有人问说在 Android SQLiteDatabase 里，query() 和 rawQuery() 方法的区别。对于这种问题，其实最好的办法就是参看源码，结果确实这样，通过源代码，很快就找到了问题的答案了。

咱们先看看 query() 是怎么实现的。

    public Cursor query(String table, String[] columns, String selection, 
        String[] selectionArgs, String groupBy, String having, String orderBy) {
            return query(false, table, columns, selection, selectionArgs, groupBy,
                    having, orderBy, null /* limit */);
    }

    public Cursor query(boolean distinct, String table, String[] columns,
            String selection, String[] selectionArgs, String groupBy,
            String having, String orderBy, String limit) {
        return queryWithFactory(null, distinct, table, columns, selection, selectionArgs,
                groupBy, having, orderBy, limit, null);
    }

这几个方法都没有具体实现。

    public Cursor queryWithFactory(CursorFactory cursorFactory,
            boolean distinct, String table, String[] columns,
            String selection, String[] selectionArgs, String groupBy,
            String having, String orderBy, String limit, CancellationSignal cancellationSignal) {
        acquireReference();
        try {
            String sql = SQLiteQueryBuilder.buildQueryString(
                    distinct, table, columns, selection, groupBy, having, orderBy, limit);
    
            return rawQueryWithFactory(cursorFactory, sql, selectionArgs,
                    findEditTable(table), cancellationSignal);
        } finally {
            releaseReference();
        }
    }

最终调用的就是这个方法。

    public Cursor rawQueryWithFactory(
            CursorFactory cursorFactory, String sql, String[] selectionArgs,
            String editTable, CancellationSignal cancellationSignal) {
        acquireReference();
        try {
            SQLiteCursorDriver driver = new SQLiteDirectCursorDriver(this, sql, editTable,
                    cancellationSignal);
            return driver.query(cursorFactory != null ? cursorFactory : mCursorFactory,
                    selectionArgs);
        } finally {
            releaseReference();
        }
    }

咱们再看看 rawQuery() 是怎么实现的。

    public Cursor rawQuery(String sql, String[] selectionArgs) {
        return rawQueryWithFactory(null, sql, selectionArgs, null, null);
    }

还是这个方法。

    public Cursor rawQueryWithFactory(
            CursorFactory cursorFactory, String sql, String[] selectionArgs,
            String editTable, CancellationSignal cancellationSignal) {
        acquireReference();
        try {
            SQLiteCursorDriver driver = new SQLiteDirectCursorDriver(this, sql, editTable,
                    cancellationSignal);
            return driver.query(cursorFactory != null ? cursorFactory : mCursorFactory,
                    selectionArgs);
        } finally {
            releaseReference();
        }
    }

可以看到，最后，调用的都是**rawQueryWithFactory**(CursorFactory,String,String[],String,CancellationSignal) 这个方法，你完全可以代码都不用看懂都可以找到答案。

回到问题上，这两个方法的区别在于，最终的 SQL 语句，谁来拼？query() 做的一件事就是帮你拼写 SQL 语句，而调用 rawQuery() 是你自己拼写好语句。我认为的差别仅次而已。