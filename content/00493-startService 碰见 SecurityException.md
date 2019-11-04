# startService 碰见 SecurityException
- 2016-03-22 03:44:02
- 
- 

<!--markdown--># startService 碰见 SecurityException

有人在 startService 的时候碰见了安全异常，SecurityException。而这个问题在早期的 Android 版本里是不会出现的。具体版本回头补上。原因是，为了安全，Android 对隐式启动 Service 做了一些限制。

startService 的文档下有这样的描述：

> This function will throw SecurityException if you do not have permission to start the given service.

然后又在官方文档找到了如下的描述：

> To ensure your app is secure, always use an explicit intent when starting or binding your Service and do not declare intent filters for the service.

大概意思是说为了确保安全，尽量使用显示的 intent 来startService 或者 bindService。而不要通过声明 intent filter 的方式。

但是如果你非要这么做，也是可以的，下面的意思是说，如果你确定这个 service 只会被你自己的 app 启动，也就是在 service 的声明里添加 *andriod:exported="false"* 的方式，那么系统认为这样是安全的。

> Additionally, you can ensure that your service is available to only your app by including the android:exported attribute and setting it to "false". This effectively stops other apps from starting your service, even when using an explicit intent.

那么，为什么会有这样的限制呢？

首先一开始设计的时候，Activity 和 Service 都有两种启动方式，显式和隐式。关于显式和隐式请戳这里 ： <http://blog.binkery.com/android/intent/intent.html>

显式就不说了，就是制定明确的 packagename + classname ，可以确保在一个系统内，肯定是唯一的。

如果是隐式的话，你发送了一个 intent，如果有多个组件（Activity 或者 Service）都可以响应这个 intent action 怎么办？

如果是Activity 的话，系统弹一个选择框让用户选择用哪个。如果是 Service 呢？我没细看代码，但是咱们可以排除一下。

如果是只启动一个？启动哪个？启动谁都不合适吧，毕竟 Android 只是系统，不应该干预，也没法干预，系统要做到公平。
如果都启动呢？都启动好像没问题，但是呢，安全有问题。我看谁不顺眼，我写一个相同 intent action filter 的 Service，然后你收到啥数据，我也收到同样的数据。这样不好吧～～

所以为了限制开发者犯错，Android 不建议使用隐式的方式来使用 Service，除非你保证你的service 只有自己家里用，那 Android 可以不管。
