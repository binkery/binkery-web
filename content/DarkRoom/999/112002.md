# Android WebView 的方法只能在 UI 线程中运行
- Android,WebView,线程
- 2018.04.25

根据报错信息，Android 的 WebView 所有的方法都只能在 UI 线程中调用，在非 UI 线程调用都会产生一些意外的崩溃。

今天分析收集到的崩溃日志，看到一下的一些日志信息。发生的机型主要集中在 4.3 的机型中。很奇怪在更高的版本中，并没有发现这样的问题。记录一下，以备后续观察。

通过日志可以看出，所有的 WebView 方法都只能在 UI 线程中被调用。


	java.lang.RuntimeException: java.lang.Throwable: Warning: A WebView method was called on thread 'WebViewCoreThread'. All WebView methods must be called on the UI thread. Future versions of WebView may not support use on other threads.
	at android.webkit.WebView.checkThread(WebView.java:2093)
	at android.webkit.WebView.loadUrl(WebView.java:836)
	at com.binkery.android.utils.webviewbridge.Bridge.executeJavascript(Bridge.java:260)
	at com.binkery.android.utils.webviewbridge.Bridge.executeJavascript(Bridge.java:229)
	at com.binkery.android.utils.webviewbridge.Bridge.dispatchMessage(Bridge.java:113)
	at com.binkery.android.utils.webviewbridge.Bridge.queueMessage(Bridge.java:100)
	at com.binkery.android.utils.webviewbridge.Bridge.access$300(Bridge.java:25)
	at com.binkery.android.utils.webviewbridge.Bridge$2.callback(Bridge.java:202)
	at com.binkery.android.webview.AbsMethod.doResponse(AbsMethod.java:48)
	at com.binkery.android.webview.methods.MethodVolunteer.downResponse(MethodVolunteer.java:43)
	at com.binkery.my.volunteer.DownQRSaveUtil$1.handleMessage(DownQRSaveUtil.java:35)
	at android.os.Handler.dispatchMessage(Handler.java:99)
	at android.os.Looper.loop(Looper.java:137)
	at android.webkit.WebViewCore$WebCoreThread.run(WebViewCore.java:1092)
	at java.lang.Thread.run(Thread.java:841)
	Caused by: java.lang.Throwable: Warning: A WebView method was called on thread 'WebViewCoreThread'. All WebView methods must be called on the UI thread. Future versions of WebView may not support use on other threads.
	at android.webkit.WebView.checkThread(WebView.java:2084)
	... 14 more
	java.lang.Throwable: Warning: A WebView method was called on thread 'WebViewCoreThread'. All WebView methods must be called on the UI thread. Future versions of WebView may not support use on other threads.
	at android.webkit.WebView.checkThread(WebView.java:2084)
	at android.webkit.WebView.loadUrl(WebView.java:836)
	at com.binkery.android.utils.webviewbridge.Bridge.executeJavascript(Bridge.java:260)
	at com.binkery.android.utils.webviewbridge.Bridge.executeJavascript(Bridge.java:229)
	at com.binkery.android.utils.webviewbridge.Bridge.dispatchMessage(Bridge.java:113)
	at com.binkery.android.utils.webviewbridge.Bridge.queueMessage(Bridge.java:100)
	at com.binkery.android.utils.webviewbridge.Bridge.access$300(Bridge.java:25)
	at com.binkery.android.utils.webviewbridge.Bridge$2.callback(Bridge.java:202)
	at com.binkery.android.webview.AbsMethod.doResponse(AbsMethod.java:48)
	at com.binkery.android.webview.methods.MethodVolunteer.downResponse(MethodVolunteer.java:43)
	at com.binkery..DownQRSaveUtil$1.handleMessage(DownQRSaveUtil.java:35)
	at android.os.Handler.dispatchMessage(Handler.java:99)
	at android.os.Looper.loop(Looper.java:137)
	at android.webkit.WebViewCore$WebCoreThread.run(WebViewCore.java:1092)
	at java.lang.Thread.run(Thread.java:841)
