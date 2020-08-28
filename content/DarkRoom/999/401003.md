# Python 过滤某后缀的文件
- Python,文件过滤
- 2018.04.28

在 Python 中，三种常见的列出某后缀名称的列表的方式。

## 问题

在 Python 中，如何过滤出一个目录下的某后缀名的文件

在 Linux 命令行中， ls | grep ".txt" 就可以实现这样的功能，在 python 中，我们有以下三种方式来实现。

## 1 . 使用 glob

这种方式需要引入 glob 。

    import glob, os
    os.chdir("/mydir")
    for file in glob.glob("*.txt"):
        print(file)
    or simply os.listdir:

## 2 . 普通的方式

这种方式是通过文件名进行字符串判断来过滤后缀。

    import os
    for file in os.listdir("/mydir"):
        if file.endswith(".txt"):
            print(os.path.join("/mydir", file))

## 3 . 使用 walk 的方式

这种方式也是通过文件名进行字符串判断来过滤后缀。

    import os
    for root, dirs, files in os.walk("/mydir"):
        for file in files:
            if file.endswith(".txt"):
                 print(os.path.join(root, file))
