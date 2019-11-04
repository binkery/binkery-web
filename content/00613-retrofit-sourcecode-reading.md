# Retrofit 源代码阅读笔记
- 2019.06.12
- Android
- Android,开源库
- Android源代码,Retrofit源代码阅读,Retrofit源代码解析,Retrofit源代码解读,Android开源库

## Retrofit 动态代理

在使用 Retrofit 的时候，我们需要写一个接口，比如 Api，每一个网络请求都对应到接口里的一个方法。在我们需要发送网络请求时，通过 Retrofit.create(Api.class) 的方式，可以获得一个 Api 对象，而我们定义的 Api 是一个接口。在这里，Retrofit 是通过动态代理的方式，给我们返回一个 Api 的对象。
