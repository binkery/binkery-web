# Android Activity生命周期
- 2015-09-03 08:32:53
- Android
- android,activity,生命周期,进程,

<!--markdown-->Android Activity 的生命周期，以及系统何时会回收他们。


<!--more-->


1. Android用Activity Stack来管理多个Activity，所以呢，同一时刻只会有最顶上的那个Activity是处于active或者running状态。其它的Activity都被压在下面了。

2. 如果非活动的Activity仍是可见的（即如果上面压着的是一个非全屏的Activity或透明的Activity），它是处于paused状态的。在系统内存不足的情况下，paused状态的Activity是有可被系统杀掉的。只是不明白，如果它被干掉了，界面上的显示又会变成什么模样？看来下回有必要研究一下这种情况了。

3. 几个事件的配对可以比较清楚地理解它们的关系。Create与Destroy配成一对，叫entrie lifetime，在创建时分配资源，则在销毁时释放资源；往上一点还有Start与Stop一对，叫visible lifetime，表达的是可见与非可见这么一个过程；最顶上的就是Resume和Pause这一对了，叫foreground lifetime，表达的了是否处于激活状态的过程。

4. 因此，我们实现的Activity派生类，要重载两个重要的方法：onCreate()进行初始化操作，onPause()保存当前操作的结果。


## 进程的生命周期 Process Lifecycle 

除了Activity Lifecycle以外，Android还有一个Process Lifecycle的说明：在内存不足的时候，Android是会主动清理门户的，那它又是如何判断哪个process是可以清掉的呢？文档中也提到了它的重要性排序：

1. 最容易被清掉的是empty process，空进程是指那些没有Activity与之绑定，也没有任何应用程序组件（如Services或者IntentReceiver）与之绑定的进程，也就是说在这个process中没有任何activity或者service之类的东西，它们仅仅是作为一个cache，在启动新的 Activity时可以提高速度。它们是会被优先清掉的。因此建议，我们的后台操作，最好是作成Service的形式，也就是说应该在Activity中启动一个Service去执行这些操作。

2. 接下来就是 background activity 了，也就是被 stop 掉了那些 activity 所处的 process，那些不可见的 Activity被清掉的确是安全的，系统维持着一个 LRU列表，多个处于background的activity都在这里面，系统可以根据 LRU 列表判断哪些 activity 是可以被清掉的，以及其中哪一个应该是最先被清掉。不过，文档中提到在这个已被清掉的Activity又被重新创建的时候，它的 onCreate 会被调用，参数就是onFreeze时的那个Bundle。不过这里有一点不明白的是，难道这个Activity被killed时，Android 会帮它保留着这个 Bundle 吗？

3. 然后就轮到 service process 了，这是一个与 Service 绑定的进程，由 startService 方法启动。虽然它们不为用户所见，但一般是在处理一些长时间的操作（例如MP3的播放），系统会保护它，除非真的没有内存可用了。

4. 接着又轮到那些 visible activity 了，或者说 visible process。前面也谈到这个情况，被 Paused 的 Activity 也是有可能会被系统清掉，不过相对来说，它已经是处于一个比较安全的位置了。

5. 最安全应该就是那个 foreground activity了，不到迫不得已它是不会被清掉的。这种 process 不仅包括 resume 之后的Activity，也包括那些 onReceiveIntent 之后的 IntentReceiver 实例。

在Android Activity生命周期的讨论中，文档也提到了一些需要注意的事项：因为Android应用程序的生存期并不是由应用本身直接控制的，而是由 Android系统平台进行管理的，所以，对于我们开发者而言，需要了解不同的组件Activity、Service和IntentReceiver的生命，切记的是：如果组件的选择不当，很有可能系统会杀掉一个正在进行重要工作的进程。