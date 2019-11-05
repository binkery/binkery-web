# kotlin 学习之 Kotlin 基本类型 Basic Types
- 2017-05-28 12:27:39
- Kotlin
- 学习,kotlin,基础知识,

<!--markdown--># Basic Types

在 Java 中，有 8 中基础数据类型，分别为 int,short,byte,long,float,double,char,boolean 。除了这 8 种外，其他的都是引用类型，包括 String。而在 Kotlin 种，所有的都是引用类型，没有基础数据类型这一个说法了，不过有这么几种类型是平时开发中离不开的，称为 Basic Types，他们本质上和其他类没有区别。

## 数字类型(Numbers)

Kotlin 中有六种数字类型。

    Double 64 位
    Float 32 位
    Long 64位
    Int 32 位
    Short 16 位
    Byte 8 位。

注意都是大写的，没有 Java 的小写的基础数据类型。在 Java 中，小写的较基本数据类型或者基本数据类型，有 8 个，每个都有其对应的封装类型，Kotlin 中没有这个概念，直接都是封装类型了，比 Java 面向对象更彻底。

另外，在 Kotlin 中，字符（characters）不算数字类型，在 Java 中 char 被算入数字类型的整数类型中。

### 数字的表达
#### 整数类型：

* 十进制 Decimals  ： 123
* 十六进制 Hexadecimals ：0x0F
* 二进制 Binaries ： 0b01010101

注意：Kotlin 不支持八进制

#### 浮点类型：

和 Java 一样，默认的是 Double 类型，比如 123.5。Float 类型需要加 F 或者 f ，比如 123.5f。

#### 数字之间的下划线

为了增加数字的可读性，Kotlin 1.1 增加了数字之间的下划线。比如 1_000_100 等于 1000000。整数类型的十进制、十六进制、二进制表达方式都支持这样的写法。

### 比较两个数字
Kotlin 中没有基础数据类型，只有封装的数字类型，你每定义的一个变量，其实 Kotlin 帮你封装了一个对象，这样可以保证不会出现空指针。数字类型也一样，所有在比较两个数字的时候，就有比较数据大小和比较两个对象是否相同的区别了。

在 Kotlin 中，三个等号 === 表示比较对象地址，两个 == 表示比较两个值大小。

    val a: Int = 10000
    print(a === a) // Prints 'true'
    val boxedA: Int? = a
    val anotherBoxedA: Int? = a
    print(boxedA === anotherBoxedA) // !!!Prints 'false'!!!
    print(boxedA == anotherBoxedA) // Prints 'true'

不同类型比较，比如一个 Int 和一个 Long 比较（两个等号 == 的比较），那么返回的是 false，因为调用 equals() 方法的时候，会判断两个对象是否是同一个类型，这个和 Java 一致。在 Java 中，基础数据类型的 == 比较的是两个值的大小，并没有 equals() 方法什么事，即使两个基础数据类型的封装对象的 == 比较，也会自动装箱和拆箱，你一定要记住 Kotlin 中没有基础数据类型，比 Java 更彻底的面向对象，你就能理解这里的 == 为什么会 false 了。

小的数字类型不支持直接转换成大一些的数字类型，比如 Byte 不能直接赋值给一个 Int，

    val b: Byte = 1 // OK, literals are checked statically
    val i: Int = b // ERROR
    val i: Int = b.toInt() // OK: explicitly widened

每个数字类型都封装了一些 toXxx() 的方法。

和 Java 一样，两个不同的数字类型运算，结果的数据类型是最大的那个。

    val l = 1L + 3 // Long + Int => Long

### 位移运算

做为一个中国人，表示 Kotlin 的位运算很不酸爽啊，为了更接近自然语言，竟然放弃了那么形象的位移符号。先哭会～～

    shl(bits) – signed shift left (Java's <<)
    shr(bits) – signed shift right (Java's >>)
    ushr(bits) – unsigned shift right (Java's >>>)
    and(bits) – bitwise and
    or(bits) – bitwise or
    xor(bits) – bitwise xor
    inv() – bitwise inversion


## 字符类型 Char
和 Java 不一样，Kotlin 中的 Char 不能直接和数字操作，Char 必需是单引号''包含起来的。比如普通字符 '0'，'a'，比如转移字符：'\t'，'\n'，比如 Unicode ：'\uFF00'。
在 Java 中，char 属于数字类型中的整数类型，所有可以这样使用 char a = 1 ,但是在 Kotlin 中，Char 彻底和数字类型划清了界限。

## 布尔类型 Boolean

只有 ture 和 false 两个值，基本和 Java 一致。运算符有 || ，&&，！

## 数组 Array

在 Kotlin 中，数组是 Array 类，有 get 和 set 方法，还有 size 属性，表示长度。
arrayOf() 方法可以返回一个数组，arrayOf(1,2,3) 会创建一个数组 array[1,2,3]。
arrayOfNulls() 方法可以返回一个指定长度的、元素为空的数组。
在创建数组的时候，除了制定数组的长度外，还可以使用方法来初始化数组元素。比如：

    // Creates an Array<String> with values ["0", "1", "4", "9", "16"]
    val asc = Array(5, { i -> (i * i).toString() })

方括号 [] 操作符可以实现和 get() 、set() 一样的操作。

和 Java 不一样，数组在 Kotlin 是不变的，不能把一个 Array<String> 赋值给 Array<Any> ，直接操作会导致数据类型异常。

Kotlin 还提供了 ByteArray,ShortArray,IntArray ，但他们和 Array 没有任何的继承关系，只是有相同的 API 设计而已。

## 字符串类型 String

和 Java 一样，String 是可不变的。方括号 [] 语法可以很方便的获取字符串中的某个字符，也可以通过 for 循环来遍历：

    for (c in str) {
        println(c)
    }

Kotlin 支持三个引号 """ 扩起来的字符串，支持多行字符串，比如：
    
    val text = """
        for (c in "foo")
            print(c)
    """

String 可以通过 trimMargin() 方法来删除多余的空白。

### String 模板
Kotlin 的 String 支持模板，语法类似：

    val s = "abc"
    val str = "$s.length is ${s.length}" // evaluates to "abc.length is 3"

这个很像脚本语言，比 Java 中用 format 方法来格式化字符串要简化了很多。