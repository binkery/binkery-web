# Kotlin 学习之空安全 Null Safety
- 2017-05-23 10:22:55
- Kotlin
- Kotlin
- Kotlin空保护,Kotlin空指针,Kotlin空安全

在写 Java 代码的时候，空指针是一直让人头疼的问题，为此我们可以通过采用 **注解** 的方式，来协助开发者避免空指针的产生，而 Kotlin 直接设计到语法中。

比如我们在定义变量的时候，Kotlin 就要求开发者在定义变量的时候，考虑这个变量是否可能为空，定义方法的返回类型的时候，也需要同时考虑返回值是否可能为空。在使用变量的时候，如果变量被明确定义不会为空，那么开发者可以放心地使用变量，而如果变量可空的话，Kotlin 要求开发者要做好空的判断，以及空的情况下的处理逻辑。

通过整个 Kotlin 语法的设计，就可以保证代码在运行的过程中，不会意外的产生空指针，即使产生空指针异常，也是按照开发者的显示要求抛出的异常。

## 可为空的类型和不可为空的类型

Nullable types and Non-Null Types

Kotlin 类型系统的设计就是为了避免代码中因为 null 的引用带来的危险。

在 Java 中，null 的引用一般就等同于一个空指针异常 NullPointerException 。空指针异常成为大部分 Java 开发的应用程序崩溃的首要原因了，防不胜防啊，指不定什么时候就出一个 null 出来了，以至于程序中有大量的if(a == null) 之类的判断。

在 Kotlin 的设计就是为了避免出现没有空指针的，但是有一些情况下，你还是可以得到一个空指针的。

 * 一个主动抛出空指针异常的代码 throw NullPointerException()
 * 使用 !! 操作符，
 * 调用外部的 Java 代码引起的空指针
 * There's some data inconsistency with regard to initialization (an uninitialized this available in a constructor is used somewhere)

 在 Kotlin 的类型系统（type system）中，类型被分成可以包含 null 的引用和不能包含 null 的引用。比如，下面的代码，String 类型的 a 是不能包含 null 的：

    var a: String = "abc"
    a = null // 编译错误

如果你需要允许出现 null，那么需要使用 String? 来定义：

    var b: String? = "abc"
    b = null // ok

对于变量 a ，你可以放心的使用，因为它不会出现 null 的情况，而变量 b 就不能直接使用，编译器都会帮你，当你直接调用变量 b 的方法或者属性的时候，编译器会报告出一个错误。

    val l = a.length
    val l = b.length // error: variable 'b' can be null

Kotlin 提供了其他办法让我们访问变量 b。

## 在条件判断语句中检查 null 

和 Java 代码一样，添加 if 判断，比如：

    val l = if (b != null) b.length else -1

不同的是，Java 代码添加的 if 语句是在运行时进行判断的，Kotlin 在编译时就做了检测了。包括在 if 语句的前半部分，如果做了 null 的检测，if 语句的后续部分就可以使用该变量了，比如：

    if (b != null && b.length > 0) {
        print("String of length ${b.length}")
    } else {
        print("Empty string")
    }

Note that this only works where b is immutable (i.e. a local variable which is not modified between the check and the usage or a member val which has a backing field and is not overridable), because otherwise it might happen that b changes to null after the check.

## 安全调用 Safe Calls

你也可以使用问号+点号的方式来安全调用 **?.** ，比如：

    b?.length

这里会返回 b 的 length，或者返回 null 如果 b 是 null 的话。这种安全调用会节省很大 if 的判断，比如我们可能会碰见这样的代码：

    bob?.department?.head?.name

这里会在整个代码的任何一个对象为 null 的情况返回 null。

?. 还可以和 let 关键词一起使用，比如：

    val listWithNulls: List<String?> = listOf("A", null)
    for (item in listWithNulls) {
         item?.let { println(it) } // prints A and ignores null
    }

null 的那个会被忽略掉，而不会引起空指针异常。

## Elvis 操作符

当我们拥有一个引用 r，如果 r 不为空的话，我们使用 r，否则，我们用另外一个值代替，比如：

    val l: Int = if (b != null) b.length else -1

我们可以写成下面的样子：

    val l = b?.length ?: -1

?: 表达式就相当于一个简写的 if 语句。如果 ?: 左边的表达式不是 null，则返回左边的结果，否则返回 ?: 右边的表达式。
在 Kotlin 中，throw 和 return 也都是表达式，所以也可以出现在 ?: 的右边，比如：

    fun foo(node: Node): String? {
        val parent = node.getParent() ?: return null
        val name = node.getName() ?: throw IllegalArgumentException("name expected")
        // ...
    }


## !! 操作符

如果你期望代码会抛出一个 NPE，而不需要你主动判断然后再去 throw，那么你可以使用 !! 操作符，比如：

    val l = b!!.length

当 b 是一个 null 的时候，代码执行在这里会抛出一个 NullPointerException。

## 安全类型转换 Safe Casts

在 Java 中，如果类型转换不匹配的时候，会抛出 ClassCastException，安全的类型转换可以在这种情况下，返回一个 null，比如：

    val aInt: Int? = a as? Int

上面的代码，如果 a 不是一个 Int，那么 aInt 等于 null。

## 可为空类型的集合 Collections of Nullable Type

如果你有一个集合，包含的元素是可为空的，你需要过滤出那些非空的元素，那么你可以使用 filterNotNull ：

    val nullableList: List<Int?> = listOf(1, 2, null, 4)
    val intList: List<Int> = nullableList.filterNotNull()

