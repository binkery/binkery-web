# 查看 Linux 系统信息
- linux,命令行
- 2018.08.27

我有多台服务器，在不同的地方买的（租的），都是装的 linux 系统，但是我总是忘了具体装的是什么系统，每次需要安装应用的时候，都需要先看一下操作系统。

我有多台服务器，在不同的地方买的（租的），都是装的 linux 系统，但是我总是忘了具体装的是什么系统，每次需要安装应用的时候，都需要先看一下操作系统。

## lsb_relaese

    [root@host ~]# lsb_release -a
    LSB Version : xxx
    Distributor ID : CentOS
    Description: CentOs release 6.8 (Final)
    Release : 6.8
    Codename : Final

可能会没有 lsb_release 命令。需要安装一下。

    yum install lsb -y

通过这个命令，我们就可以知道是 CentOS 系统了，也可以知道具体的版本了。

## 查看 64 位或在 32 位

    uname -m

如果是 i686 或者是 i386 表示 32 位 。如果是 x86_64 表示 64 位。这样我们就知道操作系统是多少位的了。
