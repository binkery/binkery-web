# Kotlin 学习之包 Package
- 2017-07-23 07:26:13
- Kotlin
- kotlin,包,import,package,

<!--markdown--># 包
## package

和 Java 一样，每个代码文件的开头都可以包含一个 package 声明，注意，是可以，也就是说也可以没有，Java 也是可以没有的。

在 Kotlin 中，package 的路径和该类所在的真实路径可以是不一致的。这个和 Java 不一样，Java 在这方面是强约束。个人建议还是尽量让他们保持一致，Kotlin 这样的设计应该是有他的道理的，但是我还是觉得这样的飘逸不够严谨，写的人可能很爽，看的人会很头疼，而且有时候，看的人和写的人是同一个人，只是中间隔着若干时间，这时候看代码的人，喷也不是，不喷也不是。


和 Java 不同的是，代码文件里可以直接定义方法，而 Java 方法肯定是在类里面的。 比如代码：

    package foo.bar
    fun baz() {}
    class Goo {}

直接在包上定义方法也是 kotlin 的一个特别的地方，所以，上面的 baz() 方法，调用的全路径是 foo.bar.baz。Goo 类的全路径是 foo.bar.Goo

## 默认的 import。

Java 文件默认都 import java.lang 了，Kotlin 也默认 import 了很多包了。

## import
Kotlin import 语法如下：
    import foo.Bar // Bar is now accessible without qualification
    import foo.* // everything in 'foo' becomes accessible
    import bar.Bar as bBar // bBar stands for 'bar.Bar'

和 Java 不一样，Kotlin 不支持 import static 语法。

另外，Kotlin 的 import 多了 as 语法，这个在当需要 import 两个不同包但是相同类名的时候，就比较实用了，在 Java 中，碰到这种情况，咱们只能使用类的全称。Kotlin 中的 as 就可以简化这样的代码，可以更加简洁了。