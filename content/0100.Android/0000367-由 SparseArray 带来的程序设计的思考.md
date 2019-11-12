# 由 SparseArray 带来的程序设计的思考
- Android,程序设计,sparsearray,
- 2014-12-16 09:59:13


我之前有一篇关于SparseArray的博客（Android SparseArray 系列 http://www.binkery.com/archives/351.html），但是发现很多项目里，这个特殊的工具类没有被很好的使用。


1. SparseArray 设计得很棒

2. SparseArray 以时间换空间

3. 用不好 SparseArray 的话，还不如直接用数组。

4. 这点利润值得吗？如果说你想定义一个 int 数组，每个 int 占用4个字节，如果数组长度为1024，那么占用内存为 4k byte，很大吗？如果使用 SparseArray，哪怕它一个字节都不占，你也就是省下4k字节的内容。在一个 Android App 里，你会用到多长的数组？多少这样长度的数组？在一个项目里，你使用SparseArray来替换数组带来的效益貌似不是很可观。

5. 风险貌似也不小。本来你想定义一个长度为1024 的int数组，发现别人都在使用SparseArray，于是你也用SparseArray替换掉了数组，但是你的初始化的时候，用一个 for 循环，给 SparseArray put 了1024个 int 值，而且都是 0，你知道你在做什么吗？好吧，我相信，在现在的CPU能力下，多出来的这些运算量也是小case了。

所以，在项目里，不管你是直接用数组，还是用 SparseArray，SparseArray用对了，还是用错了，基本上肉眼你是看不出差距来的。这也导致了很多人没有仔细去研究 SparseArray 。

但是不管怎么着，SparseArray 的源码相当的漂亮，有时间有兴趣，很值得研究，能学很多东西。

另外一个想法，就像前些天在CSDN上看到的，没有完美的设计，只有合理的设计。满足当前需要就好，像初级程序员一样，使用数组来完成这项工作又怎样？这个项目有复杂到需要你去扣这点内存吗？