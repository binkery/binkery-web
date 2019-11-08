# Andriod 的 Java 虚拟机
- Android,java,虚拟机,
- 2019-05-05 13:17:32

Dalvik ：Android 一开始选中的 Java 虚拟机，其实 Dalvik 不是一个标准的 Java 虚拟机，根据定义，Java 虚拟机是以加载 class 文件的虚拟机，但是 Dalvik 加载的是 dex 文件。虽然他们都是通过 Java 编写，并且最终编译的，但是最终还是不相认的。Dalvik 并不能直接加载 class 文件，所以我们需要打包成 dex 文件，然后才能发布到 Android 设备上。当然，这些事都有 ADT 帮开发者完成了。

ART : Android Runtime . 从 Android 4.4 起，Google 提供了新的虚拟机。Google 认为，Dalvik 并不是很高效，他们觉得需要更高效的虚拟机，Android 在研发的时候，被 Google 收购的时候，还没有 iOS 什么事，所以 Dalvik 是一个不错的选择，但是 iOS 确实比 Android 流畅多了，于是有了 ART。在 4.4 ，ART 作为开发者选项的可以被打开，5.0 的时候就成了默认的虚拟机了。

## ART 采用提前编译 Ahead-of-time (AOT) compilation

对于开发者，app 运行在 Dalvik 还是 ART 可能并不用关心，因为 Google 帮你做到了。在发布的时候，还是以 dex 的形式发布，被打包成 apk 文件，被用户下载。在安装的时候，ART 会把 dex 文件转成 oat 文件。有一个工具叫 dex2oat 。（At install time, ART compiles apps using the on-device dex2oat tool. ）。可以看出，使用 ART 的话，在安装的时候会被之前慢一些。

## 提高垃圾回收效率 Improved garbage collection
垃圾回收（Garbage collection）会影响到 app 的性能。因为当垃圾回收线程工作的时候，其他线程是被暂停的。

ART 通过下面的办法提高 GC 效率

 * One GC pause instead of two
 * Parallelized processing during the remaining GC pause
 * Collector with lower total GC time for the special case of cleaning up recently-allocated, short-lived objects
 * Improved garbage collection ergonomics, making concurrent garbage collections more timely, which makes GC_FOR_ALLOC events extremely rare in typical use cases
 * Compacting GC to reduce background memory usage and fragmentation
 
## 开发和调试的效率提高 Development and debugging improvements

### 更高效的 Trace

一般开发者会使用 Traceview 工具来分析代码的执行效率。当 Traceview 工具 在收集信息的时候，每个方法的调用都需要 Dalvik 付出额外的工作，导致 app 的运行会变慢。而且就我个人的经验，经常会失败，因为虚拟机需要把每个方法调用的一些信息记录下来，最终写到 trace 文件里。但是在 ART 上，Traceview 并不会让 app 的运行变慢。

ART 还提供了更多的调试选择。

 * See what locks are held in stack traces, then jump to the thread that holds a lock.
 * Ask how many live instances there are of a given class, ask to see the instances, and see what references are keeping an object live.
 * Filter events (like breakpoint) for a specific instance.
See the value returned by a method when it exits (using “method-exit” events).
 * Set field watchpoint to suspend the execution of a program when a specific field is accessed and/or modified.

### 更详细的异常堆栈信息
 
Improved diagnostic detail in exceptions and crash reports

比如空指针，如果是 ART ，log 会告诉你哪个引用是空的，而 Dalvik 最多只告诉你是哪一行出现了空指针。
包括其他的错误，ART 会提供比之前更加详细的信息，帮助开发者调试。

## 怎么查看设备运行的虚拟机

    System.getProperty("java.vm.version")
    
If ART is in use, the property's value is "2.0.0" or higher.
