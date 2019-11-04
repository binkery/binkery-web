# Android Video 查询 Thumbnail 出错
- 2015-03-06 09:37:04
- Android
- android,sql,video,thumbnail,缩略图,

<!--markdown-->刚才在查询Video的thumbnail的时候，发现一个问题。


<!--more-->


代码：

    Video.query(context.getContentResolver(), Video.Thumbnails.EXTERNAL_CONTENT_URI, null);

抛出下面的异常：

    android.database.sqlite.SQLiteException: no such column: _display_name: , while compiling: SELECT * FROM videothumbnails ORDER BY _display_name

没有_display_name这一个column . SELECT * FROM videothumbnails ORDER BY _display_name 这个sql 语句很明显是系统自己组装的。

后来换了一个方式

    context.getContentResolver().query(Video.Thumbnails.EXTERNAL_CONTENT_URI,null, null, null, null);

这个方法能正常运行，并且从打印的日志上看，确实没有_display_name这个column。目前不清楚这个算不算是一个Bug，这个Bug算Android还是三星的，因为我只在我的一个测试机上跑了一下。但不管怎样，目前来看，只有第二个方法是可行的了。

另外， Video.Thumbnails.EXTERNAL_CONTENT_URI 对应的路径为：
content://media/external/video/thumbnails