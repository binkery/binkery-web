# Java NIO 完全学习笔记
- 2016-04-08 09:58:37
- Java
- nio,channel,buffer,selector,

<!--markdown-->本篇博客依照 [Java NIO Tutorial](http://tutorials.jenkov.com/java-nio/index.html) 翻译，算是学习 Java NIO 的一个读书笔记。建议大家可以去阅读原文，相信你肯定会受益良多。

# 1. Java NIO Tutorial

Java NIO，被称为新 IO(New IO)，是 Java 1.4 引入的，用来替代 IO API的。

## Java NIO：Channels and Buffers

标准的 Java IO API ，你操作的对象是字节流(byte stream)或者字符流(character stream)，而 NIO，你操作的对象是 channels 和 buffers。数据总是从一个 channel 读到一个 buffer 上，或者从一个 buffer 写到 channel 上。

## Java NIO:Non-blocking IO

Non-blocking 是非阻塞的意思。Java NIO 让你可以做非阻塞的 IO 操作。比如一个线程里，可以从一个 channel 读取数据到一个 buffer 上，在 channel 读取数据到 buffer 的时候，线程可以做其他的事情。当数据读取到 buffer 上后，线程可以继续处理它。

## Java NIO: Selectors

selector 翻译为选择器，selector 可以监控(monitor)多个 channel 的事件。

# 2. Java NIO OverView

Java NIO 有三个核心组件(core components)：

* Channels
* Buffers
* Selectors

除了这三个核心组件外，还有一些辅助的类，但是咱们现在最关心的是这三个。

### Channels and Buffers

一般来说，NIO 都是从一个 Channel 开始的，Channel 有点像流(Stream)，通过 channel，数据可以读取到 Buffer，同样的，数据是从 Buffer 写入到 Channel 的。

NIO 中包含了几个常见的 Channel ，这几个 channles 包含了咱们开发中使用率较高的 文件 IO，UDP+TCP 网络 IO。

* FileChannel
* DatagramChannel
* SocketChannel
* ServerSocketChannel

NIO 中实现了几个常用的 Buffer

* ByteBuffer
* CharBuffer
* DoubleBuffer
* FloatBuffer
* IntBuffer
* LongBuffer
* ShortBuffer
* MappedByteBuffer

这几个 Buffer 分别对应了 Java 的几个基础类型，唯独没 boolean 类型的 Buffer。MappedByteBuffer 是一个特殊的，一般被用来做内存映射(memory mapped files)。

### Selectors

选择器让一个线程可以处理多个 Channels。如果你的应用有多个连接打开，但每个连接的流量都比较低(low traffic)，为每个连接单开一个线程显得比较浪费，而选择器让你可以在一个线程中操作这些低流量的连接，减少的线程的开销。

# 3. Java NIO Channel

Java NIO Channel 和流有些相似，但也有不少不同：
* 一个 Channel 可以读和写，而一个流一般只能读或者写
* Channel 可以异步(asynchronously)的读和写
* Channel 总是需要一个 Buffer，不管是读到 Buffer 还是从 Buffer 写到 Channel

### Channel Implementations

Java NIO 实现了几个常见的 channel:
* FileChannel 读取数据或者写入数据到文件中
* DatagramChannel 读写数据通过 UDP 协议
* SocketChannel 读写数据通过 TCP 协议
* ServerSocketChannel 提供 TCP 连接的监听，每个进入的连接都会创建一个 SocketChannel。

### Basic Channel Example

下面是一个简单的例子，大概的步骤是打开一个文件的连接，然后获取到一个 Channel，开辟一个 Buffer，从 channel 读取数据到 buffer，然后再从 Buffer 中获取到读取的数据。

    RandomAccessFile aFile = new RandomAccessFile("data/nio-data.txt", "rw");
    FileChannel inChannel = aFile.getChannel();

    ByteBuffer buf = ByteBuffer.allocate(48);

    int bytesRead = inChannel.read(buf);
    while (bytesRead != -1) {

      System.out.println("Read " + bytesRead);
      buf.flip();

      while(buf.hasRemaining()){
          System.out.print((char) buf.get());
      }

      buf.clear();
      bytesRead = inChannel.read(buf);
    }
    aFile.close();

# 4. Java NIO Buffer

在和 Channel 交互的时候，需要一个 Buffer，从 Channel 中读取数据放入到 Buffer 中，或者从 Buffer 中写入数据到 Channel 中。我们并不直接操作 Channel，而是操作 Buffer。

### Basic Buffer Usage

使用 Buffer 一般需要下面四个步骤：
* 写数据到 Buffer
* 调用 buffer.flip()
* 从 Buffer 读出数据
* 调用 buffer.clear() 或者 buffer.compact()

当你往 Buffer 中写数据，Buffer 会记录你已经写了多少数据，一旦你需要从 Buffer 中读数据，你需要调用 flip() 方法，让 Buffer 由写模式编程读模式。读模式下，你可以读出你刚写入的所有数据。

当你读完所有数据后，你需要清空 buffer，让 Buffer 变成可以写入的状态。有两个办法让 Buffer 变成写模式，一个是调用 clear() 方法，一个是 compact() 方法。clear() 方法会清空 Buffer 的所有数据，而 compact() 方法之清除你已经读取的数据，那些在 Buffer 中而没有被读取的数据会被移动到 Buffer 的开头部分，下次写的时候就从移动后最后的位置开始写入。

### Buffer Capacity,Position and Limit

一个 Buffer 本质上是一个内存块，你可以往里写入数据，并且可以从里往外读取数据。这样一个内存块被包裹在一个 Buffer 对象中，并且 Buffer 提供了一些方便操作方法。

Buffer 有三个重要的属性，理解这三个属性让你能更加明白 Buffer 的原理。

* capacity
* position
* limit

在读模式和写模式下，position 和 limit 有着不同的意思，但 capacity 在读模式和写模式下，意思是相同的。

#### Capacity

capacity 是容量的意思。当你创建一个 Buffer 对象的时候，这个 Buffer 的容量就是固定的，你只能写入小于等于 capacity 大小的数据，如果这个 Buffer 已经满了，你要么需要读出数据，要么需要清空数据，否则你不能写人更多的数据。

#### Position

position 是位置的意思，在你写入数据到 Buffer 的时候，这个数据被放入一个确切的位置，position 从 0 开始，写入一个数据，position 往后移动一个单元，也就是 +1 ，直到等于 capacity -1 。

当你读取数据的时候，也是从一个确切的位置读取的。当你调用 flip() 方法，Buffer 由写模式变成了读模式，position 变成了 0,当你读一个数据的时候，position 同样往后移动一个单位。

#### Limit

limit 是极限的意思，在写模式下，limit 是等同于 capacity 。当由写模式变成读模式的时候，limit 被设置为写模式下最后写入的 position。这样，position 由 0 开始，可以读到 limit 的位置。因为在读模式下，超过 limit 位置的数据其实是不合法的数据，不应该被读出。

### Buffer Types

Java NIO 实现了下面几个 Buffer，上文已经做了些介绍了。

* ByteBuffer
* MappedByteBuffer
* CharBuffer
* DoubleBuffer
* FloatBuffer
* IntBuffer
* LongBuffer
* ShortBuffer

### Allocating a Buffer

每个 Buffer 类都有 allocate() 的静态方法，用这个方法可以创建一个 Buffer 实例，比如：

    ByteBuffer buf = ByteBuffer.allocate(48);
    CharBuffer buf = CharBuffer.allocate(1024);

### Writing Data to a Buffer

有两种写入数据到 Buffer 的方法：
1. 通过 Channel 写入数据
2. 通过 Buffer 的 put() 方法写入数据

代码如下：

    int bytesRead = inChannel.read(buf); //read into buffer.
    buf.put(127);

当然，put() 方法有很多重载的方法可以让你通过各种姿势写入数据。具体的用法看 JavaDoc，很简单的。

### flip()

flip() 方法让一个 Buffer 从写模式变成读模式，这个方法调用后，position 回到 0，limit 变成写模式的最后一个位置。其实就是在读写模式切换的时候，对 position 和 limit 属性的修改。

### Reading Data from a Buffer

和写数据相似，读数据也有两种方式：
1. 通过 channel
2. 通过 Buffer 的 get() 方法。

下面是代码：

    int bytesWritten = inChannel.write(buf);
    byte aByte = buf.get(); 

同 put() 方法，也有很多 get() 方法可以使用。

### rewind()

Buffer.rewind() 方法让 position 回到 0，这样你可以再次读取一次数据。但这个方法并不会影响 limit 属性。

### clear() and compact()

每次当你完成读数据后，需要让 Buffer 变回写模式，你可以通过调用 clear() 或者 compact() 方法。

clear() 方法让 position 等于 0，limit 等于 capacity 。相当于 Buffer 被清空了，但事实上数据本身没有被清空，只是这个 Buffer 的所有数据单元都是可写入的，可覆盖的。

如果你调用了 clear() 方法，Buffer 中那些没有被你读取的数据就等于被清除了，你再也没有机会再读取他们了。

如果你还有部分数据没有读取不想丢掉，但是又需要让 Buffer 再次进入写模式，那么你应该调用 compact() 方法。compact() 方法会先拷贝那些还没有被读取的数据到 Buffer 的开头部分，position 设置在这部分数据的结束的位置，limit 还是等于 capacity 。当进入写入模式后，写入的数据就从 position 的位置开始往后写，之前没有被读取的数据被保存了下来。

### mark() and reset()

调用 Buffer.mark() 的时候，在这个 Buffer 上做一个标记，在稍后调用 Buffer.reset()，position 会回到刚才标记的位置。

### equals() and compareTo()

这两个方法用来比较两个 Buffer 是否相同。


# 5. Java NIO Scatter / Gather 

scatter 有分散，散开的意思，gather 有收集，聚合的意思。scatter 的意思是从一个 channel 读取数据，填充到多个 Buffer 中，gather 的意思是把多个 Buffer 的数据写入到一个 Channel 中。

### Scattering Reads

scattering read 表示从一个 channel 中读取数据填充到多个 Buffer 中，比如：

    ByteBuffer header = ByteBuffer.allocate(128);
    ByteBuffer body   = ByteBuffer.allocate(1024);

    ByteBuffer[] bufferArray = { header, body };

    channel.read(bufferArray);

这里有个限制，只有当第一个 Buffer 被填充满的情况下才会被填充到下一个 Buffer 中，像上面的例子，除非你能确保 header 部分肯定是 128 个字节，不然就不适合这样的写法。

### Gathering Writes

gathering write 表示可以把多个 Buffer 的数据写入到一个 channel 中。

    ByteBuffer header = ByteBuffer.allocate(128);
    ByteBuffer body   = ByteBuffer.allocate(1024);

    //write data into buffers

    ByteBuffer[] bufferArray = { header, body };

    channel.write(bufferArray);

当从 Buffer 中读数据往 channel 里写的时候，Buffer 可读的范围受 limit 限制，所以，如果上面代码中 header 只被写入 58 个字节的时候，从 header 往外读也只会是 58 字节，不会是 128字节。

# 6. Java NIO Channel to Channel Transfers

Java NIO 支持两个 channel 直接转移数据。

### transferFrom()

    RandomAccessFile fromFile = new  RandomAccessFile("fromFile.txt", "rw");
    FileChannel fromChannel = fromFile.getChannel();

    RandomAccessFile toFile = new RandomAccessFile("toFile.txt", "rw");
    FileChannel toChannel = toFile.getChannel();

    long position = 0;
    long count = fromChannel.size();

    toChannel.transferFrom(fromChannel, position, count);

position 和 count 两个参数用来告诉开始传输的起始位置和多少个字节需要传输，如果源 channel 的大小小于 count，那么取那个数值小的。

一些 SocketChannel 会只传输当前 channel 对应的 Buffer 已经准备好的数据，即使 SocketChannel 稍后还有更多的数据。因此，可能不能完整的传输一个 SocketChannel 的数据到一个 FileChannel。

### transferTo()

下面是一个使用 transferTo() 的例子。和上文的例子相似，如果从一个 SocketChannel 传输数据到一个 FileChannel，传输会在读取完当前 SocketChannel 可用的数据后就结束，而很大可能不是全部数据。

    RandomAccessFile fromFile = new RandomAccessFile("fromFile.txt", "rw");
    FileChannel fromChannel = fromFile.getChannel();

    RandomAccessFile toFile = new RandomAccessFile("toFile.txt", "rw");
    FileChannel toChannel = toFile.getChannel();

    long position = 0;
    long count = fromChannel.size();

    fromChannel.transferTo(position, count, toChannel);


# 7. Java NIO Selector

Selector 让一个线程可以同时管理多个 Channel。

### Why use a Selector?

最大的好处是你可以一个线程管理多个 channel，而不是多个线程。一般咱们认为在多个线程之间切换是相对昂贵的，每个线程都占用着一定的系统资源，比如内存，所以越少的线程是越好的。

当然，现在的操作系统和 CPU 更好的支持了多线程工作，如果你的 CPU 是多核的，不使用多任务的话，等于浪费 CPU。

不管怎么说，特别对于 Android 开发来说，线程肯定也是宝贵的，能少就少。

### Creating a Selector
    
    创建 Selector 很简单，调用 open() 方法就可以了。

    Selector selector = Selector.open();

### Registering Channels with the Selector

使用选择器，必须对 Channel 进行注册。注册例子：

    channel.configureBlocking(false);

    SelectionKey key = channel.register(selector, SelectionKey.OP_READ);

Channel 必须是非阻塞的，FileChannel 不能使用选择器，因为 FileChannel 没有非阻塞模式。

在调用 register() 方法的时候，第二个参数表面了你对那些事件感兴趣，只有你感兴趣的事件，你才会收到对应事件的回调，一共有四个事件：

1. Connect
2. Accept
3. Read
4. Write

当一个 Channel 发起一个事件的时候，意味着这个事件已经准备好了。比如，只有在一个 Channel 成功连接到另一个服务的时候，才意味着连接完成(connect ready)。一个 ServerSocketChannel 只有在与一个客户端的建立连接后，才会触发 accept ready。当一个 Channel 准备好可读的时候，才是 read ready,准备好可写的时候，才是 write ready。

下面有四个常数，被用在 register() 的第二个参数。

1. SelectionKey.OP_CONNECT
2. SelectionKey.OP_ACCEPT
3. SelectionKey.OP_READ
4. SelectionKey.OP_WRITE

### SelectionKey's

register() 方法返回一个 SelectionKey 对象，这个对象包含了一些咱们需要关心的属性：

* The interest set
* The ready set
* The Channel
* The Selector
* An attached object (optional)

#### Interest Set

Interest Set 就是在注册监听的时候，咱们设置的兴趣的集合。

    int interestSet = selectionKey.interestOps();

    boolean isInterestedInAccept  = interestSet & SelectionKey.OP_ACCEPT;
    boolean isInterestedInConnect = interestSet & SelectionKey.OP_CONNECT;
    boolean isInterestedInRead    = interestSet & SelectionKey.OP_READ;
    boolean isInterestedInWrite   = interestSet & SelectionKey.OP_WRITE; 


通过以上的代码，咱们可以获取哪些事件是已经设置为感兴趣的。

#### Ready Set

Ready set 是准备集合，可以通过它来获取当前有哪些事件是准备完成的。获取状态集合的代码：
    
    int readySet = selectionKey.readyOps();

也可以通过下面的 API ，更方便的得到当前的状态是否可用。

    selectionKey.isAcceptable();
    selectionKey.isConnectable();
    selectionKey.isReadable();
    selectionKey.isWritable();

#### Channel + Selector

通过 SelectionKey 可以获得 Channel 对象和 Selector 对象：

    Channel  channel  = selectionKey.channel();

    Selector selector = selectionKey.selector();

#### Attaching Objects

附加的对象，你可以往 SelectionKey 添加对象，在稍后的时候，你可以从 SelectionKey 取出添加的对象。

    selectionKey.attach(theObject);

    Object attachedObj = selectionKey.attachment();

添加对象也可以在注册的时候添加：

    SelectionKey key = channel.register(selector, SelectionKey.OP_READ, theObject);

### Selecting Channels via a Selector

当你把多个 Channel 注册到 Selector，你可以通过调用 select() 方法获取到 Channel，select() 方法返回的 Channel 是那些准备好的，并且你是设置为感兴趣的事件。select() 方法：

* int select() 这个方法调用后会阻塞住，直到有一个 channel 的某个你感兴趣的事件已经准备好了，才返回
* int select(long timeout) 功能和 select() 方法一样，多了一个超时时间
* int selectNow() 直接返回

select() 方法返回的是满足条件的 channel 的个数，这个个数是距离上一次调用 select() 方法直接变成 ready 的channel 的个数。

#### selectedKeys()

通过 select() 方法获取到个数后，你还不能操作 channel，因为你现在没有 channel 对象的引用，现在你需要通过 Selector.selectedKeys() 方法获取到一个 SelectionKey 集合：

    Set<SelectionKey> selectedKeys = selector.selectedKeys(); 

获取到这个集合后，你就可以遍历这个集合，代码如下：

    Set<SelectionKey> selectedKeys = selector.selectedKeys();

    Iterator<SelectionKey> keyIterator = selectedKeys.iterator();

    while(keyIterator.hasNext()) {
    
        SelectionKey key = keyIterator.next();

        if(key.isAcceptable()) {
            // a connection was accepted by a ServerSocketChannel.

        } else if (key.isConnectable()) {
            // a connection was established with a remote server.

        } else if (key.isReadable()) {
            // a channel is ready for reading

        } else if (key.isWritable()) {
            // a channel is ready for writing
        }

        keyIterator.remove();
    }

注意 remove() 方法，这个不是把 SelectionKey 从 Selector 中移除掉，只是从这个集合中移除掉，当这个 channel 下回 ready 的时候，一个 SelectionKey 会再次被添加到这个集合中，所以，remove() 是很有必要的。

#### wakeUp()

如上文所说，select() 方法是阻塞的，直到有 channel 的状态变成 ready 才会返回。如果一直没有 channel 的状态变成 ready ，那么这个方法会一直阻塞在那，这个时候，我们可以在其他线程通过调用 selector.wakeUp() 方法，让 select() 立刻返回。

#### close()

在你使用完 Selector 的时候，务必要记得调用 close() 方法。close() 方法会关闭 Selector 和 作废 SelectionKey 实例。

# 8. Java NIO FileChannel

FileChannel 提供了除了标准的 Java 文件 IO 外的另外一种读写文件的方式。

和其他 Channel 不同的是，FileChannel 不能被设置为非阻塞模式(non-blocking mode)。

### Opening a FileChannel

FileChannel 不能直接打开一个文件，需要 InputStream,OutputStream 或者 RandomAccessFile ，然后获取 Channel。

    RandomAccessFile aFile = new RandomAccessFile("data/nio-data.txt", "rw");
    FileChannel inChannel = aFile.getChannel();


### Reading Data from a FileChannel

下面是从 FileChannel 读数据的代码：

    ByteBuffer buf = ByteBuffer.allocate(48);
    int bytesRead = inChannel.read(buf);

bytesRead 的取值为 read() 方法从 channel 写入到 Buffer 的字节数量，-1 表示文件结束。

### Writing Data to a FileChannel

下面是往 FileChannel 写数据的代码：

    String newData = "New String to write to file..." + System.currentTimeMillis();

    ByteBuffer buf = ByteBuffer.allocate(48);
    buf.clear();
    buf.put(newData.getBytes());

    buf.flip();

    while(buf.hasRemaining()) {
        channel.write(buf);
    }

注意：channel.write() 并不能保证每次都把 buffer 里的数据都写入到 channel 中，所有，你需要在一个循环内，多次的调用 write() 方法，直到 buffer.hasRemaining() 返回 false，表示 buffer 内已经没有再需要被取代的数据了，说明 buffer 的数据都被写入到 channel 了，才可以退出循环。

### Closing a FileChannel

关闭一个 FileChannel，这个没有什么好说明的，用完就关，这是基本法。

### FileChannel Position

在 Java IO 中，只有 RandomAccessFile 可以做到 position 前后移动，而其他的都做不到，或者有很多限制(比如带 Buffer 的流)。而在 FileChannel 就支持这样的操作。

    long pos channel.position();
    channel.position(pos +123);

如果你把 position 移动到大于文件大小的位置，在读的时候，会获得 -1 的结果，表示文件已经结束。

如果你把 position 移动到大于文件大小的位置，并且往里写的话，新写入的内容会被写入到你指定的位置。这样的结果是，会出现文件洞。This may result in a "file hole", where the physical file on the disk has gaps in the written data.

### FileChannel Truncate

文件截断，如下的代码能把文件截断为 1024 个字节。

    channel.truncate(1024);

### FileChannel Force

FileChannel.force() 让 FileChannel 把所有还没有写入到磁盘的数据写入。一般操作系统会做一些缓冲，所以数据没有真正被写入到磁盘中。调用 force() 方法可以让数据和文件信息写入到磁盘中。

# 9. Java NIO SocketChannel

SocketChannel 用于建立 TCP 连接，SocketChannel 有两种创建的方式：

1. 直接创建一个 SocketChannel，连接到任何的网络服务
2. ServerSocketChannel 在收到连接后，也会创建一个 SocketChannel。

### 打开 SocketChannel

    SocketChannel socketChannel = SocketChannel.open();
    socketChannel.connect(new InetSocketAddress("http://jenkov.com", 80));

### 读和写

SocketChannel 的读和写都与 FileChannel 相似，基本都是一样的。

### Non-blocking Mode

SocketChannel 和 FileChannel 不一样的是，它具有非阻塞模式，在非阻塞模式下，你可以以异步的方式调用 connect(),read() 和 write()。

#### connect()

在非阻塞模式下，connect() 会立刻返回，不会等连接建立。你需要通过 finishConnect() 返回来判断连接是否建立。

    socketChannel.configureBlocking(false);
    socketChannel.connect(new InetSocketAddress("http://jenkov.com", 80));

    while(! socketChannel.finishConnect() ){
        //wait, or do something else...    
    }

#### write() and read()

在非阻塞模式中，write() 和 read() 并没有真正的数据读写，所以你需要在稍后的操作中循环的读写 buffer 中的数据。

### Non-blocking Mode with Selectors

因为 SocketChannel 有非阻塞模式，所以它是可以很好的使用在 Selector 中的。我们可以在 Selector 中注册多个 SocketChannel，然后通过一个这个 Selector 管理这些 SocketChannel。

# 10. Java NIO ServerSocketChannel

ServerSocketChannel 被使用在 TCP 连接的服务端，通过制定的端口，监听任何的连接。


### Opening a ServerSocketChannel

下面的代码是创建一个 ServerSocketChannel 实例。

    ServerSocketChannel serverSocketChannel = ServerSocketChannel.open();

在创建完一个 ServerSocketChannel 实例后，咱们需要为这个 socket server 绑定一个端口，代码如下：

    serverSocketChannel.socket().bind(new InetSocketAddress(9999));

### Listening for Incoming Connections

ServerSocketChannel.accept() 方法用来获得一个接入的连接(incoming connection)，默认的，这个方法是阻塞的，代码如下：

    while(true){
        SocketChannel socketChannel = serverSocketChannel.accept();
        //do something with socketChannel...
    }

### Non-blocking Mode

ServerSocketChannel 可以被设置为非阻塞模式，在非阻塞模式下， accept() 会立马返回，因此它很有可能会返回一个空的 SocketChannel 对象。同样的，ServerSocketChannel 是可以配合 Selector 一起友好的工作的。设置非阻塞模式的代码如下：

    serverSocketChannel.configureBlocking(false);

# 11. Java NIO: Non-blocking Server

# 12. Java NIO DatagramChannel

DatagramChannel 被用来接收和发送 UDP 数据包，因为 UDP 是无连接(connection-less)的网络协议,所以，它的读写和其他的 Channel 有些区别。

### Opening a DatagramChannel

下面是打开一个 DatagramChannel 的代码：

    DatagramChannel channel = DatagramChannel.open();
    channel.socket().bind(new InetSocketAddress(9999));


### Receiving Data

    ByteBuffer buf = ByteBuffer.allocate(48);
    buf.clear();
    channel.receive(buf);

接收数据和其他的类似，receive() 会把接收到的数据包里的内容拷贝到 Buffer 中，但是如果数据包的内容大于 Buffer 的大小，那么多出来的数据会被抛弃掉(discarded silently)，这一点需要大家注意。

### Sending Data

    String newData = "New String to write to file..."
                    + System.currentTimeMillis();
    ByteBuffer buf = ByteBuffer.allocate(48);
    buf.clear();
    buf.put(newData.getBytes());
    buf.flip();

    int bytesSent = channel.send(buf, new InetSocketAddress("jenkov.com", 80));

UDP 是一个无连接的网络协议，所以你发送的数据并不能保证接收方能否正确接收，你也不会知道这些数据发送的任何状态。

### Connecting to a Specific Address

因为 UDP 协议的特性，所以你建立一个 DatagramChannel 的时候，并不需要关心服务端是否开启并且已经准备好。因此，你完全可以任意指定一个接收地址，哪怕它真的不存在。

    channel.connect(new InetSocketAddress("jenkov.com", 80));

在初始化 DatagramChannel 后，你除了使用 receive() 和 send() 方法外，你同样也可以使用 write() 和 read() 方法，和其他的 Channel 一样。只是 DatagramChannel 并不保证数据是否正确分发。


# 13. Java NIO Pipe

管道提供了两个线程之间数据的连接和传输。一个管道包含一个 source channel 和一个 sink channel，数据从 sink channel 写入，从 source channel 被另外一个线程读出。

### Creating a Pipe

创建一个管道很简单：

    Pipe pipe = Pipe.open();

### Writing to a Pipe

在往管道里写数据前，需要先获取一个 sink channel : 

    Pipe.SinkChannel sinkChannel = pipe.sink();

在获取到 sink channel 后，就可以往里写数据了：

    String newData = "New String to write to file..." + System.currentTimeMillis();

    ByteBuffer buf = ByteBuffer.allocate(48);
    buf.clear();
    buf.put(newData.getBytes());

    buf.flip();
   
    while(buf.hasRemaining()) {
        sinkChannel.write(buf);
    }

### Reading from a Pipe

从管道中读数据，需要先获取到一个 source channel：

    Pipe.SourceChannel sourceChannel = pipe.source();

获取到 source channel 后，读取数据就跟普通 channel 相似了：

    ByteBuffer buf = ByteBuffer.allocate(48);
    int bytesRead = inChannel.read(buf);

# 14. Java NIO vs. IO

### Main Differences Betwen Java NIO and IO

下面表格展示了 NIO 和 IO 的大致区别。

![QQ图片20160408162815.png][1]

### Stream Oriented vs. Buffer Oriented

面向流和面向缓冲是 NIO 和 IO 的最大区别。

面向流意思是你一次只能从流中读一个或者多个字节的内容，它们是没有缓冲的，因此，你也不能在一个流中任意的向前或者先后移动，如果你需要向前或者向后读取，你只能自己先做一个缓冲。

而 Java NIO 是先将数据读取后写入到 Buffer 中，你可以自由的在这个 Buffer 中读取。当然，Buffer 是有大小的，意味着你也不是任意的往前和任意的往后移动的。但至少，对于 Java NIO，你直接操作的是 Buffer。

### Blocking vs. Non-blocking IO

Java IO 是阻塞的，意味着在调用 read() 或者 write() 的时候，线程会阻塞在这里的，直到数据被写入或者读出，在这个时候，线程不能做其他的事情。

Java NIO 的非阻塞模式，可以让一个线程想 channel 发起一个读取数据的请求，然后并不关心这个时候有多少数据被读取，线程可以继续执行其他的代码。非阻塞的写也是相似的，线程请求往一个 channel 里写入数据的时候，并不会等数据真正被写入。

因为读和写都可以是非阻塞的，所以一个线程可以同时处理多个 channel 的读写任务。

### Selectors

Selectors 让一个线程可以同时处理多个 channel 的数据。你们把多个 channel 注册到一个 Selector 上，然后在一个线程里，通过 Selector 的 select() 方法分别去处理各个 channel 的读或者写。

### How NIO and IO Influences Application Design

上文已经说了很多 NIO 和 IO 的区别了，已经 NIO 的使用方式，具体到应用中，就需要考虑怎么去选择和设计了。

一般来说，NIO 比较适合用在那些流量少，个数又多的场景中，比如一个聊天服务端，每个客户端并不是总是时时向服务端发送数据的，如果服务端使用 IO 的方式的话，需要给每个客户端的连接创建一个线程，一直等待客户端向服务端发送数据。而如果使用 NIO，那么服务端就可以使用一个线程或者很少的线程来完成相同的工作。

# 15. Java NIO Path

Path 在 Java 7 中被加入，Path 的完整位置为 java.nio.file.Path。但这一路径没有出现在 Android 中。一个 Path 实例表示了一个文件系统的路径，这个路径可以是绝对路径，可以是相对路径，可以是一个文件，也可以是一个目录。Path 和 java.io.File 有点相似，但又有些不一样(废话～～)

### Creating a Path Instance

下面的代码对应了 windows 和 Unix 系统下获取绝对路径 Path 的写法：

    Path path = Paths.get("c:\\data\\myfile.txt");
    Path path = Paths.get("/home/jakobjenkov/myfile.txt");

首先 Path 是一个接口，获取一个 Path 实例是通过 Paths.get() 方法，Paths.get() 就是 Path 的工厂方法。

一个相对路径的 Path 需要依赖另外一个 Path，被称为 Base Path，这个相对路径的 Path 的绝对路径就是 Base path 加上相对路径。

    Path projects = Paths.get("d:\\data", "projects");
    Path file     = Paths.get("d:\\data", "projects\\a-project\\myfile.txt");

Path 支持使用一个点 . 表示当前路径和使用两个点 .. 表示上级路径。当一个路径中存在 . 或者 .. 后，可以使用 Path.normalize() 删除掉那些路径，并且得到一个最终的绝对路径。

# 16. Java NIO Files

Java NIO Files 和 Paths 一起配合使用，提供了丰富的文件操作的 API，位于 java.nio.file 包下，但是目前同样没有出现在 Android 中。具体的 API 很简单，看看 JavaDoc 就基本 OK 了。

# 17. Java NIO AsynchronousFileChannel

AsynchronousFileChannel 在 Java 7 中被加入到 Java NIO 中。AsynchronousFileChannel 让对一个文件的异步读写可以在异步进行。

### Creating an AsynchronousFileChannel

下面的代码展示了如何创建一个 AsynchronousFileChannel 实例：

    Path path = Paths.get("data/test.xml");
    AsynchronousFileChannel fileChannel = AsynchronousFileChannel.open(path, StandardOpenOption.READ);


### Reading Data

从 AsynchronousFileChannel 读取数据有两种方式：

#### 1. Reading Data Via a Future

    AsynchronousFileChannel fileChannel = AsynchronousFileChannel.open(path, StandardOpenOption.READ);

    ByteBuffer buffer = ByteBuffer.allocate(1024);
    long position = 0;

    Future<Integer> operation = fileChannel.read(buffer, position);

    while(!operation.isDone());

    buffer.flip();
    byte[] data = new byte[buffer.limit()];
    buffer.get(data);
    System.out.println(new String(data));
    buffer.clear();

在上面的代码中， read() 方法返回了一个 Future 对象，当 Future.isDone() 返回 true 的时候，表示文件已经被读取到 Buffer 中了。当然上面只是一个例子，while true 的方式是不好的。

#### 2. Reading Data Via a CompletionHandler

第二种方式是在 read() 方法的第三个参数传递一个 CompletionHandler 实例。

    fileChannel.read(buffer, position, buffer, new CompletionHandler<Integer, ByteBuffer>() {
        @Override
        public void completed(Integer result, ByteBuffer attachment) {
            System.out.println("result = " + result);

            attachment.flip();
            byte[] data = new byte[attachment.limit()];
            attachment.get(data);
            System.out.println(new String(data));
            attachment.clear();
        }

        @Override
        public void failed(Throwable exc, ByteBuffer attachment) {
    
        }
    });

在上面的代码中，一旦读的操作完成的时候，completed() 方法会被调用，剩余的代码和上一种方式就大概相同了。

### Writing Data

写数据和读数据一样，也有两种方式，一种是通过 Future，一种也是实现 CompletionHandler。



# 18. 总结

历时 2 天，基本上完整得看完了 Jenkov 的文章，也顺便记录下了上面的内容，感觉收获是很大的，特别是感觉顺着文章一路往下学习，整个知识更加清晰明了了。相信如果你也看完一遍，你也可以有很清晰的理解。

最后结合 Android，个人认为 NIO 在 Android 上使用可能并不是很多，即使有也是在网络请求那部分，而这一部分基本上市面上主流的开源框架都集成好了，如果需要深入理解的话，可以去看看他们怎么实现，反正咱们在项目中基本上是不大可能需要直接面对 NIO 了。

对于文件操作，因为 FileChannel 是阻塞的，所以他的用处可能出现在对文件的读写上了，特别是小数阅读类的应用，FileChannel 的面向 Buffer 的机制是很有必要的。当然 RandomAccessFile 也可能能够胜任。

而文章后面的 Path，Files 和 AsynchronousFileChannel 并没有出现在 Android 中，目前还不知道怎么个支持方式。


  [1]: http://www.binkery.com/usr/uploads/2016/04/2141700526.png