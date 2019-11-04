# Android 屏幕锁 - FLAG_KEEP_SCREEN_ON
- 2014-12-18 03:02:41
- Android
- android,powermanager,wakelock,屏幕,flag,screen,

<!--markdown-->之前有一篇屏幕锁的，但是在具体的应用中总是出现问题，当我在视频播放暂停的时候，释放了锁，但是屏幕总是亮着，应该是某一个地方对屏幕进行了锁操作。


<!--more-->


WakeLock主要代码如下：

    PowerManager pm = (PowerManager)getSystemService(Context.POWER_SERVICE);
    wakeLock = pm.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, this.getClass().getName());
    wakeLock.setReferenceCounted(false);
    wakeLock.acquire(30000);
    wakeLock.release();

<http://www.binkery.com/archives/162.html>

而且android api doc 也一直在提示使用 FLAG_KEEP_SCREEN_ON 替换WakeLock 。

FLAG_KEEP_SCREEN_ON 的官方说明：
Window flag: as long as this window is visible to the user, keep the device's screen turned on and bright. 当这个window对用户可见的情况下，打开屏幕并且亮着。英语不好，大概意思而已。

对 Flag 的操作主要有：

    getWindow().setFlags(int flags, int mask);
    getWindow().addFlags(int flags);
    getWindow().clearFlags(int flags);

我使用 addFlags 和 clearFlags 的方式，目前不清楚这种方式有没有什么不好的地方，不过我的目标实现了，在我需要的地方对这个 Flag 进行操作，能把屏幕的开关交给系统去处理，达到了我在视频播放暂停的时候，释放屏幕。

    getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
    
    getWindow().clearFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);