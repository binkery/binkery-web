# Android 进程的生命周期 Processes and Application Life Cycle
- 2016-04-20 01:28:24
- Android
- 

<!--markdown--># Android 进程的生命周期 Processes and Application Life Cycle

每个 Android 应用都运行在自己的 Linx 进程里，这篇文章主要介绍进程和应用程序的生命周期。官方文档的原文地址：<http://developer.android.com/guide/topics/processes/process-lifecycle.html> 。这里只做了简单的翻译已经我的一些理解。[20150825更新：这个页面可能被更新了，请尽可能查看原文]


<!--more-->

## Android 进程

大部分情况下，每个 Android 应用运行在自己的 Linux 进程里。当应用程序的代码需要被执行的时候，进程被创建，并且一直运行，直到它不再被需要并且系统需要回收内存给其他应用程序使用的时候。

> In most cases, every Android application runs in its own Linux process. This process is created for the application when some of its code needs to be run, and will remain running until it is no longer needed and the system needs to reclaim its memory for use by other applications.

Android 应用程序的进程不受自己管理，而是由系统来判断这个进程是否应用存在，是否需要被 kill 掉，内存是否需要被回收。

> An unusual and fundamental（基本的） feature of Android is that an application process's lifetime is not directly controlled by the application itself. Instead, it is determined by the system through a combination of the parts of the application that the system knows are running, how important these things are to the user, and how much overall memory is available in the system.

Android 的基本组件一定程度上影响了一个应用程序的进程，如果使用不当的话，应用程序会可能意外得被系统 kill 掉。

> It is important that application developers understand how different application components (in particular Activity, Service, and BroadcastReceiver) impact the lifetime of the application's process. Not using these components correctly can result in the system killing the application's process while it is doing important work.

例如，BroadcastReceiver 在接收到广播的时候，系统会创建一个进程，然后执行 BroadcastReceiver.onReceive() ，在方法结束后，系统认为这个进程该做的事已经做完了，随时看不顺眼分分钟把它 kill 掉。如果你在 onReceive() 方法里创建了一个进程，那么……线程跑着跑着，host process 没了！！！WTF！ 所以 BroadcastReceiver 里是不建议创建线程去执行任务的，一般会把这个任务交给 Service 去做。具体的可以参考 BroadcastReceiver 的文档。

> A common example of a process life-cycle bug is a BroadcastReceiver that starts a thread when it receives an Intent in its BroadcastReceiver.onReceive() method, and then returns from the function. Once it returns, the system considers the BroadcastReceiver to be no longer active, and thus, its hosting process no longer needed (unless other application components are active in it). So, the system may kill the process at any time to reclaim memory, and in doing so, it terminates the spawned thread running in the process. The solution to this problem is to start a Service from the BroadcastReceiver, so the system knows that there is still active work being done in the process.

## 进程的优先级

在系统内存不够用的时候，系统是按照优先级去 kill 进程，回收内存的。从而保证了系统的其他应用程序正常运行。

> To determine which processes should be killed when low on memory, Android places each process into an "importance hierarchy" based on the components running in them and the state of those components. These process types are (in order of importance):

### 1. foreground process

foreground process，前台进程，优先级最高的进程，一个进程有下面几个方式让自己变成前台进程

> A foreground process is one that is required for what the user is currently doing. Various application components can cause its containing process to be considered foreground in different ways. A process is considered to be in the foreground if any of the following conditions hold:

* 当一个进程的某个 Activity 运行在屏幕的最顶端的时候，也就是 onResume() 被调用的时候。
用户正在和它进行交互。这个很好理解，用户正刷着微博呢，微博被系统关了，这样以后还怎么一起玩耍！It is running an Activity at the top of the screen that the user is interacting with (its onResume() method has been called).

* Service 的生命周期方法被回调的时候。
> It has a Service that is currently executing code in one of its callbacks (Service.onCreate(), Service.onStart(), or Service.onDestroy()).

* 当这个进程的一个 Service 被用户当前正在使用的 Activity 绑定的时候。
> It hosts a Service that's bound to the activity that the user is interacting with.

* 当这个进程的一个 Service 的 startForeground() 方法被调用的时候。
> It hosts a Service that's running "in the foreground"—the service has called startForeground().

* 当这个进程的一个 BroadcastReceiver 的 onReceive() 被回调的时候。
Android 分配给 BroadcastReceiver 执行的时间本来就不多，让它优先级高的也可以理解嘛。其实 BroadcastReceiver 确实需要比较高的权限，你想想，一个信息在系统里广播，系统得赶紧给广播的接收者们较高的权限，让它们赶紧处理掉，并且每个接收者分配的时间不能太长。如果不这样呢，接收者没有优先级去处理，要么广播信息一个接一个在系统里放着，要么就扔掉，两个都不合适，所以只能给 BroadcastReceiver 高优先级，让它们赶紧把自己的包裹从传达室拿走，不然大爷要生气了。It has a BroadcastReceiver that is currently running (its BroadcastReceiver.onReceive() method is executing).

foreground 优先级的总是少数的，一般情况下，系统不会去 kill 掉这样的进程，除非系统的内存实在太 low 了，该换手机了，少年。

> There will only ever be a few such processes in the system, and these will only be killed as a last resort if memory is so low that not even these processes can continue to run. Generally, at this point, the device has reached a memory paging state, so this action is required in order to keep the user interface responsive.

