# U盘安装Windows
- 2015-03-06 07:08:24
- 操作系统与开发环境
- windows7,u盘,安装,

<!--markdown-->笔记本要拿回家给老爸老妈用，要重装一下系统。结果找不到之前刻好的系统盘，头疼。重新刻一张吧，结果不知道是盘的问题还是刻录机的问题，就是刻不了。很郁闷。没办法，手头上只有U盘，但是我的那个U盘总是出点问题，之前装Ubuntu的时候，也是这个U盘怎么装就是装不上去，换一个就行。这回也是，高手说要量产啥的，太高了，搞不懂，不想去研究。后来发现一个比较简单的方法，试一下，果然OK，具体原因原理理解不了，咱不是这个专业的。


<!--more-->


主要步骤：

1. 运行CMD命令。
2. 输入：diskpart
3. list disk
4. select disk 编号
5. clean
6. create partition primary
7. select partition 1
8. active
9. format fs=fat32 quick


这样我的那个U盘就可以用了。剩下的就比较简单了，我用的是Windows 7 USB/DVD Download Tool  这个据说是微软官方发布的。使用也很简单，先选ISO文件，然后选择放U盘是DVD盘，然后就是慢慢等待了。一路很顺利。