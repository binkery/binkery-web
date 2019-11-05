# Android Intent 的解析
- 2016-03-22 02:41:42
- 
- 

<!--markdown--># Android Intent 的解析

在应用中，我们可以以两种形式来使用Intent：

<!--more-->

## 两种分类

 - 显式 Intent：明确的指定 component 的名字，也就是完整的包名 + 类名。可以通过 setComponent(ComponentName) 或者setClass(Context, Class) 来指定。通过指定具体的组件类，通知应用启动对应的组件。

> Explicit intents specify the component to start by name (the fully-qualified class name). You'll typically use an explicit intent to start a component in your own app, because you know the class name of the activity or service you want to start. For example, start a new activity in response to a user action or start a service to download a file in the background.

 - 隐式 Intent：没有指定 component 属性的Intent。这些Intent需要包含足够的信息，这样系统才能根据这些信息，在所有的可用组件中，确定满足此Intent的组件。

> Implicit intents do not name a specific component, but instead declare a general action to perform, which allows a component from another app to handle it. For example, if you want to show the user a location on a map, you can use an implicit intent to request that another capable app show a specified location on a map.

## 理解
我们可以这样理解 Intent ,我们假设有一个班级，班级每个人的名字都是唯一的，没有重名的。于是老师叫"小明童鞋起来回答问题"，这就是一个显示的　Intent ,老师向小明童鞋发送了一个命令。如果老师说"来一个力气大的男生帮忙搬桌子"，那么每个力气大的男生都是备选的方案，但是最后只能有一个被选中去搬桌子，所有力气大的男生都站起来了，然后老师再选一个去搬桌子。在　Android 系统里，系统就会弹出一个框，让用户选择某一个组件来响应这个命令。


## 显示 Intent
对于显式 Intent，Android 不需要去做解析，因为目标组件已经很明确，Android 需要解析的是那些隐式 Intent，通过解析将 Intent 映射给可以处理此 Intent 的 Activity、Service 或 Broadcast Receiver。

## 隐式 Intent

Intent 解析机制主要是通过查找已注册在 AndroidManifest.xml 中的所有 <intent-filter> 及其中定义的 Intent，通过PackageManager（注：PackageManager 能够得到当前设备上所安装的
application package 的信息）来查找能处理这个 Intent 的 component。在这个解析过程中，Android 是通过 Intent 的action、type、category 这三个属性来进行判断的，判断方法如下：

 - 如果 Intent 指明定了 action，则目标组件的 IntentFilter 的 action 列表中就必须包含有这个 action，否则不能匹配；
 - 如果 Intent 没有提供 type ，系统将从 data 中得到数据类型。和 action一样，目标组件的数据类型列表中必须包含Intent的数据类型，否则不能匹配。
 - 如果 Intent 中的数据不是 content:类型的URI，而且 Intent 也没有明确指定 type，将根据 Intent 中数据的scheme（比如 http:或者mailto:）进行匹配。同上，Intent 的 scheme 必须出现在目标组件的 scheme 列表中。
 - 如果 Intent 指定了一个或多个 category，这些类别必须全部出现在组建的类别列表中。比如 Intent 中包含了两个类别：LAUNCHER\_CATEGORY 和 ALTERNATIVE\_CATEGORY，解析得到的目标组件必须至少包含这两个类别。

[Android Intent 和 Intent Filter](http://blog.binkery.com/android/intent/summary.html)