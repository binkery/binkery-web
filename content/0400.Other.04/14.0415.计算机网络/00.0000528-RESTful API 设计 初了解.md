# RESTful API 设计 初了解
- api,restful,
- 2016-05-16 03:24:14

REST，Representational State Transfer,表现层状态转化，是一种 Web 服务交互设计的风格，而不是标准。其他相似的方案有 SOAP（Simple Object Access protocol，简单对象访问协议），XML-RPC。

## URIs

要理解 RESTful API 设计思想，首先要理解 URIs（Uniform Rsource Identifiers,统一资源标识），每一个 web 资源都有一个统一的标识，这个和 Android 的 Provider 的设计思路是一样的。作为一个标识，一般只包含名词，不包含动词。

比如　http://your.domain/user/1/article/1 表示某个用户的某篇文章。如果是用户的所有文章呢？ http://your.domain/user/1/articles 。如果我只要某个用户的 10 篇文章呢？ http://your.domain/user/1/articles?limit=10 或者 http://your.domain/user/1/articles/limit/10 。后者更符合　RESTful　API　风格一些。

这样子，一个 URI 基本可以标识一个资源元素（Element URI），或者一个集合(Collection URI)。

## HTTP method

RESTful 系统一般通过 HTTP (Hypertext Transfer Protocol) 通信，但不是只能是 HTTP 。HTTP 的请求方法除了咱们常见的　POST 和　GET 外，还有　PUT,DELETE 等。RESTful 的设计思想就是通过　PUT,GET,POST,DELETE　等表达一个动作，URI 标识资源，客户端向服务端发起一个请求，包含了动作和资源，服务器对这个请求进行响应。


这几个动作分别对应的意义：
GET : 获取
PUT : 更新
POST : 创建
DELETE : 删除

是不是很像数据库的增删改查？恩，确实是这样的。不过针对元素还是集合，处理是有些许区别对待的。

## Android

上面也说了，这种设计思路和　Android Provider 的设计思路是基本一致的，都是基于 URI,Provider 也分别提供了增删改查的方法。

## 链接
 * <http://www.ruanyifeng.com/blog/2014/05/restful_api.html>
 * <https://en.wikipedia.org/wiki/Representational_state_transfer>
 * <http://www.cnblogs.com/artech/p/3506553.html>
