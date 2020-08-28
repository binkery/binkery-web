# Python3 reload(sys) 找不到
- Python,reload
- 2018.02.28

在使用 python 的时候，出现了 reload 方法找不到的情况。

## Python reload

在 Python2 时代，我们经常在代码中调用 reload 方法。我们在设置默认的字符编码的时候，经常使用以下代码：

    reload(sys)
    sys.setdefaultencoding("utf-8")

但是，在 Python 3.x 中会提示 name ‘reload’ is not defined

原因是在 3.x 中已经被毙掉了被替换为

    import importlib
    importlib.reload(sys)

sys.setdefaultencoding("utf-8") 这种方式在 3.x 中被彻底遗弃，可以看看 stackoverflow 的这篇文章：<http://stackoverflow.com/questions/3828723/why-should-we-not-use-sys-setdefaultencodingutf-8-in-a-py-script>
