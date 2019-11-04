# Android 开源项目之 Volley
- 2014-11-21 08:15:50
- 开源项目
- android,开源项目,

<!--markdown-->Volley 是一款 Android 网络通信开源框架，由 Google 在 Google I/O 2013 发布。这是由 Google 官方提供的，肯定错不了。Volley 是 Android 平台上的网络通信库，减少了开发者在网络通信编程过程的工作量，并且提供一个高效，稳定，易用的 API  。Volley 名字的由来：a burst or emission of many things or a large amount at once .


<!--more-->


先上几个地址。
    Volley 主页 ：  https://android.googlesource.com/platform/frameworks/volley
    Git clone 的地址 ： https://android.googlesource.com/platform/frameworks/volley 

## volley 的使用场景

根据 volley 的特点，也是 volley 的出发点，就是为了帮助解决一般项目开发过程中需要的 HTTP 的请求的处理，比如 server API 请求的发送和数据的接收，网络图片的加载等。这些东西呢，其实自己也可以做到，volley 并没有增加什么特别的新的东西，就是对一些工具类的封装，让你使用起来更加方便，也省去了你自己开发的过程中遇到的一些问题，而且人家会设计好各个接口，满足不同的场景的需求，同时也会考虑性能的需求，并且可以获得长期的支持。至少 volley 这个项目零零星星的，还是一直有一些代码的checkin 的，说明还是有人在维护的。