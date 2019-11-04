# Ubuntu环境变量配置
- 2016-03-31 07:38:21
- 操作系统与开发环境
- ubuntu,环境变量,

<!--markdown-->经常需要配置环境变量，但是每次都忘了具体配置的文件名，还得Google，百度一下。
主要三个方法比较常用。

1. 修改主目录下的 .bashrc 文件。


    export PATH="$PATH:/your-path"

编辑后保存，然后在命令行输入

    source .bashrc

这种方式影响的是当前这个用户，因为这个环境变量的信息是保存在当前这个用户的 .bashrc 文件中的，只有在这个用户登录的时候，这个文件才会被执行。

2. 修改/etc/profile


    PATH="$PATH:/your-path"
    export PATH

编辑后保存，然后需要在命令行输入 

    source /etc/profile

这种方式修改的是 /etc/profile ，所有在这台机器上登录的用户都会受到影响。

3. 直接在终端 


    export PATH="$PATH:/your-path"

前面两种最好Log out 一下再进来。第三种一般只在当前终端有效。
