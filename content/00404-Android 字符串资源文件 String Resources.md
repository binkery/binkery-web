# Android 字符串资源文件 String Resources
- 2016-03-22 07:19:46
- Android
- android,字符串,适配,

<!--markdown-->本文主要参考 Android 官方文档，以及平时的一点点心得。更加详细，原汁原味的，烦请移步 Android 官方文档。


<!--more-->


一般在Android 里，会需要你把字符串写在资源文件里。

 - 为了解偶，逻辑代码属于控制层，字符串属于显示层，把两者分开可以降低耦合度。
 - 有利于编译器把你做优化。
 - 有利于做多语言适配。

反正好处多多，我也总结不好，越大型的应用越需要它。

Android 提供三种类型的字符串资源。

 - String 提供一个单独的字符串
 - String Array 提供一个字符串数组
 - Quantity Strings(Plurals) 为不同的数量提供不同的字符串适配

## String

一个单独的字符串，定义在xml文件里，可以供 layout xml 引用，也可以供 Java 读取。一般默认的，在 res/values/strings.xml 里可以定义 \<string name="helloworld"\>Hello World\</string\>。下面是一个完整的 xml 内容。

    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <string name="string_name">text_string</string>
    </resources>

其中的 name 对应的就是 key，每个字符串都需要有一个单独的 key 。必须单独的，如果有重复的，编译器可能不会报错，但是运行的时候，可能会读不到你想要的内容。这个就不用深入解释了，理所应当的，key 必须唯一，没啥好商量的。但是 xml 文件可以有多个。很多人喜欢把所以的字符串都放在 strings.xml 里。这是开发工具默认帮你生成的。但是随着项目的持续开发，项目越来越大的时候，我还是建议可以分成多个文件的。这样有利于代码的阅读，而且不会影响运行的效率，多出来的工作在编译的时候已经做好了。

使用方法：
在layout xml 里使用，例如 

    <TextView android:text="@string/helloworld"/> 

或者在 Java code 里使用 

      String string = getString(R.string.helloworld);

getString(int) 和 getText(int) 都可以返回字符串内容，不同的是 getText(int) 可以返回富文本（rich text）字符串。富文本就是加粗啊，斜体啊之类的简单的样式，下面会说。

## String Array 
字符串数组，可以定义在 strings.xml 里，也可以定义在其他的 xml 里。

    <string-array name="string_array_name">
        <item>text_string</item>
    </string-array>

一个 string-array 里可以有 N 多个 item。同样，name 也必须唯一。item 可以是一个字符串，也可以是另外一个字符串的引用。使用： 

    Resources res = getResources();
    String[] strings = res.getStringArray(R.array.string_array_name);

这样就得到了一个字符串数组了。

## Quantity Strings(Plurals)

带数量的字符串。在很多语言里，不同的数量的文字的表达方式有些不同。比如在英文里，一本书表示为 one book . 两本书表示为 two books 。在单词上，或者在语法上，就有很多的不一样的地方，这样一个字符串就可能搞不定了。
这个时候 Quantity Strings  就可以帮你搞定这个问题。
语法是这样子的：

    <resources>
        <plurals name="plural_name">
            <item quantity=["zero" | "one" | "two" | "few" | "many" | "other"] >text_string</item>
        </plurals>
    </resources>

 - name 也就是 ID，唯一，不废话
 - item 可以有多个，每个 item 都有 quantity 属性，每个 item 的 quantity 属性不能一样。
 - zero 表示没有；one 表示一个，单数；two 表示两个，或者一对，一双；few：表示很少；many：表示挺多的；other：表示其他。

使用：

    int count = getNumberOfsongsAvailable();
    Resources res = getResources();
    String songsFound = res.getQuantityString(R.plurals.numberOfSongsAvailable, count, count);

## 格式化和样式

1. 转义。对一些特殊字符，需要做转义处理。比如单引号等。
2. 格式化，在一个字符串里，可以包含一些不确定的内容。这些不确定的内容会在运行的时候被填写。

你可以在定义这么一个字符串：

    <string name="welcome_messages">Hello, %1$s! You have %2$d new messages.</string>

在运行的时候去填充对应的内容。
  

    Resources res = getResources();
    String text = String.format(res.getString(R.string.welcome_messages), username, mailCount);

String.format(String,Object...) 是一个很强大字符串格式化的 API 。

3. 富文本样式
你可以这样定义：

    <string name="welcome">Welcome to <b>Android</b>!</string> 

然后调用 Html.fromHtml(text) 输出一个 CharSequence 对象。这样在一个 TextView 里，可以有不同样式的字符串。
Android 支持简单的样式。\<b\> 粗体，\<i\> 斜体，\<u\> 下划线。