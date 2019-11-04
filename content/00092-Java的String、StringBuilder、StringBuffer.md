# Java的String、StringBuilder、StringBuffer
- 2015-03-06 08:09:43
- Java
- java,string,stringbuffer,stringbuilder,

<!--markdown-->String是Java里很重要的一个类型，但是它不是基础数据类型。基础数据类型只有八个。这里不多说。


<!--more-->


String的几个重要的API，是会经常用到的。

对字符串操作的相关动作，这个类基本都已经实现了。比如找目标字符串是否存在及其出现的位置，字符串的切割，按要求截取字符串获得子串。

有一个 matches() 方法，是可以配合正则表达式来判断一个字符串的。这个方法在用户名密码的本地验证的时候可能会用到。这是个很不错的方法，虽然用的次数比较少。

还有字符串和 byte 数组的转换关系，这个也经常会用到，主要在跟字节流或者其他流结合使用的时候会用到。

length() 获取String的长度，返回一个int值。面试笔试经常会考到这个，区别于数组，数组获取长度是length属性。

最最常用的应该是 equals() 了，String 的比较是不能用 == 来比较的，这个切记切记。

## StringBuilder 和 StringBuffer

StringBuilder 和 StringBuffer 是为了优化 String 而产生的。因为 String 是字符串常量，在JAVA里，String对象是被放在一个对象池里的，当有大量的String的拼接的时候，会产生一些垃圾，而这些垃圾并不一定能够及时回收。StringBuilder和StringBuffer就这样产生了，为了解决这个问题。两个类的API应该是基本一样的，主要的就一个方法append（）。注意append（）返回的类型，在很多地方，很多人喜欢这样写代码：

sb.append().append().append(); 最后在 sb.toString();来获取String对象。

## StringBuilder 和 StringBuffer 区别

StringBuilder 和 StringBuffer 最大的区别在于StringBuffer是线程安全的，在查看源代码的时候，你可以发现StringBuffer比StringBuilder多了一个同步而已。StringBuffer的append方法前多了一个synchronized修饰符。不过看一下API，并不是所有的方法都加了这个修饰符，在append基础数据类型的时候是没有加synchronized的。大概猜想一下，无非是运行时间很短，不需要加同步而已。这里不多研究，主要记住线程安全是两个最大的区别。

这三个类是经常会用到的，其实都不难，需要一段时间熟练一下就好了，还要勤看API。