# nginx ssl 编译问题
- nginx,ssl,https
- 2018.04.26

在给我的网站配置 https 的时候，出现 unknown directive "ssl" 的问题，这个问题的主要原因就是 nginx 缺少 ssl 模块，解决的办法也很简单，就是重新编译一个带 ssl 的 nginx。

https 是目前网站的标准配置了，各大厂商开始在推广和普及 https。

经过一番折腾，给自己的网站申请了一个 https 证书。开始往 blog.binkery.com 网站上配置证书。

	server {
        listen 443;
        server_name blog.binkery.com; #填写绑定证书的域名
        ssl on;
        ssl_certificate blog_binkery.com_bundle.crt;
        ssl_certificate_key blog.binkery.com.key;
        ssl_session_timeout 5m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2; #按照这个协议配置
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;#按照这个套件配置
        ssl_prefer_server_ciphers on;
        location / {
            root   html; #站点目录
            index  index.html index.htm;
        }
    }

上面的配置还是比较普通的，很多教程都有了。配置完了重启 nginx 服务器。结果出现了下面的错误。

	nginx: [emerg] unknown directive "ssl" in /usr/local/nginx/conf/conf.d/blog.conf:4

google 了一下，结论是安装 nginx 的时候，没有配置 ssl 模块。需要重新编译一下 nginx 。还好我当时编译完后源代码并没有删掉。

进入到源代码所在目录下，执行下面的命令，配置编译的时候加入 ssl 模块。

	./configure --with-http_ssl_module

然后执行编译

	make

特别注意，这里不要执行 make install 。make install 会覆盖安装。执行完 make 后，会在 objs/ 目录下生成一个 nginx 可执行文件。我们需要把这个 nginx 文件替换掉现在的 nginx 文件。首先先备份一下原来的 nginx 文件，然后再替换。

	cp /usr/local/nginx/sbin/nginx /usr/local/nginx/sbin/nginx.bak
	cp objs/nginx /usr/local/nginx/sbin/nginx

替换后就可以重启 nginx 了。

	/usr/local/nginx/sbin/nginx
