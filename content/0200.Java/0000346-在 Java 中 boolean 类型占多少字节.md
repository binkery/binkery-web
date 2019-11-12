# 在 Java 中 boolean 类型占多少字节
- Java,数据类型,虚拟机,boolean,

在 Java 中，boolean 类型占用多少空间呢？刚才在 CSDN 上看了一下，一个很老的帖子里有人讨论来着，有人说 1 bit ，有人说 1 byte ， 也有人说 4 bytes ，那到底是多少呢？


先来个官方文档的说法。
> boolean: The boolean data type has only two possible values: true and false. Use this data type for simple flags that track true/false conditions. This data type represents one bit of information, but its "size" isn't something that's precisely defined.

上面的说的很清楚，boolean 值只有 true 和 false 两种，这个数据类型只代表 1 bit 的信息，但是它的“大小”没有严格的定义。也就是说，不管它占多大的空间，只有一个bit的信息是有意义的。

咱们再去看看 Java 虚拟机规范上是怎么写的。

> Although the Java Virtual Machine defines a boolean type, it only provides very limited support for it. There are no Java Virtual Machine instructions solely dedicated to operations on boolean values. Instead, expressions in the Java programming language that operate on boolean values are compiled to use values of the Java Virtual Machine int data type. 

Java 虚拟机虽然定义了 boolean 类型，但是支持是有限的，没有专门的虚拟机指令。在 Java 语言中，对 boolean 值的操作被替换成 int 数据类型。

> The Java Virtual Machine does directly support boolean arrays. Its newarray instruction (§newarray) enables creation of boolean arrays. Arrays of type boolean are accessed and modified using the byte array instructions baload and bastore (§baload, §bastore). 

Java 虚拟机没有直接支持 boolean 数组。boolean 类型数组和 byte 数组公用指令。

> In Oracle’s Java Virtual Machine implementation, boolean arrays in the Java programming language are encoded as Java Virtual Machine byte arrays, using 8 bits per boolean element.

在 Oracle 的 Java 虚拟机实现中，Java 语言中的 boolean 数组被编码成 Java 虚拟机的 byte 数组，每个元素占 8 比特。

> The Java Virtual Machine encodes boolean array components using 1 to represent true and 0 to represent false . Where Java programming language boolean values are mapped by compilers to values of Java Virtual Machine type int , the compilers must use the same encoding. 

Java 虚拟机使用 1 表示 true ，0 表示 false 来编码 boolean 数组。Java 语言的 boolean 值被编译器映射成 Java 虚拟机的 int 类型的时候，也是采用一样的编码。

Ok，现在可以总结一下了。

1. boolean 类型被编译成 int 类型来使用，占 4 个 byte 。
2. boolean 数组被编译成 byte 数组类型，每个 boolean 数组成员占 1 个 byte 。
3. 在 Java 虚拟机里，1 表示 true ，0 表示 false 。
4. 这只是 Java 虚拟机的建议。
5. 可以肯定的是，不会是 1 个 bit 。