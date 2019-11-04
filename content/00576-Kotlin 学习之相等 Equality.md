# Kotlin 学习之相等 Equality
- 2017-05-23 08:49:48
- Kotlin
- 比较,kotlin,相等,

<!--markdown-->在 Kotlin 中，有两种相等，
 Referential equality 两个引用指向同一个对象
 Structural equality 通过 equals() 方法判断两个对象是否相等。

## 引用相等 Referential equality

三个等号 === 用来表示引用相等的判断，相反的符号为 !== 。 a === b 只有在 a 和 b 都指向同一个对象的时候才返回 true。

=== 比较的其实是内存地址，如果两个对象的内存地址是一样，那么 === 返回的就是 true。

## 结构相等 Structural equality

两个等号 == 用来表示结构相等的判断，相反的符号为 !=。 一般来说，a == b 表达式等同于以下代码

    a?.equals(b) ?: (b === null)

上面代码的意思是，如果 a 不是 null 的话，就调用其 equals(Any？) 方法，如果 a 是 null 的话，那么就判断 b 是不是 null 了。

== 比较的是对象的 equals() 方法。

一般情况下，a == null 会自动变成 a === null。