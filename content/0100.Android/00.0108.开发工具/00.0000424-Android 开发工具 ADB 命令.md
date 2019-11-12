# Android 开发工具 ADB 命令
- adb,andriod,
- 2016-03-22 07:25:09

ADB 的全称是 Android Debug Bridge，Android 调试桥，这个翻译有点别扭，大概就是这个意思，是用来连接开发环境和运行设备的桥梁，是一个 debug 工具。在下载安装 Android SDK 后，adb 命令位于 \<sdk\>/platform-tools/ 目录里。可以把这个目录加入到“豪华”环境变量中，这样你可以在任何终端直接输入 adb 命令了。



这里有几个 adb 常用的用法。

 - 连接多个设备/模拟器的时候，选择接收命令的设备/模拟器

        #adb -s <serialNumber>

 - 查看已连接的设备 

        #adb devices

 - 打印日志 -c 的目的是清除之前的日志

        #adb logcat 
        #adb logcat -c && adb logcat

 - 安装 APK 

        #adb install abc.apk

 - 卸载 APK

        #adb uninstall package-name

 - 从设备/模拟器上拉取文件/目录

        #adb pull remote-file-path local-file-path

 - 向设备/模拟器推文件/目录

        #adb push local-file-path remote-file-path

 - 登录到设备/模拟器上

        #adb shell
