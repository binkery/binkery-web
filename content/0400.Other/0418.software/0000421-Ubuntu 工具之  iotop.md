# Ubuntu 工具之  iotop
- Ubuntu,iotop,Ubuntu磁盘参看
- 2016-03-22 07:49:35


iotop 是专门用来显示硬盘 IO 的命令，对每个进程进行单独的跟踪和分析，这样就可以找出疯狂读写你的硬盘的进程了。


安装：

    sudo apt-get install iotop

快捷键：
安装后，直接在命令行里运行 iotop 就可以了。界面和 top 命令相似，可以使用左右键切换排序的列，默认是 IO ， r 键是置换排序，显示 > 表示从大到小，显示 < 表示从小到大。一般就是从大到小，从小到大应该很少使用。o 是显示只有 IO 的进程，那些一直没有 IO 操作的就不会列在上面了。q 是退出，任意键是强制刷新。

参数：

    --version             查看版本
    -h, --help            查看帮助
    -o, --only            只显示有 IO 操作的进程或线程
    -b, --batch           没有交互的模式，可以当成日志直接输出到文件记录用。
    -n NUM, --iter=NUM    循环次数，在刷新了指定的次数后，程序就退出
    -d SEC, --delay=SEC   刷新的频率，默认 1 秒一次
    -p PID, --pid=PID     监视单个进程，默认监视所有。要监视多个，可以加多个 -p PID 
    -u USER, --user=USER  监视单个用户，默认监视所有。
    -P, --processes       只显示进程，不显示线程。
    -a, --accumulated     在 Disk Read 和 Disk Write 列显示的是从 iotop 启动开始，累计的数据量。
    -k, --kilobytes       使用 KB 为单位。
    -t, --time            在每一行加上时间戳
    -q, --quiet           退出
