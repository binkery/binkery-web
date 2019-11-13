# Eclipse – “Too many open files” Problem
- android,eclipse,error,命令行,终端,配置,
- 2015-03-06 10:05:33

在开发的时候遇见这个问题，总是提示Too many open files。日志如下：


    Errors occurred during the build.
    Errors running builder 'Android Pre Compiler' on project 'binkery-demo'.
    Errors occurred while refreshing resources with the local file system.
    Could not write metadata for '/home/binkery/workspace/.metadata/.plugins/org.eclipse.core.resources/.projects/binkery-demo/.indexes/properties.index'.
    /home/binkery/workspace/.metadata/.plugins/org.eclipse.core.resources/.projects/binkery-demo/.indexes/properties.index (Too many open files)
    Errors occurred while refreshing resources with the local file system.
    Could not write metadata for '/home/binkery/workspace/.metadata/.plugins/org.eclipse.core.resources/.projects/binkery-demo/.indexes/properties.index'.
    /home/binkery/workspace/.metadata/.plugins/org.eclipse.core.resources/.projects/binkery-demo/.indexes/properties.index (Too many open files)

在网上找了一下，貌似跟ubuntu下个配置有关。老外是这么说的：

> Eclipse – “Too many open files” Problem
> If your OS is Linux and you are using Eclipse, you might possibly see the following error messages or similar after installing lots of plug-ins in Eclipse. In my case, it usually happened after installing TPTP (I’m using Ubuntu Linux 9.04 Jaunty Jackalope Desktop 64bit by the way).

打开命令行终端，

    $lsof | wc -l

这个命令能打印出当前打开的文件数目。我的打印出来是5000+

    $lsof | grep eclipse | wc -l

这个命令打印出eclipse打开的文件数目。我的打印出来是有500+。

    $ ulimit -a
    core file size          (blocks, -c) #
    data seg size           (kbytes, -d) #
    scheduling priority             (-e) #
    file size               (blocks, -f) #
    pending signals                 (-i) #
    max locked memory       (kbytes, -l) #
    max memory size         (kbytes, -m) #
    open files                      (-n) 1024
    pipe size            (512 bytes, -p) #
    POSIX message queues     (bytes, -q) #
    real-time priority              (-r) #
    stack size              (kbytes, -s) #
    cpu time               (seconds, -t) #
    max user processes              (-u) #
    virtual memory          (kbytes, -v) #
    file locks                      (-x) #

这个命令能打印一些数据出来，具体啥意思不打了解。
或者

    $ulimit -n

直接打印出来一个1024。这个1024应该是你当前电脑上的配置的数目。
这个时候需要修改这个数目，让它大一点。

老外这么说的：
> To change it, open the file /etc/security/limits.conf and put a greater number than 1024 depending on the number of open files you checked with lsof | wc -l just before.

    $ gksudo gedit /etc/security/limits.conf

add these lines

    *                soft    nofile          9216
    *                hard    nofile          9216

把这两行加进去。注意要有前面的*号。
然后注销一下重新登录进来看一下

    $ulimit -n

这个时候应该是9216了。

到目前为止，使用这个方法很好，没有再出现那个烦人的error提示了。持续观望中。

新学了几个终端命令。

* lsof
* ulimit
* gksudo

特别是gksudo，一开始我以为是老外打错了，或者复制带过来的，我用sudo命令去做，没有任何提示错误，但是那个值就是一直修改不了，后来改用gksudo，ok了。
