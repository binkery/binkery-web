# 如何从Eclipse迁移到Android Studio上
- android,google,eclipse,插件,studio,adt,
- 2013-09-12 10:42:57


在5月15号的Google I/O大会上，Google 发布了 Android Studio 开发工具。

这个开发工具是用来替换Eclipse + ADT 插件的。如何从Eclipse上迁移到Android Studio上？

官方文档<a href="http://developer.android.com/sdk/installing/migrate.html">Migrating From Eclipse

1 . 从Eclipse中导出
1 . 1 . 升级Eclipse ADT 插件到版本22或更高
1 . 2 . 在Eclipse里，File(文件) -- Export（导出）
1 . 3 . 在弹出的窗口，选择Android -- Generate Gradle Build Files
1 . 4 . 选择你要导出的项目，点击Finish（完成）
在项目的目录下，产生了一个build.gradle的文件。
2 . 导入到Android Studio上
2 . 1 . 在Android studio 上，选择File -- Import
2 . 2 . 在弹出的窗口选择项目的路径
2 . 3 . 选择Create project from existing source , 然后下一步
2 . 4 . 搞定。

注意：官方文档说了，即使不产生build.gradle文件，也可以直接导入到Android Studio 上，但是Google还是强烈建议这样子做。

> However, in order to take advantage of build variants and other advanced features in the future, we strongly suggest that you generate a Gradle build file using the ADT plugin or write your own Gradle build file for use with Android Studio.
