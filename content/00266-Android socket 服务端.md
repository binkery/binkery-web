# Android socket 服务端
- 2016-12-13 08:18:01
- Android
- 

<!--markdown-->想在Android 上跑一个 socket 服务端。把在java工程里运行起来的代码直接放到android项目里来，开启线程，创建ServerSocket对象，创建对象的时候报错了。

    W/System.err( 3998): java.net.SocketException: socket failed: EACCES (Permission denied)
    W/System.err( 3998): at libcore.io.IoBridge.socket(IoBridge.java:583)
    W/System.err( 3998): at java.net.PlainSocketImpl.create(PlainSocketImpl.java:201)
    W/System.err( 3998): at java.net.PlainServerSocketImpl.create(PlainServerSocketImpl.java:38)
    W/System.err( 3998): at java.net.ServerSocket.<init>(ServerSocket.java:98)
    W/System.err( 3998): at java.net.ServerSocket.<init>(ServerSocket.java:69)
    W/System.err( 3998): at com.binkery.http.server.HttpServer.run(HttpServer.java:34)
    W/System.err( 3998): at java.lang.Thread.run(Thread.java:864)
    W/System.err( 3998): Caused by: libcore.io.ErrnoException: socket failed: EACCES (Permission denied)
    W/System.err( 3998): at libcore.io.Posix.socket(Native Method)
    W/System.err( 3998): at libcore.io.BlockGuardOs.socket(BlockGuardOs.java:181)
    W/System.err( 3998): at libcore.io.IoBridge.socket(IoBridge.java:568)
    W/System.err( 3998): ... 6 more

缺少权限的问题。

    <uses-permission android:name="android.permission.INTERNET" />

加上权限之后，一直出现这个问题，很郁闷。

    W/System.err( 4232): java.net.BindException: bind failed: EACCES (Permission denied)
    W/System.err( 4232): at libcore.io.IoBridge.bind(IoBridge.java:89)
    W/System.err( 4232): at java.net.PlainSocketImpl.bind(PlainSocketImpl.java:150)
    W/System.err( 4232): at java.net.ServerSocket.<init>(ServerSocket.java:100)
    W/System.err( 4232): at java.net.ServerSocket.<init>(ServerSocket.java:69)
    W/System.err( 4232): at com.binkery.http.server.HttpServer.run(HttpServer.java:34)
    W/System.err( 4232): at java.lang.Thread.run(Thread.java:864)
    W/System.err( 4232): Caused by: libcore.io.ErrnoException: bind failed: EACCES (Permission denied)
    W/System.err( 4232): at libcore.io.Posix.bind(Native Method)
    W/System.err( 4232): at libcore.io.ForwardingOs.bind(ForwardingOs.java:39)
    W/System.err( 4232): at libcore.io.IoBridge.bind(IoBridge.java:87)
    W/System.err( 4232): ... 5 more

后来在stackoverflow.com 上找到了答案，百度不给力啊，关键时候还是google，google能search到这些答案，百度很无力啊。
这个是链接：
http://stackoverflow.com/questions/2694797/bindexception-with-internet-permission-requested

原因呢，是端口号不能低于1024，据说是Linux的问题。这个待考证吧。

    Either root your phone, modify the firmware, or don't bind to ports lower than 1024. That's a Linux thing more than an Android thing.

我本来打算用80端口的，结果不能用。我用无参的构造器的时候，也没有给我返回一个自动分配的端口。
我觉得这个问题还是有可能通过其他方式解决的。80端口除非被占用了，不然还是能有办法搞到手的。现在只能老习惯，9527占用端口了。

    mServer = new ServerSocket(9527);

有个地方搞错了。刚才看了一眼API，无参的ServerSocket（） 返回一个未绑定ServerSocket , 使用ServerSocket(0) 才是返回系统自动分配的端口。

不过还没有找到关于1024的问题。

2016.12.13 更新

比较悲剧的是，多年以后 google 问题 google 到自己当年写的破玩意～～

上面的问题都是比较初级的问题了，一个是没有权限，一个是端口号的问题。端口号确实是不能少于 1024 的，1024 以下被定义为保留端口，所有一般不能使用。当然是一般不能使用了，说明还是有办法的，这里就不讨论了（主要我也不知道～～）。

最近我又再次碰见 socket failed: EACCES (Permission denied) 的问题，但这次可以肯定的是 application 的权限是有的，而且是正确的，因为我这是在一个正在运行的线上的商业项目中的，这种低级的问题是不能的。但是在错误日志的收集中还是看见了若干这样的报错，感觉有些困惑。

鉴于只是少量用户碰见这样的问题，大概的推测为兼容性问题，一直以来，Android 的网络权限都是安装时授权的，不管是6.0之前还是 6.0 之后，所以当运行的时候碰见因为网络权限拒绝的问题，大概可以确定是部分机型的兼容性问题。

部分机型，特别是国内机型，在设置里会有针对每个应用单独的网络权限控制，在国内目前高昂的流量资费的大背景下，很多机型都提供给用户可以为每个应用设置网络权限的方式，还有可以分别设置 wlan 或者数据。