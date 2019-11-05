# Android ADB package manager pm
- 2016-03-22 07:25:39
- Android
- android,adb,

<!--markdown-->adb 提供 pm 命令，可以对 package 进行管理。你可以在 adb shell 到设备上，然后输入 pm \<command\> 进行操作，也可以直接在你本地的命令行里输入 adb shell pm \<command\> 操作。


<!--more-->


 - list package [options] \<FILTER\>
    打印所有的 packages , 可以通过文本进行过滤
    - -f 查看关联的文件 apk 文件
    - -d 只显示不可用的 packages ,就是被你禁止的应用
    - -e 只显示可用的 packages
    - -s 只显示系统的 packages
    - -3 只显示第三方的 packages
    - -i 显示 installer 的 packages ,在某些设备上，可能不给显示
    - -u 显示包含未安装的 packages
    - --user <USER_ID> 

 - list permission-groups
    打印所有已知的权限集合 permission groups

 - list permission [options] \<GROUP\>
    打印所有已知的权限。
    - -g 按 group 组织输出
    - -f 打印所以信息，比较详细
    - -s 打印简短的信息
    - -d 只打印危险的权限
    - -u 只显示跟用户有关的权限

 - list instrumentation
    打印所有测试的 package

 - list features
    打印系统的所有 features

 - list libraries
    打印当前设备支持的库 libraries

 - list users
    打印系统上的所有用户

 - path \<PACKAGE\> 
    打印出给定的 package 的 APK 路径
    
 - install [options] \<PATH\>
    安装 package ,
    - -l install the package with forward lock
    - -r 如果已经存在，重新安装，保留上一个 package 的数据
    - -t 允许测试的 APK 被安装
    - -i <INSTALLER_PACKAGE_NAME> 指定安装器
    - -s 安装到共享的存储空间，比如 sdcard 上
    - -f 安装到系统内部存储上
    - -d 允许安装低版本的，一般安装会校验应用的版本，高版本的覆盖低版本的，特殊的时候需要低版本覆盖高版本，就需要这个选项。

 - uninstall [options] \<PACKAGE\>
    卸载 package
    - -k 卸载，但是保留数据和缓存

 - clear \<PACKAGE\>
    清除指定 package 下的数据文件。

 - enable \<PACKAGE_OR_COMPONENT\> 
    启用 package 或者组件，组件的需要指定包名和类名 package/class

 - disable \<PACKAGE_OR_COMPNENT\>
    禁用 package 或者组件，组件使用包名+类名
 
 - disable-user [options] \<PACKAGE_OR_COMPONENT\>
    --user <USER_ID> 对某个用户禁用某个包或者组件

 - grant \<PACKAGE_PERMISSION\>
    给应用授权，前提是应用声明了该权限

 - revoke \<PACKAGE_PERMISSION\>
    取消权限，取消应用声明的权限。

 - set-install-location \<LOCATION\>
    设置安装的目录，LOCATION 的值有：
    - 0 自动
    - 1 内部
    - 2 外部
    这个只适用于 debug ， 因为这个命令可能会造成应用被破坏或者其他不可预知的问题。
 
 - get-install-location
    获取默认的安装目录，跟设置一样，0 表示自动，1 表示内部，2 表示外部

 - set-permission-enforced \<PERMISSION\> [true|false]
    指定给定的权限是否是强制的。

 - trim-caches \<DESIRED_FREE_SPACE\>
    裁剪缓存文件的大小到指定的额度。

 - create-user \<USER_NAME\>
    创建一个指定名字的用户，打印出新创建的用户的 ID

 - remove-user \<USER_ID\>
    删除指定ID 的用户，并且会删除这个用户相关的数据。

 - get-max-users
    打印设备支持的最大的用户数量