### 2. visible process 

可见的进程。有一个 Activity 可见，但不是在最顶端。比如系统弹了一个对话框。一般这样的进程也是很重要的，虽然这个时候没有和用户交互，但是用户还是可以看得见的，而且一般用户很快会回到这个进程的。用户正刷着微博呢，突然弹了框提示收到一条代开发票的短信，然后微博被回收了，这样也不好吧。

> A visible process is one holding an Activity that is visible to the user on-screen but not in the foreground (its onPause() method has been called). This may occur, for example, if the foreground Activity is displayed as a dialog that allows the previous Activity to be seen behind it. Such a process is considered extremely important and will not be killed unless doing so is required to keep all foreground processes running.

* 一个进程的某个 Activity 不在前台，但是依旧可见的时候。
> It hosts an Activity that is not in the foreground, but is still visible to the user (its onPause() method has been called). This might occur, for example, if the foreground activity started a dialog, which allows the previous activity to be seen behind it.

* 一个进程的某个 Service 绑定到某个可见的或者前台的 Activity 的时候。
> It hosts a Service that's bound to a visible (or foreground) activity.

这里有个比较不好理解的是，一个 Service 被一个 可见的或者前台的 Activity 绑定的时候，这个 Service 所在进程是前台进程还是可见进程？我的理解是这样的：如果 Activity 只绑定了一个 Service，获得一个 Binder 对象，这个时候 Service 所在的进程是可见进程。当 Activity 调用了 Binder 的方法，Service 对应的方法被调用的时候，Service 所在的进程被提升到前台进程。

### 3. service process 

service process ， 拥有一个通过 startService() 被启动的 Service的进程。虽然用户看不见它们，但是它们做了一些跟用户很重要的事情，如果播放音乐，或者上传下载文件。

> A service process is one holding a Service that has been started with the startService() method. Though these processes are not directly visible to the user, they are generally doing things that the user cares about (such as background mp3 playback or background network data upload or download), so the system will always keep such processes running unless there is not enough memory to retain all foreground and visible process.

### 4. background process

background process ， 拥有一个对用户不可见的 Activity 的进程。系统为了保证前面那三种进程正常运行，会随时 kill 这样的 background 进程。如果内存足够的情况下，系统里保留了很多这样的进程，它们以 LRU 的规则被系统缓存着。其实系统还是很仁慈的，内存是要被尽可能地利用的，只有不够的时候才回去回收的。

> A background process is one holding an Activity that is not currently visible to the user (its onStop() method has been called). These processes have no direct impact on the user experience. Provided they implement their Activity life-cycle correctly (see Activity for more details), the system can kill such processes at any time to reclaim memory for one of the three previous processes types. Usually there are many of these processes running, so they are kept in an LRU list to ensure the process that was most recently seen by the user is the last to be killed when running low on memory.

### 5. empty process

empty process，空进程，也就是这个进程里没有任何活动的组件。它们的存在只有一个理由，有钱任性，内存多，还没有需要回收这些小玩意的时候。

> An empty process is one that doesn't hold any active application components. The only reason to keep such a process around is as a cache to improve startup time the next time a component of its application needs to run. As such, the system will often kill these processes in order to balance overall system resources between these empty cached processes and the underlying kernel caches.

## 等级确定的规则

一个应用程序的多个组件处于不同的生命周期，也就有不同的等级，那么这个进程的等级以最高的那个为准。

> When deciding how to classify a process, the system will base its decision on the most important level found among all the components currently active in the process. See the Activity, Service, and BroadcastReceiver documentation for more detail on how each of these components contribute to the overall life-cycle of a process. The documentation for each of these classes describes in more detail how they impact the overall life-cycle of their application.

如果一个进程被另外一个进程依赖，那么它的等级会提高到被它依赖的进程相同的等级。如果我有个应用，需要另外一个进程提供地图导航服务，如果地图导航服务的进程没有跟我当前这个应用相同等级的话，万一它被 kill 了怎么办？怎么玩？

> A process's priority may also be increased based on other dependencies a process has to it. For example, if process A has bound to a Service with the Context.BIND_AUTO_CREATE flag or is using a ContentProvider in process B, then process B's classification will always be at least as important as process A's.

WTF！写文章的过程中被中断了几次，结果提交的时候没有保存上，害我又重头翻译了一遍！多么痛苦的领悟啊！！！


[Android 进程间的通信](http://www.binkery.com/archives/489.html)

## 写在最后

发现最近的文档又多出了下面一段话（不确定是否我之前遗漏的还是最近新加进来的）

下面这段话的大概意思是，Service 一般来说有比 Activity 更高的等级。Activity 不可见的时候，一下子被丢到了 background process 的等级，而 Service 被 start 后，没有了 Activity 的绑定和调用的话，如果 Service 还有上传下载或者播放音乐类似的事情正在做的话，它会在 service process 这个等级。

> Because a process running a service is ranked higher than a process with background activities, an activity that initiates a long-running operation might do well to start a service for that operation, rather than simply create a worker thread—particularly if the operation will likely outlast the activity. For example, an activity that's uploading a picture to a web site should start a service to perform the upload so that the upload can continue in the background even if the user leaves the activity. Using a service guarantees that the operation will have at least "service process" priority, regardless of what happens to the activity. This is the same reason that broadcast receivers should employ services rather than simply put time-consuming operations in a thread.