# Google 开源项目之 GSON
- 开源项目,google,json,gson,

正如 google-gson 官网描述的，GSON ， A Java library to convert JSON to Java objects . 一个把 JSON 转化成 Java 对象的 Java 类库。是一个现在比较流行的开源项目。


不细说 JSON 与 XML 相比的种种优点了。这个开源库方便在 JSON 和 Java 对象之间的转换，不管是 client 端还是 server 端，接收到的 JSON 格式的数据，把它转换成 Java 对象，或者把 Java 对象格式化成 JSON 格式的数据，发送给另外一方。减少了解析和字符串拼接的代码编写工作量。

GSON 的使用还是比较简单的，主要是因为 JSON 的设计本来天生就非常适合面向对象思想。对于理解和使用，比起 XML 来说，要简单得多了。 Android 里以及包含的对 JSON 支持的类库，如果对 JSON 格式的解析，字符串拼接的业务逻辑不多的话，可以不使用 GSON 。