# ubuntu下无法启动ADB
- 2015-03-06 06:56:00
- 操作系统与开发环境
- ubuntu,adb,

<!--markdown-->ubuntu版本：11.10 64位系统,使用 adb 的时候报加载共享库 libncurses.so 出错.需要安装 ia32-libs 。


<!--more-->


./adb 的时候报错：error while loading shared libraries: libncurses.so.5: wrong ELF class: ELFCLASS64

报错的信息大概也写得很清楚，但是貌似对我来说没用，google了一下。

解决方案：

    sudo apt-get install ia32-libs

据说是某个lib出错了，需要重新安装。稀里糊涂就这样能弄好了，不明所以，仰拜大神们。