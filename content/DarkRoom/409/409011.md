# Ubuntu 下代理和 pac 设置
# ubuntu,proxy,pac文件
# 2019.04.16

在 Ubuntu 16.04 上升级 Chrome 73 后，发现代理并不好用，系统设置的代码选项不起作用。

最后的解决方案是在启动 chrome 的时候添加对应的参数。我的方法是直接修改桌面快捷方式的启动参数，其他方式也可以。主要就是 --proxy-server 和 --proxy-pac-url 这两个参数。


    /usr/bin/google-chrome-stable --proxy-server=socks5://127.0.0.1:1080 --proxy-pac-url=file:///etc/shadowsocks/autoproxy.pac

修改启动参数后，内网的文档可以访问，墙外的 google 也可以访问，非常完美。

内网的域名可能需要添加到 autoproxy.pac 对应的地方。
