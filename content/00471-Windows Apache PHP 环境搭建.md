# Windows Apache PHP 环境搭建
- 2016-03-22 10:27:13
- 前端技术
- php,windows,apache,

<!--markdown-->经常在 Linux 环境下搭建　php 环境，在　windows 下还是第一次，没啥技术含量，就是记录一下，省得下次还得到处乱找。


<!--more-->


## 下载地址

http://windows.php.net/download/#php-5.5
http://www.apachelounge.com/download/
http://www.microsoft.com/zh-CN/download/details.aspx?id=30679

V11是微软的一个组件，如果不安装的话会提示 msvcr110.dll丢失。

下载完后安装V11,解压 Apache 和 PHP 到你想要的目录下。

## 配置

### PHP 配置
PHP需要配置环境变量。把　;X:\php;X:\php\ext　添加到 PATH 里。

### APACHE 配置
修改　X:\Apache24\conf\httpd.conf 文件。

需要修改的：

    ServerRoot "X:\Apache24"
    DocumentRoot "X:/Apache24/htdocs"
    <Directory "X:/Apache24/htdocs">
    Listen 8080
    ServerName localhost:8080

需要添加的：

    # php5 support
    LoadModule php5_module X:/php/php5apache2_4.dll
    AddType application/x-httpd-php .php .html .htm
    # configure the path to php.ini
    PHPIniDir "X:/php"

配置好 Apache ，配置好环境变量，安装好V11，然后可能需要重启一下电脑。

## 启动 Apache

    X:\Apache24\bin\httpd.exe -k install/start/stop/restart

验证 Apache 服务器是否搭建成功，在地址栏上直接输入　127.0.0.1:8080 ,如果能打开网页，说明 Apache 是成功的。验证　PHP 是否配置成功，新建一个 php 文件比如　php.php ，输入

    <?php　phpinfo();　?>

放在　X:\Apache24\htdocs 目录下，然后用浏览器打开　127.0.0.1:8080/php.php 。
