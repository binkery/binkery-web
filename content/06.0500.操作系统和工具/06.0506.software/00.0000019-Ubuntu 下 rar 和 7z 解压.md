# Ubuntu 下 rar 和 7z 解压
- Ubuntu,zip,rar,Ubuntu Rar,Ubuntn 7z,Ubuntu解压,
- 2015-03-06 04:00:33


rar 和 7zip 是两种常见压缩文件格式。在 windows 上，咱们用 RAR 可以很好的解决解压问题，但是在 Ubuntu 系统下，默认是没有这两种文件格式的解压支持的，需要自己另行安装。


## rar 安装

    sudo apt-get install rar

解压命令行：

    rar e xxx.rar
    rar x xxx.rar 

压缩命令行 ： 

    rar a xxx.rar file1 file2 ...

## 7zip安装：

    sudo apt-get install p7zip

7zip解压命令行：

    7zr x xxx.7z    // 解压到XXX

    7zr e xxx.7z    // 解压到当前文件夹

