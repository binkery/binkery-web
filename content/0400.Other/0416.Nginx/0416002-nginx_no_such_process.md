# nginx 启动报 no such process 错误
- nginx,start,process,启动,配置错误
- 2018.04.26

nginx 启动的时候,报出 no such process 错误

在重新编译 nginx 后，发现启动的时候出现了下面的错误

	[root@host nginx-1.12.2]# /usr/local/nginx/sbin/nginx -s reload
	nginx:[alert] kill(1605, 1) failed (3: No such process)

具体原因大概是因为重新编译的 nginx 后，新的 nginx 可执行文件没有找到对应的 nginx.conf 目录。所以我们需要手动的指定一下。

	/usr/local/nginx/nginx -c /usr/local/nginx/nginx.conf

执行完上面的命令，再重启一下 nginx，就搞定了。
