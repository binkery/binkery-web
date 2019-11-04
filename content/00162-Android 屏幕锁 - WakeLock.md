# Android 屏幕锁 - WakeLock
- 2014-12-18 03:00:53
- Android
- android,powermanager,wakelock,屏幕,

<!--markdown-->## PowerManager
android.os.PowerManager
PowerManager 是用来管理设备的电源状态的类。下面是官方文档

>This class gives you control of the power state of the device.
>
>Device battery life will be significantly affected by the use of this API. Do not acquire WakeLocks unless you really need them, use the minimum levels possible, and be sure to release it as soon as you can.
>
>You can obtain an instance of this class by calling Context.getSystemService().
>
>The primary API you'll use is newWakeLock(). This will create a PowerManager.WakeLock object. You can then use methods on this object to control the power state of the device.

Wake Lock是一种锁的机制, 只要有人拿着这个锁,系统就无法进入休眠,可以被用户态程序和内核获得. 这个锁可以是有超时的或者是没有超时的,超时的锁会在时间过去以后自动解锁. 如果没有锁了或者超时了, 内核就会启动休眠的那套机制来进入休眠.

PowerManager.WakeLock 有加锁和解锁两种状态，加锁的方式有两种，一种是永久的锁住，这样的锁除非显式的放开，是不会解锁的，所以这种锁用起来要非常的小心。第二种锁是超时锁，这种锁会在锁住后一段时间解锁。在创建了 PowerManager.WakeLock 后，有两种机制，第一种是不计数锁机制，另一种是计数锁机制。可以通过PowerManager.WakeLock.setReferenceCounted(boolean value) 来指定，一般默认为计数机制。这两种机制的区别在于，前者无论 acquire() 了多少次，只要通过一次 release()即可解锁。而后者正真解锁是在（ --count == 0 ）的时候，同样当 (count == 0) 的时候才会去申请加锁，其他情况 isHeld 状态是不会改变的。所以 PowerManager.WakeLock 的计数机制并不是正真意义上的对每次请求进行申请／释放每一把锁，它只是对同一把锁被申请／释放的次数进行了统计再正真意义上的去操作。

## 获取锁的方式

    public PowerManager.WakeLock newWakeLock (int flags, String tag)

## Flags

Android 总共定义了四个 Flags , 你只需要其中的一个，现实上现在只有 PARTIAL_WAKE_LOCK 没有过期，其他的可以使用 FLAG_KEEP_SCREEN_ON 代替。

 - PARTIAL_WAKE_LOCK : CPU 运转，屏幕和键盘灯关闭
 - SCREEN_DIM_WAKE_LOCK ： 已过期（API 17） CPU 运转，屏幕亮但是比较暗，键盘灯关闭 
 - SCREEN_BRIGHT_WAKE_LOCK ： 已过期（API 13）CPU 运转，屏幕高亮，键盘灯关闭
 - FULL_WAKE_LOCK ：已过期（API 17） 完全唤醒，CPU 运转，屏幕高亮，键盘灯亮

如果使用的是 PARTIAL_WAKE_LOCK 这个 Flag,，那么下面有另外两个 Flag 可以和它一起使用。

 - ACQUIRE_CAUSES_WAKEUP
Normal wake locks don't actually turn on the illumination. Instead, they cause the illumination to remain on once it turns on (e.g. from user activity). This flag will force the screen and/or keyboard to turn on immediately, when the WakeLock is acquired. A typical use would be for notifications which are important for the user to see immediately.

 - ON_AFTER_RELEASE
If this flag is set, the user activity timer will be reset when the WakeLock is released, causing the illumination to remain on a bit longer. This can be used to reduce flicker if you are cycling between wake lock conditions.

这个文档下面有个说明：If using this to keep the screen on, you should strongly consider using FLAG_KEEP_SCREEN_ON instead. This window flag will be correctly managed by the platform as the user moves between applications and doesn't require a special permission.还是推荐使用FLAG_KEEP_SCREEN_ON

## 权限获取

android.permission.WAKE_LOCK 的权限是必须的。

>Any application using a WakeLock must request the android.permission.WAKE_LOCK permission in an <uses-permission> element of the application's manifest.


另外WakeLock的设置是 Activiy 级别的，不是针对整个Application应用的。

## FLAG_KEEP_SCREEN_ON
屏幕锁另一种解决方案：Android 屏幕锁 - FLAG_KEEP_SCREEN_ON <http://www.binkery.com/archives/165.html>