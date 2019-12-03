# Java 基础知识复习点
- Java,面试,基础知识
- 2018.09.08

在 Java 中，一共有 8 种基本类型（primitive type），4 种整形，2 种浮点类型，1 种用于表达 Unicode 编码的字符单元的字符类型 和 1种表示真值的 boolean 类型。

float 类型占 4 个字节，单精度，有效位大约 6-7 位。double 占 8 个字节，双精度，有效位大约 15 位。

char 类型用来表示单个字符，Unicode 编码单元可以表示范围 \u0000 - \uffff 。

在 Java 中，不区分变量的声明和定义。

final 修饰的变量表示只能被赋值一次。

static 修饰的变量称为类变量

static final 修改的变量称为常量。

运算符的优先顺序，编码规范要求尽可能使用括号来表达优先顺序。

i++ 和 ++i 的区别，i++ 先使用变量的值，再++；++i，先++，再使用变量的值。

>>> 0 填充高位，>> 符号位填充高位，<<< 没有这种操作～～

数值类型的转换，在运算的时候，数值类型会向高精度转换。

强类型转换，会损失精度

String 不可变字符串

StringBuilder 线程不安全，StringBuffer 线程安全

switch case 支持整数和枚举常量，在 Javay7 中加入了 String 的支持。

数组大小不能改变。

for each 表达式，遍历的对象是数组或者实现了 Iterable 接口的类对象。

for each 的优点是没有下标，缺点也是没有下标。

数组拷贝，Arrays.copyOf() 和 System.arraycopy() 方法。

Arrays.sort() 方法使用了优化的快速排序算法。

Java 上没有多维数组，只有一维数组，多维数组由“数组的数组”组成。

算法 + 数据结构 = 程序 （Algorithms + Data Structures = Programs ， Prentice Hall）

封装（encapsulation），继承（inheritance）

类之间的关系：依赖 dopendence（uses-a），聚合 aggregation（has-a），继承 inheritance（is-a）

不要编写返回引用可变对象的访问器方法，如果需要返回一个可变数据域的拷贝，应该使用克隆。

final 修饰符大都应用于基本数据（primitive）类型域，或不可变（immutable）类的域

如果类中的每个方法都不会改变其对象，这种类就是不可变的类，比如 String

值调用（call by value）表示方法接收的是调用者提供的值，引用调用（call by reference）表示方法接收的是调用者提供的变量地址。Java 中采用的是值调用，方法得到的是所有参数值的一个拷贝。

方法的签名（signature）包含方法名以及参数类型，不包含返回类型。所以，不能存在两个名字相同，参数类型相同，返回类型不同的方法。

初始化数据域的方法，在构造器中赋值，在声明中赋值，在初始化块（initialization block）中赋值。但是初始化块并不推荐使用。

finalize() 方法，在垃圾回收器清除对象前调用。

超类（superclass），基类（base class），父类（parent class）
子类（subclass），衍生类（derived class），子类（child class）

子类可以增加域，增加方法，或者覆盖（override）父类的方法，但是不可以删除继承的任何域和方法。

一个对象变量可以引用多种实际类型的现象称为多态（polymorphism），在运行时能够自动地选择调用哪个方法的现象称为多态绑定（dynamic binding）。

静态绑定（static binding）表示在编译期可以准确地知道调用的方法，动态绑定需要在运行时，根据上下文，确定调用的方法。为了减少动态绑定的开销，Java 中为每个类创建了一个方法表（method table）

final 类表示该类不允许被继承，final 类没有任何的子类，俗称断子绝孙类。

final 方法表示子类不能覆盖这个方法。final 类的所有方法自动地成为 final 方法。

类型转换：把一个类型强制换成另外一个类型的过程。使用 instanceof 来判断是否可以类型转换，如果没有进行判断可能会抛出 ClassCastException 异常。

Java 语言规范要求 equals 方法需要具有以下几个特性。1)自反性，x.equals(x) = true. 2)对称性 x.equauls(y) = y.equals(x) 3) 传递性 x.equals(z) = y.eqals(z) 4）一致性，反复调用 x.equals(y) 返回一样的值 5）对于任意 x != null 的情况下，x.equals(null) = false

散列值（hash code）是由对象导出的一个整型值，散列值没有规律。每个对象默认有一个散列码，其值为对象的存储地址。

如果重新定义 equals 方法，就必须重新定义 hashcode 方法。以便可以将对象插入到散列表中。

ArrayList 是一个采用类型参数（type parameter）的泛型类（generic class）

打包和拆包是编译器认可的，装箱，拆箱的说法源于 C#，自动打包（autowrapping）

Java 5 提供了参数数量可变的方法，编译器会把可变数量参数变成数组，比如 Object... 变成 Object[]

Java 5 增加了枚举类型，所有枚举类型都是 Enum 类的子类。比较枚举不需要调用 equals 方法，直接使用 “==” 就可以了。

能够分析类能力的程序被称为反射（reflective）

class.getName() 方法返回该 Class 的名字，数组类型返回会类似 [Ljava.lang.Double 表示Double[] 或者 [I 表示 int[]

静态方法 Class.forName(classname) 可以获得类名对应的 Class 对象。

通过反射构造对象有两种方法。第一种，通过 Class.forName() 获得 Class 对象，然后调用 class.newInstance() 方法，会调用默认无参构造器。第二种是通过 Constructor.newInstance() 来调用有参的构造器。

Class 类的 getFields(),getMethods(),getConstructors() 得到的是 public 修饰的成员，getDeclareFields(),getDeclareMethods(),getDeclaredConstructors() 得到所有的成员，包括 private 的，但是不包括父类的成员。

反射机制的默认行为受限于 Java 的访问控制，通过调用 setAccessible(boolean) 方法可以解除访问控制。

接口中的所有方法都是 public 的，接口中所有的域都是public static final 的。

默认的克隆是浅拷贝，没有克隆包含在对象中的内部对象。

内部类（inner class）是定义在另一个类中的类。内部类方法可以访问该类定义所在的作用域中的数据，包括私有的数据。内部类对同一个包的其它类隐藏起来。匿名（anonymous）内部类场用来做回调函数。

私有的内部类对外是不可见的，这样设计可以减少 api 对外的暴露。当然内部类也可以设计成公开的。

内部类有外部类的隐式的引用，通过这个引用可以访问外部类的全部状态。static 内部类，也有称静态内部类，其实应该是嵌套类（nested class），是没有外部类的引用的。

Error 和 Exception 继承于 Throwable 。Error 描述了 Java 运行时系统的内部错误和资源耗尽错误。应用程序不应该抛出 Error。Exception 分为 RuntimeException 和其它异常。由程序错误导致的异常属于 RuntimeException；而程序本身没有错误，由于环境等问题导致的异常属于其它异常。Error 和 RuntimeException 称为未检测（unchecked）异常。其它异常称为已检测（checked）异常。

我们需要处理已检测异常，对于未检测异常，要么我们无能无力，比如 Error，要么我们可以避免，比如 RuntimeException。

final 子句的 return 会覆盖 try 子句的 return 值。
