# Android 获取控件的宽高
- 2015-03-06 10:01:05
- Android
- android,layout,布局,view,

<!--markdown-->在Android开发中，很多时候，在使用XML布局后，还需要在Java代码对内容进行一些修改或者添加之类的操作。


<!--more-->


    setContentView(layout_id)
    View view = findViewById(view_id);
    int width = view.getWidth();
    int height = view.getHeight();

这样的方式获取到的宽高都会是0.

在这些代码放在 onCreate(),onResume(),onStart() 执行的结果都是一样的。因为在这个时候还没有为这个布局算好宽高。老外是这么说的 The issue here is you are trying to get the parent height/weight before the layoutmanager completes parent layout.

另外一个老外是这么说的 One alternative to programmatically implement this is to use following method:


    public void onWindowFocusChanged(boolean b){...}

By the time this method is invoked, the layouting-process has been finished. Thus you can obtain the parent attributes correctly.

这个方法在会在布局线程结束后有个回调。至于这个方法会不会在其他的情况下回调，这个继续跟踪中……