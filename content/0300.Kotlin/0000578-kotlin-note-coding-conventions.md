# Kotlin 自学笔记 - 编码规范
- Kotlin自学笔记,Kotlin编码规范,Kotlin学习笔记
- 2019.05.03

## Applying the style guide

IntelliJ IDE 提供了对应的插件，应用插件，可以在编程的时候对你进行一些友好的提示。

## 源代码组织 Source Code Organization

### 目录结构 Directory structure

在混合语言的项目中，比如和 Java 代码一起，Kotlin 的源码可以和 Java 代码采用相同的代码目录结构，这样看上去，他更像是一个 Java 项目，和 Java 完全融合在一起。

如果在纯粹的 Kotlin 项目中，就可以采用比较省略的目录结构。在 Java 中，包名和目录结构必须完全一致，而 Kotlin 并不需要，但是项目中，我们一般也不允许源代码随便乱放，还是和 Java 类似，只是可以省略掉相同的根目录，这样比较减少目录的层级嵌套。

### 源文件命名 source file names

如果一个 Kotlin 文件只包含一个类，那么这个 kotlin 文件和这个类同名，如果一个文件包含多个类，选择一个类同名。文件命名符合驼峰命名。

文档中说，命名要能描述这个代码，因此，避免使用一些没有意义的名字命名文件。这和没说一样，命名一直是程序员心中永远的痛。

## 源文件组织 Source file organization

Placing multiple declarations (classes, top-level functions or properties) in the same Kotlin source file is encouraged as long as these declarations are closely related to each other semantically and the file size remains reasonable (not exceeding a few hundred lines).

In particular, when defining extension functions for a class which are relevant for all clients of this class, put them in the same file where the class itself is defined. When defining extension functions that make sense only for a specific client, put them next to the code of that client. Do not create files just to hold "all extensions of Foo".

### 类布局 class layout

通常，一个类的内容按以下的顺序排列：

  - 属性定义，初始化代码块 property declarations and initalializer blocks
  - 次要构造器 Secondary constructors
  - 方法定义 method declarations
  - 伴生对象 companion object
  
一般，我们把功能相关的代码放在一起，不需要按字母排序，也不需要按开放权限排序，这些功能交给 IDE，他们会帮你快速检索的，现在的 IDE 已经不是当年的 IDE 了。这样的排序对于你的代码的阅读者是友好的。
  
内部类一般放在你使用他的代码的后面，我们经常会把内部类放在文件的最后面。和我们开发 Java 代码一样。

### 接口继承的布局 interface implememention layout

当一个类继承于一个接口的时候，继承的成员的排序和接口定义成员的顺序保持一致。


### 重载的布局 overload layout

永远把重载的内容放在相邻的地方，这个和上面的要求是一致的，相同功能的代码放在一起。

## 命名规则 Naming rules

Kotlin 跟随 Java 的命名规则。基本上就是驼峰命名法。

原则上，包名永远都是小写的，不使用下划线。

类名和 object 大写开头。方法首字母小写，特殊的是在工厂方法中，工厂方法的方法和类名一致，这是比较特殊的。在 Kotlin 中，创建对象已经不需要 new 关键词了，工厂方法本身的功能就是创建对象并且把对象返回给调用者，这种情况下，工厂方法的方法名采用首字母大写，看起来会更舒服一些吧。

## 测试方法的命名 Names for test methods

## 属性命名 Property names

基本上，常量，不可变量，一般的命名是大写 + 下划线，可变量采用首字母小写 + 驼峰命名的规则。

如果一个类中有两个属性的意义是相同的，但是一个是对外公开的，另外一个是具体的内部实现的，那个内部实现的属性可以用下划线开头。

## Choosing good names

还是那个问题，谁都知道应该起一个好听、好用、好记、正确、准确的名字，但是呢～

文档中有一个例子我以前并没有注意到，**sort** 方法一般是对一个容器进行排序，**sorted** 则是返回一个排好序的容器的副本。

## 开发格式化 Formatting

大部分情况下，kotlin 采用和 Java 一样的代码规范。

缩进采用 4 个空格，而不是用 tab 。

对于大括号，文档上说了，左括号在行为，右括号另起一行，和对于代码对齐。这样子的话，括号另起一行的就是异教徒了。









  
  








