# Android Service startService and bindService
- Android,service,
- 2016-03-22 07:13:32


Service 和 Activity 一样，属于Android 四大组件之一。Activity 主要功能是与用户进行交互，而 Service 主要负责一些后台的服务。service 甚至可以运行在与当前 APP 不同的进程里，这样如果 APP 发生了崩溃，service 还在运行中。


## 生命周期

Service 的生命周期比 Activity 稍微简单些。其实Activity 的生命周期也很简单，相比一下，比 Service 多出来的也是因为它需要与用户交互，多出了几个生命周期的状态，Service 主要在后台运行，所以很好理解它对应的比 Activity 少了那些方法的回调。

因为 Service 的启动有两种方式，所以生命周期又相比 Activity 有些不同。但是这个区别我不想过多的去研究，因为这样子其实不好理解。

换种方式，startService 是通过 Intent 来实现 Activity 和 Service 之间的消息通信的，Service 是通过onStart() 方法来接收 Activity 发送来的请求，Intent 可以携带任何你想要传递的信息（当然尽量不要传递大对象了）；

而 bindService 是在 Activity 里直接调用 Service 里的方法，首先 Activity 需要调用 bindService(Intent,ServiceConnection,int) 获取一个Activity 与 Service之间的连接，通过这个连接，Activity 就可以直接调用Service对应的方法了。当Activity 发起一个bind请求的时候，对应的Service 里的 onBund会被调用。

不管是startService 还是 bindService ，如果当前的 Service 还不存在，就需要被创建，并且回调onCreate方法。

什么时候用startService？什么时候使用bindService？这个没有一刀切的答案，得看需求。但是个人理解，startService使用在Activity 与 Service 交互比较少的地方，Activity 的请求不需要 Service 同步相应。如果需要Service响应，可以通过 broadcast 和 Receiver进行交互。这样，我可能在 A Activity发起一个 Service 请求，在B 接收到了 Service 发送过来的广播。

bindService 获取到一个可以直接访问 Service 的对象，通过这个对象，可以直接访问 Service 的公开资源。这样的调用会更加快捷一些。但是不能调用耗时比较长的操作。

两种方法，各有优劣。重点是要记住，service的主要任务是在后台负责一些比较耗时的操作。在设计上，要利用好它。

## 远程Service

默认的，Service和Activity都是在主线程里，也就是说在同一个进程里。在同一个进程里的，被称外本地servcei。远程service是service运行在其他进程里。夸进程的调用，可以通过Android提供的AIDL的方式来实现。远程Service一是为了更好的利用系统资源，二是增强软件的健壮性，不要在一颗树上吊死。