# Android 权限管理之 \<uses-permission\> 标签
- Android,权限,permission,


\<uses-permission\>标签位于 Manifest.xml 文件里，现在的 IDE 会提示需要把 <uses-permission> 标签写于 <application> 之前。


语法：

    <uses-permission android:name="string" android:maxSdkVersion="integer" />

Requests a permission that the application must be granted in order for it to operate correctly. Permissions are granted by the user when the application is installed, not while it's running. 为了应用操作的正确，需要请求相应的权限。权限在应用安装的时候，而不是运行的时候，需要得到用户的确认。

 - android:name  权限的名字。
    它可以是应用自身使用 <permission> 标签定义的权限，其他应用定义的权限，或者系统提供的标准的权限。系统提供的标准的权限的详细列表可以参考 Manifest.permission 里定义的常量。 

 - android:maxSdkVersion 设置该权限需求被确认的 SDK 的最大版本。
    举个例子，在 Android 4.4 (API level 19) ，WRITE_EXTERNAL_STORAGE 权限以及不是必须的，但是在 API level 18 及以下的版本还是需要申请的，所以你可以把该属性设置成18，这样子，在 API 19以上的设备上，在安装的时候就不会提示这个权限的申请要求了。