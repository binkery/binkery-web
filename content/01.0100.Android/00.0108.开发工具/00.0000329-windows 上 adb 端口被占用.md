# windows 上 adb 端口被占用
- android,adb,windows,端口,
- 2014-08-02 03:50:45


在windows 上安装了 Android SDK， 但是ADB 连接或者打LOG的时候，经常碰见

    adb server is out of date.  killing...
    ADB server didn't ACK
    * failed to start daemon * 


原因是ADB的端口被占用，一般想豌豆荚，QQ，其他一些电脑管家，安全软件，都可能会去监听是否有Android 设备连接到电脑上，所以他们会占用相应的端口。

命令行输入 netstat -ano | findstr "5037" 找出监听5037端口的 PID ，然后 tasklist | findstr "PID number" 找出是哪个程序，把它kill掉。

为了抢占用户，不惜一切代价强弓虽女干用户。
