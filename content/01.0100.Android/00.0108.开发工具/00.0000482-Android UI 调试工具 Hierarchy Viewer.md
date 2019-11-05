# Android UI 调试工具 Hierarchy Viewer
- 2016-03-22 04:02:38
- 
- 

<!--markdown--># Android UI 调试工具 Hierarchy Viewer

Hierarchy Viewer 是 Android SDK 提供的，用来调试 UI 的工具，它位于 sdk 的 tools 目录下。


<!--more-->


> The Hierarchy Viewer application allows you to debug and optimize your user interface. It provides a visual representation of the layout's View hierarchy (the View Hierarchy window) with performance information for each node in the layout, and a magnified view of the display (the Pixel Perfect window) to closely examine the pixels in your layout.

Hierarchy Viewer　主要分两部分，View Hierarchy window　和　Pixel Perfect window.

现在在使用的时候会出现这样的提示，这是因为在连接的手机上没有获得到　view server 的信息。view server 是安装在手机端的一个服务，如果没有这个服务，Hierarchy Viewer　是没有办法连接成功的。

    The standalone version of hieararchyviewer is deprecated.
    Please use Android Device Monitor (tools/monitor) instead.

在文档上有这么一句话："To preserve security, Hierarchy Viewer can only connect to devices running a developer version of the Android system."。只有在开发版的 Android 设备上才有这样的功能。坑爹啊～

如果使用　tools/monitor 的话，其实和传说中的 hieararchyviewer 还是差别挺大的。


## View Hierarchy window
View Hierarchy window　打开后会有四个面板。四个面板上显示了非常丰富的信息。
* Tree View
Use Tree View to examine individual View objects and see the relationships between View objects in your UI.
以一个树形结构展示 UI 上 View 的关系。

* Tree Overview
Use Tree Overview to identify the part of the view tree that is being displayed in Tree View.
Tree View 的每个节点都是一个单独的 View ,当你选中某个节点的时候，就会显示这个 View 的一些信息。
    1. View class:View 的类名，比如　Button,TextView
    2. View object address : 地址
    3. View Object ID : andorid:id 的值
    4. Performance indicators : 这里会有三个颜色的小点点，三个分别代表　measure,layout,draw 的性能。绿色表示比树上的其他View快50%,黄色表示比其他的慢50%，红色表示这个 View 是整个树上最慢的。
    5. View index : 这个View在父级容器的索引位置。

* Properties View
With Properties View, you can examine all the properties without having to look at your application source.
显示了每个 View 对象的具体属性。
* Layout View
这个没啥好说的。

## Optimizing with View Hierarchy

> View Hierarchy also helps you identify slow render performance. You start by looking at the View nodes with red or yellow performance indicators to identify the slower View objects. As you step through your application, you can judge if a View is consistently slow or slow only in certain circumstances.
>
> Remember that slow performance is not necessarily evidence of a problem, especially for ViewGroup objects. View objects that have more children and more complex View objects render more slowly.
> 
> The View Hierarchy window also helps you find performance issues. Just by looking at the performance indicators (the dots) for each View node, you can see which View objects are the slowest to measure, layout, and draw. From that, you can quickly identify the problems you should look at first.

Performance indicators 是我们最应该关心的一个信息，这样我们可以找出在哪个控件上浪费的最多的运算。
另外树形结构也让我们很容易发现 UI 的布局是否过于冗余，嵌套是否过多。

## Pixel Perfect window

Pixel Perfect window 的最大作用就是以像素级的界面展示你渲染的 UI 是否复合产品经理或者视觉设计师的需求。字体大小，显示区域。这是像素级的，这个工具的最大作用就是程序猿和产品经理吵架的导火索。

你丫的，跟你说了多少遍了，这个按钮再往左挪一像素，你！到！现！在！还！没！有！给！我！挪！

就是这样子。
