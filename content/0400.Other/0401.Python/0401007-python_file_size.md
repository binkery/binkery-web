# Python 获取文件大小的方法
- Python,FileSize,文件大小
- 2018.05.02

Python 获取文件大小的方法。

## 问题

在 Python 中，如果获取一个文件的大小

有以下几种方式获取文件的大小。

## os.stat

使用 os.stat() 获得一个 stat 对象，然后通过 st_size 属性获得文件大小。

    import os
    statinfo = os.stat('somefile.txt')
    statinfo.st_size

## os.path.getsize

使用 os.path.getsize 的方式

    import os
    b = os.path.getsize("/path/file.mp3")
