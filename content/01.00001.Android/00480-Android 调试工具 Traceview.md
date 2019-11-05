# Android 调试工具 Traceview
- 2016-03-22 04:07:50
- 
- 

<!--markdown--># Android 调试工具 Traceview

Traceview 是　Android 调试性能的一个好工具。
Traceview is a graphical viewer for execution logs that you create by using the Debug class to log tracing information in your code. Traceview can help you debug your application and profile its performance.


<!--more-->


## Traceview 界面

Traceview 界面主要有两个部分

* 时间线面板　Timeline panel

 describes when each thread and method started and stopped

* 性能面板 Profile panel 

 provides a summary of what happened inside a method

## Timeline Panel
时间线面板显示了在统计开始到统计结束这段时间内，所有 Java 线程分别使用的 CPU 时间。每个线程一行，每行都是密密麻麻的五颜六色的色块，每个色块表示一个方法执行的时间。可以放大时间线，选中某个色块的时候，Profile Panel 也会定位到这个色块对应的方法的数据上。

## Profile Panel

Profile Panel 的每一行显示一个方法的调用信息。点开每个方法名前的小三角后，显示　Parents 和　Children .　Parents 是这个方法的父方法，也就是调用这个方法的方法。Children 里是这个方法里调用的方法。这样可以一路追下去，找到计算量最大的方法。

Profile Panel 的每一行有很多信息，每个信息都什么意思呢。下面是每列的说明。

* Name 方法名字
* Incl Cpu Time　该方法占用的 CPU 时间，包括它的子方法。
* Excl Cpu Time　该方法占用的　CPU 时间，不包括它调用的子方法。
* Incl Real Time　该方法运行的真实时间，包括它的子方法。
* Excl Real Time　该方法运行的真实时间，不包括它的子方法。
* Call+Recur Calls/Total　该方法被调用的次数和递归调用的次数／总调用次数
* Cpu Time/Call　该方法占用的 CPU 时间除以调用次数，得到平均每次占用的时间。
* Real Time/Call　该方法运行的真实时间除以调用次数，得到每次运行的平均时间。

## 使用方法
Traceview 只是一个分析数据的工具，收集数据需要其他的工具来帮助。Android 一共提供了两种方法来收集数据。
### DDMS 
我们可以在　DDMS 里，当你选中某个应用程序的时间，有个　Start Method Profiling 的按钮可以点击。点击就开始收集数据，这个按钮会变成　Stop ,点击 Stop 结束收集，然后 Traceview 就自动弹出来了。
### 代码收集
通过工具收集就考验手的速度了，其实手再快也难免引入一大堆没用的数据。在代码里收集是最好的，Android 提供两个方法来干这个事情。

    Debug.startMethodTracing(String traceName)
    Debug.stopMethodTracing()


traceName 的说明：
>Name for the trace log file to create. If traceName is null, this value defaults to "/sdcard/dmtrace.trace". If the files already exist, they will be truncated. If the trace file given does not end in ".trace", it will be appended for you.

在开始和结束的地方分别加入这两个方法，收集的数据会被写到文件里，然后你需要把文件从手机上扒下来，用 Traceview 打开。[adb pull 的使用](http://www.binkery.com/archives/424.html)
另外你需要有 sdcard 的写权限。

Traceview 在 SDK 的 tools 目录下，可以使用下面的方法打开文件。

    traceview tracefile

## 已知问题
在线程的处理上会碰见一些问题。
Traceview logging does not handle threads well, resulting in these two problems:

* If a thread exits during profiling, the thread name is not emitted;
* The VM reuses thread IDs. If a thread stops and another starts, they may get the same ID.