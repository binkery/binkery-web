# 【原创】Android Handler和Message
- 2014-11-20 05:44:10
- Android
- android,handle,message,线程,

<!--markdown-->## handler的作用

在 Android 程序启动时，系统会开一个线程，这个线程是主线程，也就是 UI 线程。在实际运用的过程中，可能需要在 UI 线程中进行一个比较耗时的操作，这个时候如果主线程等待的时间如果超过5秒，Android 系统会提示强制关闭。这个时候就需要把这些耗时的操作移动到子线程去完成。但是至今新开一个子线程是不行的。因为 Android 的 UI 绘制只在主线程里做。子线程是起不到作用的。


<!--more-->


handler是运行在主线程中的，通过 Message 来与子线程传递数据。handle 接受到数据以后再进行 UI 的操作。

## Message

Message 是用来 handler 和子线程传递数据的一个类。

## 实现思路

继承实现 handle，重写 public void handleMessage(Message msg) 这个方法。一般在这个方法里，先判断 msg.what，这是一个 int 类型参数。然后在获取 msg 里的数据。

在子线程里生成一个 message 对象，然后是对 msg 进行各种赋值，使用 handle.sendMessage(Message msg)。 Message 这个类的构造器是公开的，也就是说你可以直接用，不过有另外一个方法来获取一个 Message 对象。调用 Message.obtain() 或者 Handler.obtainMessage()。调用这两个方法获取的是从一个可回收的对象池里获取一个Message对象。也就是这两个方法是从池里获取的，跟你直接 new 出来的还是有点区别的。具体运用中怎么去适应就看具体情况了，如果是用一次也就没必要从池里捞了。不过还是建议不直接 new ，毕竟人家推荐的。

这些是简单的一些操作，应该能满足一般的使用，如果有更复杂的需求的话，还是建议看看官方文档对这几个类的描述。英文学好了还是有些用的。