# Kotlin 学习之控制流 
- 2017-05-22 03:16:25
- Kotlin
- kotlin,

<!--markdown--># 控制流

## if 语句
Kotlin 的 if 语句和 Java 大同小异，没有太大的区别，在看官方文档的时候，你可能会感觉差别很大，其实差别大的不是 if 语句，是 Kotlin 的 代码块的 return 值的问题。在 Java 中，每个方法都有一个 return 的类型，如果一个方法不需要 return 类型，那么方法定义的时候，类型是 void，方法最后如果你没有写 return 语句的话，编译的时候会自动帮你加上 return void 。在 Kotlin 中的代码块会自动帮你return 最后一行语句的值或者返回值。

    // Traditional usage 
    var max = a 
    if (a < b) max = b

    // With else 
    var max: Int
    if (a > b) {
        max = a
    } else {
        max = b
    }
     
    // As expression 
    val max = if (a > b) a else b

    val max = if (a > b) {
        print("Choose a")
        a
    } else {
        print("Choose b")
        b
    }

上面的代码适用不同的情况，写起来比 Java 要飘逸多了，但是有个建议，在实际项目开发中，不建议太飘逸，代码一要可阅读性，二要可调试。如果一行代码不能很清晰的表达清楚业务逻辑的时候，是有必要分成多行的，提高可阅读，也方便别人调式。


## when 语法
when 语法是 switch 的升级版，语法飘逸，比如下面比较常规的写法：

    when (x) {
        1 -> print("x == 1")
        2 -> print("x == 2")
        else -> { // Note the block
            print("x is neither 1 nor 2")
        }
    }

在 -> 后面可以跟一个语句，也可以跟一个语句块。还可以这样子写：

    when (x) {
        0, 1 -> print("x == 0 or x == 1")
        else -> print("otherwise")
    }

注意那个逗号 。

每个条件语句只要返回 true 或者 flase 就可以，支持任意的表达式，比如下面的写法：

    when (x) {
        parseInt(s) -> print("s encodes x")
        else -> print("s does not encode x")
    }

in 和 !in 的语法，这个语法就比较类似于 SQL 查询的语法了，用来表示一个跨度。

    when (x) {
        in 1..10 -> print("x is in the range")
        in validNumbers -> print("x is valid")
        !in 10..20 -> print("x is outside the range")
        else -> print("none of the above")
    }

is 和 !is 的语法，类似于 Java 的 instancesOf 关键词了，用来判断类型的。

    val hasPrefix = when(x) {
        is String -> x.startsWith("prefix")
        else -> false
    }

when 的强大在于它基本可以替代 if 语句，比如下面的代码 ：

    when {
        x.isOdd() -> print("x is odd")
        x.isEven() -> print("x is even")
        else -> print("x is funny")
    }


## for 循环
for 循环的基本语法如下：

    for (item in collection) print(item)
    for (item: Int in ints) {
        // ...
    }

for 循环可以遍历任何提供 迭代器的容器。

有一个 iterator() 方法，返回一个迭代器。迭代器的 next() 方法返回一个元素，迭代器的 hasNext() 返回一个 Boolean 类型。只要满足以上条件，就可以用 for 循环遍历。

这个语法和 Java 的 for-each 语法类似，在 Java 中用 for each 比 for( ; ; ) 清爽了很多，但是偶尔要 index 却，要么换回 for( ; ; )，要么遍历前加一个 index 计数，每次 ++。Kotlin 提供了下面的写法，解决了这样的尴尬：

    for (i in array.indices) {
        print(array[i])
    }

    这样的写法，相当于用 index 来遍历容器了。
    再来一个更酸爽的，元素和 index 都有了：

    for ((index, value) in array.withIndex()) {
        println("the element at $index is $value")
    }

## while 循环

while 和 do..while 和 Java 没有的区别 。

## break 和 continue

break 和 continue 同样适用在循环语句中，和 Java 没有区别。