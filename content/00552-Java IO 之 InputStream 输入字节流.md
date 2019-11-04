# Java IO 之 InputStream 输入字节流
- 2016-04-07 16:15:37
- Java
- java,inputstream,输入流,io,

<!--markdown-->java.io 包中包含了咱们跟 IO 打交道中必要的类和接口。IO 流可以分为输入流和输出流，也可以分为字节流(byte stream)和字符流(character stream)。只是划分的维度不一样而已。

# java.io.Closeable

Closeable 是一个接口，继承于 java.lang.AutoCloaseable 接口，close() 方法可能会抛出 IOException 异常。


# java.io.InputStream

InputStream 是所有输入字节流的父类。字节流表示它操作的对象是字节，与字节流对应的是字符流，Reader 是输入字符流的父类，咱们可以通过其 API 的设计看出区别。

## InputStream API 

* int available()
* int read(byte[] buffer)
* int read()
* int read(byte[] buffer,int byteOffset,int byteCount)
* long skip(long byteCount)

# java.io.FileInputStream

FileInputStream 是一个常见的 InputStream 的直接子类。一般用来读取文件，也就是说把一个文件当成输入，以字节流的方式读取。

常见的用法是：

    File file = ...
    FileInputStream fis = new FileInputStream(file);

## FileInputStream 构造器

FileInputStream 有三个构造器

* FileInputStream(File file)
* FileInputStream(FileDescriptor fd)
* FileInputStream(String path)

## FileInputStream API

下面列出 FileInputStream 比 InputStream 增加的 API

* FileChannel getChannel() Returns a read-only FileChannel that shares its position with this stream
* final FileDescriptor getFD() Return the underlying file descriptor.

# ByteArrayInputStream

字节数组输入流，把一个字节数组当成输入，以字节流的方式读取这个数组。

## ByteArrayInputStream 构造器

* ByteArrayInputStream(byte[] buffer)
* ByteArrayInputStream(byte[] buf,int offset,int length)

# FilterInputStream

## FilterInputStream 构造器

* FilterInputStream(InputStream in)

# ObjectInputStream

ObjectInputStream 是把一个 Java 对象当成一个输入。

## ObjectInputStream 构造器

* ObjectInputStream(InputStream input)

## ObjectInputStream API

ObjectInputStream 有丰富的 API，这里不具体罗列，因为咱们平时用的也不多。ObjectInputStream 一般与 ObjectOutputStream 配合使用，先通过 ObjectOutputStream 往流里写入数据，包括 Java 对象的成员变量的字段名字以及值。ObjectInputStream 在获取到流后，再以写入的反向顺序读取出来，还原出来 Java 对象。

可能的运用场景是对 Java 对象的保存，比如保存到文件中，再恢复的时候从文件中还原对象。另外一种是两个进程之间的对象传输，把 A 进程的 Java 对象传输到 B 进程。

# PipedInputStream

pipe 一般翻译为管道，当两个线程（注意，是线程）需要传送数据的时候，一个创建管道输出流，一个创建管道输入流。

## PipedInputStream 构造器
* PipedInputStream()
* PipedInputStream(PipedOutputStream out)
* PipedInputStream(int pipeSize)
* PipedInputStream(PipedOutputStream out,int pipedSize)

## PipedInputStream API

* viod connect(PipedOutputStream out)

# SequenceInputStream

sequence 有按顺序排好的意思，SequenceInputStream 的作用是把两个或者多个 InputStream 按顺序读取。第一个 InputStream 读取结束了，接着读取第二个 InputStream。

## SequenceInputStream 构造器

* SequenceInputStream(InputStream s1, InputStream s2)
* SequenceInputStream(Enumeration<? extends InputStream> e)

# LineNumberInputStream

LineNumberInputStream 的上级父类是 FilterInputStream，不是 InputStream 的直接子类。其作用是对其包裹的 InputStream 进行读行的计数，每当读到 '\r','\n' 和 '\r\n' 的时候，计数会加一。这个类在引入到 Android 的时候就被抛弃，建议使用 LineNumberReader 替代。

# BufferedInputStream

FilterInputStream 的子类，其作用是对其包裹的 InputStream 进行缓冲。缓冲带来的缺点就是占用了一定的空间。

# DataInputStream

InputStream 是字节流，每次 read 只能读取一个字节，或者一个字节数组，如果我们需要读取一个 int，那么就需要读取 4 个字节，然后再对其进行移位，最后得到一个 int，而 DataInputStream 则把这些操作封装好了。

## DataInpuptStream 构造器

* DataInputStream(InputStream in)

## DataInputStream API

* final byte readByte()
* final byte readInt()
* final byte readLong()
* final byte readDouble()
* final String readLine() NOTE:Deprecated in API level 1. See BufferedReader
* final String readUTF()




