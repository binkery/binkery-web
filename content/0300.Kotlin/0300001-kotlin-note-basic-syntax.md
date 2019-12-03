# kotlin 自学笔记 - 基本语法
- kotlin,学习笔记,自学笔记,基本语法,kotlin学习笔记,kotlin基本语法
- 2019.04.30

## 定义包 Defining packages

    package my.demo
  
    import java.util.*

和 Java 一样，包的定义一般放在源文件的最上头。和 Java 不一样的是，Kotlin 不要求包名和文件名一致。当然这样并不是很好。

## 定义函数 Defining functions

    fun sum(a: Int, b: Int): Int{
        return a + b
    }
    fun sum(a: Int, b: Int) = a + b

 第一个方法定义了方法名字，参数列表，两个 Int ，返回类型是 Int ，以及方法体。第二个方法省略了返回类型，并且简化了方法体。一定程度上简化了代码，提高可阅读性。
 
 不需要返回类型的情况，同样的，可以明确声明这个方法返回类型，也可以通过推断来确定返回类型。第一种是推荐的。
 

    fun printSum(a: Int, b: Int) : Unit{
        println("$a + $b = ${a + b}")
    }
    
    fun printSum(a: Int, b: Int){
        println("$a + $b = ${a + b}")
    }

    
## 定义变量 Defining variables

**val** 用来定义不变量。也就是 val 只能被赋值一次，和 Java 的 final 修饰一样的作用。


    val a: Int = 1 // 明确的数据类型，立即赋值
    val b = 2  // 立即赋值，并且推断数据类型
    val c:Int  // 明确的数据类型，但是没有明确赋值
    c = 3 
    
**var** 用来定义可变量。

    var x = 5
    x += 1

## 注释 Comments

有两种注释方式，单行注释和多行注释。官方说法是 end-of-line 和 block comments ，行尾注释和注释块。

    // 单行注释
    /** 多行
    注释 */
    
和 Java 不一样，注释块可以嵌套。这个暂时不明白什么意思。

## 字符串模板 Using string templates

这个比较强大，可以字符串中使用美元符**$**来使用变量，并且做一些简单的运算。

    var a = 1
    val s1 = "a is $a"
    val s2 = "${sl.replace("is","was"), but now is $a}"

## 使用条件表达式 conditional expressions

    fun maxOf(a: Int,b: Int):Int{
        if(a > b ){
            return a
        }else{
            return b
        }
    }


可以简化为：

    fun maxOf(a:Int,b:Int) = if(a>b) a else b

## 使用可为空的值和空检查 using nullable values and checking for null

一个引用，如果可能是 null 的话，必须明确标识它是可为空的。

    fun parseInt(str:String):Int? {
        //...
    }

这个方法的问号 **?** 表示这个方法可以返回 null。所以，判断这个方法的返回值是否为空是必要的。

## 类型检测和自动转化 using type checks and automatic casts

kotlin 用 **is** 代替了 Java 中的 **instanceof** ，效果是一样的。比 Java 优化的是，增加了自动类型转换。在 Java 中需要强转换，一般 IDE 会帮助你生成代码，而在 Kotlin 中，直接就省了。

    if(obj is String && obj.length > 0){
        // ...
    }

## 循环 Using a for loop

两种常见的循环

    val items = listOf("apple","banana","kiwifruit")
    for(item in items){
        // 和 Java 的 for each 语法一样
    }
    for(index in items.indices){
        // 增加了索引，解决了 Java for each 没有索引的痛点
    }

## while 循环

    while (index < items.size){
    index++
    }

while 循环没有什么特殊的，和 Java 一样。

## when 表达式

when 表达式是一个 kotlin 比 Java 优秀的特色。感受一下：

    fun describe(obj : Any):String = 
        when(obj){
            1 -> "One"
            "hello" -> "Greeting"
            is Long -> "Long"
            !is String -> "Not a String"
            else -> "unknown"
        }

强大归强大，问题还是有，代码飘逸的话，脑袋的运行速度要跟上。

## Using ranges
经常和 **in** 关键字一起使用

    val x = 10
    val y = 9
    if(x in 1..y+1){
        // x 在 1 到 y+1 区间内
    }
    val list = listOf("a","b","c")
    if (-1 !in 0..list.lastIndex){
        // -1 不在 0 到 list.lastIndex 区间内
    }
    if(list.size !in list.indices){
        // list.size 不在 list 的索引组里
    }


for 循环遍历也经常会用到，还有 **step**，**downTo** ，是不是很爽。

    for(x in 1..6){
        print(x)
    }
    for (x in 1..10 step 2){
    }
    for(x in 9 downTo 0 step 3){
    }

## 集合
迭代一个集合，for in 是最简单常见的方法。

    for(item in items){
    }

**in** 也可以用来判断一个对象是否在一个集合里。

    when{
        "orange" in items -> println("juicy")
        "apple" in items -> pringln("apple is fine too")
    }

## Using lambda expressions to filter and map collections:


    val fruits = listOf("banana", "avocado", "apple", "kiwifruit")
    fruits
        .filter { it.startsWith("a") }
        .sortedBy { it }
        .map { it.toUpperCase() }
        .forEach { println(it) }


## 实例化对象
不再需要 **new** 这个关键词了。

    val rectangle = Rectangle(5.0,2.0)



