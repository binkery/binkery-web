# nginx 配置 http 跳转到 https 实现全站 https
- nginx,http,https
- 2018.04.26

有了 https 那么就希望 http 的请求都跳转到 https。在最新的 nginx 的配置还是比较简单的。

## 实现全站 https

全站 https 的重要性不用多说，要跟上时代潮流。

这里只贴出简要的代码，server 443 的省略代码可以在网上找一找，很容易找到的。这里只描述一下 http 跳 https 的方式。

目前最新版本的 nginx 还是比较简单的，直接加一个 301 跳转就行。

	server {
		listen    80;
		server_name    blog.binkery.com;
		return    301 https://$server_name$request_uri;
	}

	server {
		listen    443 ssl;
		server_name    blog.binkery.com;

		[..这里省略了很多代码..]
	}

这些都配置完后，重启一下 nginx 就可以工作了。非常干净漂亮。
