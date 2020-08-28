# DNS 和 HttpDns
- DNS,HttpDns,Https
- 2018.04.17

DNS 是域名解析服务，由于 DNS 设计的一些特点，导致它是比较容易收到攻击的。DNS 劫持是比较普遍的互联网攻击方式。DNS 节点服务器故障也比较容易造成大面积的网络问题。在移动客户端，为了避开 DNS 的这些问题，于是有了 HttpDns 的解决方案。

## 域名

互联网最开始是在美国的几个大学的电脑相互通信设计的，随着电脑越来越多，ip 地址的记忆是非常枯燥无聊的事情，于是就有域名。目前，域名由一个国际组织来管理，ICANN The Internet Corporation for Assigned Names and Numbers 。互联网名称与数字地址分配机构，这是一个非营利性的国际组织，包括 ip 地址的分配也是由它来分配的。域名注册由它授权的一些域名注册商进行注册。它向域名注册商收取少量的管理费，域名注册商向域名注册者再收取管理费。大概就是这样的方式，每个人都可以自由的注册域名。只要你注册的域名没有被别人注册，那么你就可以注册。选择一个你喜欢的域名注册商，向它提交你要注册的域名，以及你的信息，你就可以完成你一个域名的注册。一旦注册上了，这个域名就属于你了。当然，你需要每年记得续费。如果你忘记续费了，当这个域名会进入一段时间的高价赎回期，这个时间内，只有你可以续费，但是会比较贵。过了这个高价赎回期，这个域名就进入了自由注册时期，任何都可以再次抢注这个域名。

## DNS

一个域名要可以使用的话，需要把它指向一个具体的 ip 地址。你需要有一台主机，然后获得这台主机的 ip 地址，然后进行域名解析。域名注册商提供域名解析服务，一般都是免费的。

DNS 是一个分布式的系统，由一个主根服务器，和十二个辅根服务器组成。主跟在美国，12个辅根中有9个在美国，日本、英国、瑞典各有一个辅根。可以看出美国是主要的节点，然后是欧洲，再然后是亚洲。DNS 主要使用的是 UDP 协议，使用 53 端口。当一台主机发起一个 DNS 查询的时候，并不是直接向根服务器发起查询，而是先向本地 DNS 服务器发起查询，然后本地 DNS 再进行向上一级的查询。最终得到域名的 IP 地址。查询有递归查询和迭代查询两种方式，现在的 DNS 基本都是采用递归查询和迭代查询集合的方式，这样可以一定程度上提高效率。

DNS 的解析过程就存在一定的风险，当中间某个 DNS 服务器有意的进行篡改或者受到的攻击，把你的域名指向了一个恶意的 ip 地址，那么所有这个 DNS 服务器服务的主机都会收到影响，他们会得到错误的 ip 地址，请求的数据会向错误的 ip 发送。

特别是针对客户端的 DNS 劫持，目前比较流行的是使用 HttpDns 的方式来规避 DNS 劫持的风险。

## HttpDns

HttpDns 最开始主要是为了规避 DNS 劫持的。其主要的原理就是向一个 HttpDns 服务器发起一个 Http 请求。这个 HttpDns 服务器不使用域名，直接使用 ip 地址，这样就避免了 DNS 劫持。HttpDns 会返回域名的解析结果，这样客户端就可以用 ip 地址替换域名的方式，发起正常的 http 请求了，这样整个过程就不用 DNS 了，也就避免了 DNS 劫持了。

HttpDNS 的方式，存在的一个向 HttpDns 发起的 Http 请求时被劫持的风险。对于这样的风险比较简单的解决办法就是 https 了。 HttpDns + https + 本地缓存的方案，可以大大的提高客户端的访问效率，也提高了客户端的安全性。

HttpDns 在安全上，比 DNS 要高了很多。除此之外，HttpDns 还有一些其他的有点，比如在 HttpDns 域名解析的时候，就可以根据客户端的 IP 进行判断客户所处的地理位置，给其分配最近的 IP 地址，进行精确的调度，而之前的 DNS 就不能实现这样精确的调度了。当然，这样的调度是花钱的。

## Android 的实施方案

一般的公司是不会选择自己搭建 HttpDns 服务器的，采用第三方是最佳的方案。目前国内来说，阿里云和腾讯云都是可以考虑的，选择哪个就看价格了。这里不做价格比较，咱们关心实现。

下面是域名替换成 ip 地址，以及设置 Host 属性的代码。设置 Host 属性是因为你的服务器一般来说不接收直接 ip 地址的请求。url 是你原本的请求的 url，ip 是你从第三方 sdk 获得的 ip 地址。

    String url = ...
    URL oldUrl = new URL(url);
    String host = oldUrl.getHost();
    String ip = ...
    String newUrl = url.replaceFirst(host, ip);
    connection = (HttpURLConnection) new URL(newUrl).openConnection();
    connection.setRequestProperty("Host", host);

### Android 的 WebView 支持

在 App 中内嵌了大量的 H5 页面，这种也需要进行 HttpDns 的适配，不然 H5 页面还是会受到 DNS 劫持的威胁。简单代码如下

    webview.setWebViewClient(new WebViewClient() {
        // API 21及之后使用此方法
        @SuppressLint("NewApi")
        @Override
        public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) {
            String scheme = request.getUrl().getScheme().trim();
            String url = request.getUrl().toString();
            URL oldUrl = new URL(url);
            URLConnection connection = oldUrl.openConnection();
            String ip = ...
            String newUrl = url.replaceFirst(oldUrl.getHost(), ip);
            connection = (HttpURLConnection) new URL(newUrl).openConnection();
            connection.setRequestProperty("Host", oldUrl.getHost());
            return new WebResourceResponse("text/css", "UTF-8", connection.getInputStream());
        }

        // API 11至API20使用此方法
        public WebResourceResponse shouldInterceptRequest(WebView view, String url) {
            String scheme = Uri.parse(url).getScheme().trim();
            URL oldUrl = new URL(url);
            URLConnection connection = oldUrl.openConnection();
            String ip = ...;
            String newUrl = url.replaceFirst(oldUrl.getHost(), ip);
            connection = (HttpURLConnection) new URL(newUrl).openConnection();
            connection.setRequestProperty("Host", oldUrl.getHost());
            return new WebResourceResponse("text/css", "UTF-8", connection.getInputStream());
        }
    });

经过这样的修改，WebView 的 HTTP 请求也避开了 DNS 解析的过程。
