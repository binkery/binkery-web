# Android 和 iOS 混合编程
- 2015-03-06 13:33:54
- Android
- android,ios,混合编程,

<!--markdown-->这里的混合编程，不是Android 和 iOS 之间的混合，是Android 和 HTML/JavaScript 之间的混合编程，和 iOS 和 HTML/JavaScript 之间的混合编程。


<!--more-->


HTML 开发有诸多的优势，但是纯HTML 开发也有着一些局限，所以使用混合编程，可以相互整合，相互弥补直接的弱点。但是看上去很美的东西，其实还是有很多坑的。

WebView 组建是大部分UI系统都有的一个重要的组建。在Android 就是 WebView ，在 iOS 里是 UIWebView 。基本上都是一个意思，load 一个 HTML 页面，并且可以执行 JavaScript 脚本。这样的混合编程带来了不少的好处，就是减少开发的成本，特别是像 PhoneGap 这样的产品，帮你集成了很多 API ， 这样开发者就可以专心做应用了。

之前一直只做 Andriod Hybrid 开发，Android 里对 WebView 的功能还是很全的，而且可以通过 addJavaScriptInterface 来进行扩展，让 JavaScript 代码可以直接调用 Java 代码，并且同步返回值。但是最近在 iOS 上就碰见了问题了。 iOS 是使用另外的一套机制来实现的，必须当页面发起一个请求的时候，OC 层才可以捕获到事件，并且去处理，处理完成后，再调用 JavaScript 来传递值。这是一个异步的方法。同时，需要页面发起请求，这个是怎么做到的呢？参考PhoneGap 的做法，在当前页面里，增加一个 iFrame 对象，这个 iFrame 的宽高都为0，并且不可见，iFrame 的src 的值，就是最终传递到 OC 层的请求，这个可以自定义协议。