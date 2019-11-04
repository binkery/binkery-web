# Android 服务之 AlarmManager
- 2014-12-06 08:26:13
- Android
- android,service,alarmmanager,闹钟,

<!--markdown-->AlarmManager 提供了系统闹钟服务。允许你在未来的某一个时间点安排运行你的应用程序。当一个闹钟响起，在系统中已经注册的intent会被系统广播出去，自动地启动一个已经不再运行的目标应用。被注册的闹钟在设备休眠的时候也会被保留，并且在设备休眠的时候，如果闹钟的时间到了，也有可能唤醒设备。但这些注册会在设备关机和重启的时候被清空。

Alarm Manager 在alarm receiver 的 onReceive() 方法执行的时候会拥有一个 CPU 唤醒锁。这样保证设备在你实行完这次广播之前不会休眠。一旦onReceive() 返回，Alarm Manager 就释放这个锁。这意味着在某些情况下，设备会在onReceive() 方法完成的时候马上进入休眠。如果你的alarm receiver 调用Context.startService()的话，设备有可能在你请求的service启动前已经休眠了。预防这样的事情发生，你的BroadcastReceiver 和 Service 需要实现一个单独的wake lock，来确保设备在service变成可用的时候一直在运行中。

Alarm Manager 来用在一些情况下，你需要你的应用程序在一个特殊的时间运行，即使应用当前不再运行中。对于一些常规的定时操作，它比使用 Handler 简单和更有效率。

从 API 19(KITKAT) 开始，alarm 交付变成不精确了 ：系统为了减少唤醒和电池使用会关掉alarm。有新的API来用支持那些需要保证精确交付的应用程序。setWindow(int,long,long,PendingIntent) 和 setExact(int,long,PendingIntent) .那些 targetSdkVersion 早于19的应用程序会继续执行之前的行为，alarm 会在被请求的情况下，精确的交付。交付，原文是 delivery，不知道具体怎么翻译，感觉交付还是比较 OK 的。