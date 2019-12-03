# Python 3 安装
- Python3,Python
- 2018.03.01

Python3 是目前最新的版本，区别于之前的 python2，语法还是存在挺多不一样的。这里介绍如何安装 Python3。

## 下载前准备

需要安装以下库，不然会有问题。

    yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make

## 下载 Python3 源码

因为我本地环境是 3.5.2，为了保持一致，我在服务器上也安装的是 3.5.2

    wget http://mirrors.sohu.com/python/3.5.2/Python-3.5.2.tar.xz

## 解压缩并安装

    xz -d Python-3.5.2.tar.xz
    tar xf Python-3.5.2.tar -C /usr/local/src/
    cd /usr/local/src/Python-3.5.2/
    ./configure --prefix=/usr/local/python3
    make -j8 && make install

## 安装的目录

默认情况下，python会安装在

    /usr/local/python3

## 环境变量

为了你可以全局的使用 python3 ，最好还是加上全局变量。当然有些人会通过添加链接的方式来实现，这样也是可以的。

    PATH=$PATH:/usr/local/python3/bin

## 验证安装是否成功

    python3 -V

如果可以正常打印出 python 的版本，证明安装是成功的。同时 pip3 也是可以使用的。pip3 也是在 /usr/local/python3/bin 目录下，如果环境变量设置正确的话，相关命令都可以使用了。
