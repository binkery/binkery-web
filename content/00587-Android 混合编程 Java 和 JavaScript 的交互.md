# Android 混合编程 Java 和 JavaScript 的交互
- 2017-12-28 10:08:07
- Android
- android,webview,javascript,混合编程,

<!--markdown-->现在，在移动端做混合编程已经不是什么新鲜事了，在大家的应用中，或多或少都会用到一些。混合编程的好处不用多说，大家也都心里明白，缺点也是一样的，痛并着快乐，大家都懂的。

对于 Android 来说，实现混合编程，离不开下面几个重要的 API。

- WebViewClient.shouldOverrideUrlLoading(Webview view,String url)
- Webview.addJavascriptInterface(Object object,String name)
- Webview.evaluateJavascript(String script,ValueCallback<String> callback) 【注：>= KITKAT 19】
- Webview.loadUrl("javascript:" + script);

其中第三个和第四个是一样的，第三个只在 API >= 19 的版本中支持。第四个是 Webview 一开始就有的方法。

## shouldOverrideUrlLoading

先说 shouldOverrideUrlLoading 这个 API。这个 API 很常用，在 HTML 或 JavaScript 发起一个新的页面请求的时候，Java 层可以收到这个回调返回，并且有机会进行拦截。那么在 HTML 中，什么样的操作下，Java 层会收到回调呢？

第一种是 HTML 中的 a 标签，很普通的超链接。但用户点击 HTML 页面中的超链接的时候，Java 层可以收到回调。

    <a href="http://www.binkery.com/">Text</a>

第二种是 Javascript 的 window.location.herf 。很多时候前端会给某个 div 设置一个 click 事件，在 click 事件中做页面的跳转。

    window.location.href="http://www.binkery.com/"

第三种是 JavaScript 添加 iframe 。在向 document 中添加完 iframe 后，马上进行了删除。这种方法是第二种方法的升级版。setTimeout 是 javascript 中实现异步的一种方式。

    var iframe = document.createElement('iframe');
    iframe.style.display='none'
    iframe.src='http://www.binkery.com';
    document.documentElement.appendChild(iframe);
    setTimeout(function() { document.documentElement.removeChild(iframe) }, 0)

通过以上三种方式，在 shouldOverrideUrlLoading 方法都会收到回调，并且可以得到 URL，可以根据 URL 进行逻辑处理。

## addJavascriptInterface

这个 API 可以向 JavaScript 中的 window 对象添加一个对象。首先 window 是 JavaScript 中的一个特殊的对象。然后，在 JavaScript 中，可以很自由的往对象上添加属性。

    webview.addJavascriptInterface(new Android(),"android");
    class Android{
        @JavascriptInterface
        public String sayHello(String message){
	    Log.i("TAG","say hello " + message);
	    return "say hello " + message;
        }
     }

比如我们在 Native 中定义一个普通的 Java 类，叫 Android，然后调用这个方法，new 出一个 Android 的对象，传递的值是 "android"。那么在 javaScript 代码中，我们可以使用 window.android.xxx 的方式去调用 Java 层的代码，并且可以获得一个返回值。

    <script>
        var message = window.android.sayHello("binkery"); 
        // message = "say hello binkery"
    </scpirt>

## evaluateJavascript 和 loadUrl

在 Java 代码中，也可以调用 javascript 的方法。假设我们有以下的 javascript 方法。

    <script>
        function sayHello(name){
            return "say hello " + name + " from js.";
        }
    </script>

然后我们可以通过这样的方式调用这个方法。

    webview.loadUrl("javascript:window.sayHello('binkery');");

在 API >= 19 ，我们还可以使用 evaluateJavascript 方法。这个方法可以得到 javascript 的返回值。loadUurl 的方法是收不到返回值的。

    webview.evaluateJavascript(script , new ValueCallback<String>(){
        public void onReceiveValue(String value){
            Log.i(TAG,value); // value = say hello binkery from js
        }
    });
