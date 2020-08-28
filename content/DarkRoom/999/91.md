# Android BroadcastReceiver 的简单用法。
- Android,broadcastreceiver,

BroadcastReceiver 有两种注册方式，一个是BroadcastReceiver单独写一个类，注册到XML里；一个是在具体代码里临时创建和销毁。


各有各的好处。实现方式不尽相同，但是主要的几个类和方法都一样。

## 类和方法

1 . IntentFilter 过滤器。

- addAction(); 给过滤器增加监听的动作。对应的这个功能也可能出现在XML里。

2 . BroadcastReceiver 主角

- onReceive() 这个不多说了。要的就是它了。一般习惯，第一行打印日志看看。

3 . Context 背后主使者

- registerReceiver()
- unregisterReceiver() //这个别忘鸟……
- sendBroadcast()


简单的应用这些应该就够了，高级的慢慢再研究吧。

反正这种东西经常是用一次，学一次，忘一次，不过道理懂了，即使忘了也没啥影响。具体API想不起来可以查嘛。
