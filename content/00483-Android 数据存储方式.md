# Android 数据存储方式
- 2016-03-22 03:59:05
- 
- 

<!--markdown--># Android 数据存储方式

在 Android 开发过程中，数据的存储是必不可少的，而存储数据的方式也有很多种，各种存储方式都有它们的利弊，没有哪个是最好的，只有最合适的而已。下面列举了五种存储方式：

* 使用SharedPreferences存储数据
* 文件存储数据
* SQLite数据库存储数据
* 使用ContentProvider存储数据
* 网络存储数据

## SharedPreferences

SharedPreferences 是 Android 平台上一个轻量级的存储类，当你需要存储一些少量的简单的数据的时候，SharedPreferences 是一个不错的选择。

涉及到的几个步骤
1. 获取 SharedPreferences 对象 


    SharedPreferences p = context.getSharedPreferences(name, mode);

name: 文件的名字

mode : Use 0 or MODE_PRIVATE for the default operation, MODE_WORLD_READABLE and MODE_WORLD_WRITEABLE to control permissions. The bit MODE_MULTI_PROCESS can also be used if multiple processes are mutating the same SharedPreferences file. MODE_MULTI_PROCESS is always on in apps targeting Gingerbread (Android 2.3) and below, and off by default in later versions.

2. 通过 edit() 方法获取 Editor 对象。


    Editor editor = p.edit();

3. 通过 Editor 对象存储数据。


    editor.putBoolean(key, value);
    editor.putFloat(key, value);
    editor.putInt(key, value);
    editor.putLong(key, value);
    editor.putString(key, value);
    editor.putStringSet(key, values);

4. 通过 commit() 方法提交数据。


    editor.commit();

数据会被存储到 /data/data/<package_name\>/shared_prefs 目录下。也就是，其实 SharedPreferences 是数据以 XML 的格式存储到文件里。

优点就是轻量级，使用方便。
缺点可能会比较多一些。
1. 只能存储简单的数据，就如它的 API 提供的，boolean,float,int,long,String 和 Set<String>
2. 以 XML 格式存储数据意味着需要 XML 的解析。


## 文件存储数据

不管是 SharedPreferences 还是数据库，甚至是网络的方式，其根本都是文件，只是文件的地址和文件的格式不一样而已。Android 也提供了文件的存储（Java SE 本来就提供了）。

文件的存储有很多种，主要的区别在于文件存放的位置。

    context.openFileOutput(name, mode);

这种方式不需要任何权限，因为文件是存储在 /data/data/<package_name\>/files/ 目录下的。是属于内部的存储（internal storage）。

Android 还提供一个缓存目录，你也可以往里面写一些文件，但要注意是"缓存"，也就是文件搁这里的话，系统会在它不高兴的时候把里面的文件删掉，而且你不能主动删。

    context.getCacheDir();

> Note: you should not rely on the system deleting these files for you; you should always have a reasonable maximum, such as 1 MB, for the amount of space you consume with cache files, and prune those files when exceeding that space.

这些目录下的文件是不需要申请权限的，但是一般来说，你是不能把比较大的文件搁里头的。比如你下载了个 mp3 文件，这个 mp3 文件应该被搁到 sdcard 上。什么？没有 sdcard ？谁说的，肯定有。[Android 获取 sdcard 和 内部存储的空间大小](http://blog.binkery.com/android/get_sdcard_and_innernal_storage_size.html) , Android 虚拟出了一个 sdcard 。

对 sdcard 上的文件读写就需要 File 这个类了，然后你就可以根据的需求，获取各种各样的 IO 流了。

权限的申请是必要的。

    <uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/> 

相比 /data/data/<package_name\>/files/ ， sdcard 文件的访问权限就很松了，大家都可以访问。做不做加密就看你的需求了。

[Android Internal Storage And External Storage](http://blog.binkery.com/android/storage_internal_and_external.html) 这篇文章介绍得更加清楚一些，关于Android 的存储空间。

## SQLite数据库存储数据

SQLite 是 Android 数据存储的重头戏了。相比于文件存储，SQLite 是重量级的，但是相比其他的数据库，SQLite 是轻量级的，也是移动设备数据库存储的最佳选择。

SQLite 的使用这里就不详细写了，因为确实挺多的。咱这里就只说说它的优缺点了。

其实也没啥优缺点，是特点。
1. 首先它是一个完整的数据库，所以增删改查完全没问题，SQL语句没问题
2. 它有数据类型，但是是弱数据类型，所以很灵活。
3. 支持事务


## ContentProvider 

ContentProvider 其实本质还是数据库，但是它又不同于数据库。主要区别有
1. ContentProvider 方便数据在多个应用程序之间共享。数据库一般都是应用内部访问的，不能多应用共享，即使你可以把数据库文件放在 sdcard 上供其他应用读写，但是这一不安全，二别人也不清楚你的数据库表结构。
2. ContentProvider 提供了数据存储的统一接口。其他应用程序可以通过 Uri 来访问。
3. Android 系统很多内置的数据都是以 ContentProvider 的方式提供访问的。比如通讯录，电话记录，短信等等。

Android 在 android.provider 这个包下提供了很多支持这个功能的帮助类。


## 网络存储

手机上的数据再怎么存储都属于临时的，换个手机啥都没了，所以最终极的存储是网络存储了。




