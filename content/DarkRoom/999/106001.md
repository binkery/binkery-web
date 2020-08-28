# Android 画中画适配问题
- Android,PictureInPicture
- 2019.03.19


## 华为手机 Android 8.0 适配问题

在华为 Android 8.0 的手机上，碰见一个适配问题。在进入画中画模式后，画面拖拽，控制器和画面会出现分离的现象。最后通过反复测试，问题的根源在给 Window 添加了 FLAG_SHOW_WHEN_LOCKED 的标志导致的。这个标志在 API 27 的时候已经过期，可以改用 Activity.setShowWhenLocked() 方法来替换。

改问题在另外一个相同型号的手机，相同 Android 8.0 的系统，但不同的小版本中没有出现，大概推测是华为系统的适配问题，并且在稍后的版本中修复了。

    getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON|
        WindowManager.LayoutParams.FLAG_DISMISS_KEYGUARD|
        WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED|
        WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON);
