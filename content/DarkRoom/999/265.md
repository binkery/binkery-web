# adb shell 启动应用程序
- android,adb,ant,shell,脚本,
- 2013-08-22 08:17:02


命令：

    adb shell am start -n 包名/.Activity名字

创建一个自动编译，安装程序的脚步。

新建一个sh文件，例如 app.sh 在项目的目录下。与src res 等同级目录。

    app.sh
    ant clean & ant debug
    adb uninstall 包名
    adb install bin/项目名-debug.apk
    adb shell am start -n 包名/.Activity名字

ant 命令找不到的话，说明你没有安装，或者ant命令没有被添加到PATH里。

ant 命令执行错误的话，可能是local.properties文件错误或者没有这个文件。

在项目目录下新建一个 local.properties文件，里面加入一行：

    local.propertiessdk.dir=/home/xxx/android-sdk-linux

这里的目录要指向你的sdk的目录。这两个文件都是普通的文本文件，在每一行前面加上#符合，表示注释。
执行脚本的命令：

    sh app.sh

运行这个脚本，你剩下需要做的就是等待了。

我总觉得这样比用 eclipse 用鼠标点要快。另外，当你在 eclipse 里修改完代码，保持，然后去执行 ant clean 和 ant debug 的时候，可能会出现一些问题，两边都在编译你的代码。所以最好可以在eclipse 里把自动编译的选项去掉。project -> Build Automatically这个选项会在你每次保存的时候，编辑一次程序。
