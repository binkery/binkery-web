# 在webview中，使用javascript调用java代码
- Android,java,webview,javascript,

最近在做一个项目，需要使用webview在加载完网页后，分析网页的内容。首先想到的方法是在网页加载完后的回调后，获取网页的html数据。但是在 WebViewClient 里，只有这么一个方法：public void onPageFinished(WebView view, String url) 。




也就是说没法获取HTML数据。后来在网上找了一个方法。WebView有这么一个API： **addJavascriptInterface(Object obj, String interfaceName)** 

> **Note**：Use this function to bind an object to JavaScript so that the methods can be accessed from JavaScript. IMPORTANT: * Using addJavascriptInterface() allows JavaScript to control your application. This can be a very useful feature or a dangerous security issue. When the HTML in the WebView is untrustworthy (for example, part or all of the HTML is provided by some person or process), then an attacker could inject HTML that will execute your code and possibly any code of the attacker's choosing. Do not use addJavascriptInterface() unless all of the HTML in this WebView was written by you. * The Java object that is bound runs in another thread and not in the thread that it was constructed in.
> **Parameters**:
> *obj* The class instance to bind to Javascript
> *interfaceName* The name to used to expose the class in Javascript 

 首先是写一个类，普通的类。 

    class MyJavaScriptInterface { 
        public void showHTML(String src) { 
        //do somethings 
        } 
    } 

 然后呢，添加到WebView对象上。

    WebView.addJavascriptInterface(new MyJavaScriptInterface(), "HtmlViewer");

然后是在页面加载完的回调里，执行下面的代码。

    public void onPageFinished(WebView view, String url) {
        super.onPageFinished(view, url);
        mWebView.loadUrl(“javascript:window.HtmlViewer.showHTML(‘hello’);”);
    } 

Note:WebView.loadUrl 里的参数，String 的开头是"javascript:"，然后注意一下 HtmlViewer 和 showHTML 的名字。当然在项目中，还是应该命名些比较有实际意义的名字。这里是直接拷贝别人的。 根据我的多次调试的结果，在“javascript:”后面，可以有很长的一串脚本代码。可以定义变量，可以定义函数。

 我做这个其实只是一个demo，目的是想扒别人网站上的某些数据，所以，网页的内容是别人写的，我做的是在当前的网页上，添加一些javacript代码，然后再调用我的java代码。这些代码算是完全后加的。网上有很多是在写网页的javascript的时候，就把java的相应的接口嵌进去了。

写得很乱，这个过程各种折腾，有些收获，不写点东西不痛快，写又写不出啥鸟东西。

苦逼敲代码的命。