# Ubuntu下下载Android源码
- 2015-03-06 06:50:50
- 操作系统与开发环境
- android,ubuntu,git,源码,

<!--markdown-->现在 eclipse 上的 ADT 在更新的时候会把最新的源代码下载下来了。不用那么麻烦去找源代码了。

下载Android源码，需要使用Git和repo。今天尝试过N多种失败，总的来说，就是我的ubuntu版本太低了。是9.04的，在使用sudo apt-get的时候总是找不到所要的软件。后来查了一下是，说是源的问题。好不容易找到一个可用的源，使用sudo apt-get update终于可以更新了，之前是报404错误。但是有源也没有用。里面的软件还是比较旧的。我安装的git是1.6的，后来证实，使用1.6的是不会成功的。目前最新的版本是1.7.

后来我在ubuntu 11.10的环境下，基本很顺利。下面是大概的步骤，也可以参考android的官网。

安装软件。

    sudo apt-get install git-core
    sudo apt-get install curl

创建目录，配置环境变量。

官方文档是这么说的Make sure you have a bin/ directory in your home directory, and that it is included in your path:

    $ mkdir ~/bin
    $ PATH=~/bin:$PATH

下载一个repo脚本，并修改权限Download the Repo script and ensure it is executable

    $ curl https://dl-ssl.google.com/dl/googlesource/git-repo/repo > ~/bin/repo
    $ chmod a+x ~/bin/repo

创建一个空目录，用来放源码。Create an empty directory to hold your working files. If you're using MacOS, this has to be on a case-sensitive filesystem.

更新repo版本，

    $ repo init -u https://android.googlesource.com/platform/manifest

会更新出一堆东西出来，也就是各个Android版本和分支啥的。

签出某个具体的版本：

    $ repo init -u https://android.googlesource.com/platform/manifest -b android-4.0.1_r1

需要你提供一个your name 和 your email

获取文件

    $ repo sync

然后就是漫长的download……