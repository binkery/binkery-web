# Kotlin 基本语法 basic syntax
- 2017-05-22 10:02:19
- Kotlin
- Kotlin,基本语法,


## 定义包 Defining packages

和 Java 类似，包的定义一般在一个代码文件开始的地方，代码如下

    package my.demo
    import java.util.*

Kotlin 不要求定义的包的目录和代码文件实际的物理位置匹配，个人感觉有点坑，不建议这样做。

## 定义方法 Defining functions

下面的例子是定义两个 Int 值相加的方法，

    fun sum(a: Int, b: Int): Int {
        return a + b
    }

fun 是定义方法的关键词，sum 是方法名，参数列表是两个 Int ,返回类型也是 Int。方法体是 return a + b。下面是其简写的代码：

    fun sum(a: Int, b: Int) = a + b

返回类型被省略了，方法体也简写成一个表达式了。 

如果一个方法不需要返回任何内容，可以这样写：

    fun printSum(a: Int, b: Int): Unit {
        println("sum of $a and $b is ${a + b}")
    }

Unit 类似 Java 中的 void 。其中 Unit 还可以被省略：

    fun printSum(a: Int, b: Int) {
        println("sum of $a and $b is ${a + b}")
    }

看见神坑了吧，个人觉得，不管 Kotlin 怎么支持，方法都需要写返回类型。方法名，参数列表，返回类型就相当于这个方法的说明文件一样，应该让阅读者看到这些内容就知道这个方法是干什么用的，应该怎么调用，会返回什么样的结果。所有不建议省略返回类型。

## 定义变量

定义变量的关键词有两个 val 和 var。val 是定义的是只读的，表示不变量，var 表示可变量。

    val a: Int = 1  // immediate assignment
    val b = 2   // `Int` type is inferred
    val c: Int  // Type required when no initializer is provided
    c = 3       // deferred assignment
    var x = 5 // `Int` type is inferred
    x += 1

## 注释

和大多数语言一样，Kotlin 有单行注释和多行注释，两个斜杠 // 表示单行注释，/* */ 表示的是多行注释。

    // This is an end-of-line comment

    /* This is a block comment
       on multiple lines. */

## 字符串模板 Using string templates

Kotlin 的字符串模板（string templates）更加方便了字符串的格式化，这种语法在很多语言中都支持，但是 Java 一直没有很友好的支持。

    var a = 1
    // simple name in template:
    val s1 = "a is $a" 

    a = 2
    // arbitrary expression in template:
    val s2 = "${s1.replace("is", "was")}, but now is $a"

## 条件表达式 conditional expressions

条件表达式可以让代码更加的简略，写起来很飘逸，但是阅读上有点麻烦，需要一定的熟悉过程。

    fun maxOf(a: Int, b: Int): Int {
        if (a > b) {
            return a
        } else {
            return b
        }
    }

可以写成下面的样子，一行就搞定了：

    fun maxOf(a: Int, b: Int) = if (a > b) a else b

## 空值和空检查  using nullable values and checking for null

Kotlin 的一个特点就是安全，没有空指针异常，在 Kotlin 中所有的引用都是有空值保护的。一个引用需要明确的显示的（explicitly）标记为可空（nullable）的，这个引用才可能会是 null。

    fun parseInt(str: String): Int? {
        // ...
    }

和普通方法的定义不同的是，返回类型后面加了一个问好 ? 。使用如下

    fun printProduct(arg1: String, arg2: String) {
        val x = parseInt(arg1)
        val y = parseInt(arg2)
    
        // Using `x * y` yields error because they may hold nulls.
        if (x != null && y != null) {
            // x and y are automatically cast to non-nullable after null check
            println(x * y)
        }
        else {
            println("either '$arg1' or '$arg2' is not a number")
        }    
    }

或者

    // ...
    if (x == null) {
        println("Wrong number format in arg1: '${arg1}'")
        return
    }
    if (y == null) {
        println("Wrong number format in arg2: '${arg2}'")
        return
    }
    
    // x and y are automatically cast to non-nullable after null check
    println(x * y)

## 类型检测和自动转换

类型检测（type checks）和自动转换（automatic casts）

is 关键词和 Java 中的 instanceOf 一样，用来类型检测。

    fun getStringLength(obj: Any): Int? {
        if (obj is String) {
            // `obj` is automatically cast to `String` in this branch
            return obj.length
        }
    
        // `obj` is still of type `Any` outside of the type-checked branch
        return null
    }

或者

    fun getStringLength(obj: Any): Int? {
        if (obj !is String) return null
    
        // `obj` is automatically cast to `String` in this branch
        return obj.length
    }

或者

    fun getStringLength(obj: Any): Int? {
        // `obj` is automatically cast to `String` on the right-hand side of `&&`
        if (obj is String && obj.length > 0) {
            return obj.length
        }
    
        return null
    }


注意上面 is 语句后面 obj 的类型自动转换为 String 类了。在 Java 中，需要做强制的类型转换，在 Kotlin 中都可以省略了。

## for 循环

    val items = listOf("apple", "banana", "kiwi")
    for (item in items) {
        println(item)
        // 和 Java 的 for each 语法一样
    }

或者

    val items = listOf("apple", "banana", "kiwi")
    for (index in items.indices) {
        println("item at $index is ${items[index]}")
        // 增加了索引，解决了 Java for each 没有索引的痛点
    }
    

## while 循环

    val items = listOf("apple", "banana", "kiwi")
    var index = 0
    while (index < items.size) {
        println("item at $index is ${items[index]}")
        index++
    }


## when 表达式

when 表达式在 Java 中没有，比 Java switch case 的要强大很多。

    fun describe(obj: Any): String =
    when (obj) {
        1          -> "One"
        "Hello"    -> "Greeting"
        is Long    -> "Long"
        !is String -> "Not a string"
        else       -> "Unknown"
    }

## in 关键词

in 关键词用来表达一个跨度。在 if 语句中，用来判断关键词 in 前的值是否在 in 后的范围内，比如：

    val x = 10
    val y = 9
    if (x in 1..y+1) {
        println("fits in range")
    }
    
    val list = listOf("a", "b", "c")
    if (-1 !in 0..list.lastIndex) {
        println("-1 is out of range")
    }
    if (list.size !in list.indices) {
        println("list size is out of valid list indices range too")
    }

in 也可用用来遍历，遍历中，还增加了 step 和 downTo

    for (x in 1..5) {
        print(x)
    }
    for (x in 1..10 step 2) {
        print(x)
    }
    for (x in 9 downTo 0 step 3) {
        print(x)
    }

## 集合

遍历一个集合

    for (item in items) {
        println(item)
    }

使用 in 关键词检查一个元素是否在某个集合里，

    when {
        "orange" in items -> println("juicy")
        "apple" in items -> println("apple is fine too")
    }

用 lambda 表达式来过滤容器

    fruits
    .filter { it.startsWith("a") }
    .sortedBy { it }
    .map { it.toUpperCase() }
    .forEach { println(it) }
