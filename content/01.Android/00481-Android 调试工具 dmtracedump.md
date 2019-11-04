# Android 调试工具 dmtracedump
- 2016-03-22 04:06:12
- 
- 

<!--markdown--># Android 调试工具 dmtracedump

dmtracedump 是 Android 提供的另一个调试工具，与 Traceview 区别的是，它是把信息以一个树形的图形展现出来。


<!--more-->

> dmtracedump is a tool that gives you an alternate way of generating graphical call-stack diagrams from trace log files. The tool uses the Graphviz Dot utility to create the graphical output, so you need to install Graphviz before running dmtracedump.
>
> The dmtracedump tool generates the call stack data as a tree diagram, with each call represented as a node. It shows call flow (from parent node to child nodes) using arrows. 


数据的收集与 Traceview 相同，通过在代码里添加调试代码，输出 .trace ,然后使用 dmtracedump 输出一个图形文件，恩，png 格式的，如果你调试信息多的话，这个 png 文件是会很大很大的，对，就是这样子。

dmtracedump 需要使用到另外一个工具，Graphviz Dot，所有在使用 dmtracedump 前需要确认 Graphviz Dot 已经安装。
