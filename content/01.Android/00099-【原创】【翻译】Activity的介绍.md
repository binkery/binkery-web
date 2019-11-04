# 【原创】【翻译】Activity的介绍
- 2015-03-06 07:54:52
- Android
- android,activity,翻译,原创,

<!--markdown-->Activity 是 Android 系统里非常重要也非常基本的一个组件，下面的内容来自于 Android 的官方文档，本人做了简单的翻译。本人英语水平巨菜，做这件事情一是为了学习 Android，二是为了学习英语。

【Activity的官方文档的简单翻译，本人英语四级没过，参考需谨慎！！！】


<!--more-->


> An Activity is an application component that provides a screen with which users can interact in order to do something, such as dial the phone, take a photo, send an email, or view a map.

Activity是application的一个组成部分，它给用户（users）提供(provides)一个窗口(screen)用来做一些事情。比如拨打电话，看照片，发送邮件或者显示一张地图。

> Each activity is given a window in which to draw its user interface.

每个Activity都提供一个窗口用来渲染用户交互界面（user interface 也就是 UI）。

> The window typically fills the screen, but may be smaller than the screen and float on top of other windows.

这个窗口一般（typically）是填充满整个屏幕的，但也有一些比较小的screen浮动（float）在其他的windows上面。

> An application usually consists of multiple activities that are loosely bound to each other.

一般一个应用（application）由多个Activity组成，这些Activity是相对比较独立的。

> Typically, one activity in an application is specified as the "main" activity, which is presented to the user when launching the application for the first time.

一般情况下，有一个Activity被指定为主活动（main activity）,这个main activity会在应用第一次启动的时候被呈现（present）出来。

> Each activity can then start another activity in order to perform different actions.
每一个activity可以启动其他的activity用来执行（perform）不同的动作。

> Each time a new activity starts, the previous activity is stopped, but the system preserves the activity in a stack (the "back stack").

每一次一个新的activity启动(start)，当前的activity会停止(stop),但是这个被停止的activity会被保存（preserves）到一个栈(stack)里面。

> When a new activity starts, it is pushed onto the back stack and takes user focus.

当一个新的activity启动（start），它会被push到栈里，并且获得用户的焦点。

> The back stack abides to the basic "last in, first out" queue mechanism, so, when the user is done with the current activity and presses the BACK key, it is popped from the stack (and destroyed) and the previous activity resumes. (The back stack is discussed more in the Tasks and Back Stack document.)

这个back stack遵守(abide)栈的基本机制，后进先出(last in, first out)，所以，当用户在当前的activity上点击（presses）后退键（BACK key）,当前的activity就会被从栈里popped出来并且可能被销毁（destroy），然后之前的那个activity被会恢复(resume)。

> When an activity is stopped because a new activity starts, it is notified of this change in state through the activity's lifecycle callback methods.

当一个activity因为一个新的activity启动而被停止，这个activity会被通知(notified被通知)这个状态的改变通过activity的生命周期（lifecycle）的回调方法(callback method)。

> There are several callback methods that an activity might receive, due to a change in its state—whether the system is creating it, stopping it, resuming it, or destroying it—and each callback provides you the opportunity to perform specific work that's appropriate to that state change. For instance, when stopped, your activity should release any large objects, such as network or database connections.

activity有多个回调方法，是因为不同的状态的改变 - 不管是系统正在创建它，停止它，恢复它，或者销毁它 - 这些回调方法提供给你（开发者）一个机会(opportunity)用来执行（perform）一些特殊(specific)的工作,适当地适应状态的变化。比如，当被停止，你的activity应用释放（release）一些大的对象(large object)，比如网络(network)或数据库(database)的连接(connection)。

> When the activity resumes, you can reacquire the necessary resources and resume actions that were interrupted. These state transitions are all part of the activity lifecycle.

当一个activity被恢复(resume)，你可以再次请求(reacquire)必要(necessary)的资源(resource)和接续执行(resume)刚才被中断(interrupted)的动作(action)。状态的转变只是activity生命周期（lifecycle）的一部分(all part of)。