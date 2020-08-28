# Python 文件大小格式化输出
- Python,格式化,文件大小格式
- 2018.04.29

在 Python 中，格式化文件大小的方法

## 问题

在 Python 如何格式化输出一个文件的大小

在项目中，直接打印文件的大小总是让人感觉那么的不友好，特别是一些比较大的文件，一大串数字看起来非常费劲。那么我们就需要打印一个人类可读的文件大小格式。封装一个格式化文件大小的方法是非常有必要的。

    def format_file_size(filesize) :
        for count in ['Bytes','KB','MB','GB']:
            if fileSize > -1024.0 and fileSize < 1024.0:
                return "%3.1f%s" % (fileSize, count)
            fileSize /= 1024.0
        return "%3.1f%s" % (fileSize, 'TB')

这个方法可以支持大部分需求了。
