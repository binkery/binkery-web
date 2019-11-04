# Android 软键盘弹起和消失事件
- 2016-03-23 03:15:21
- Android开发中的那些坑
- 

<!--markdown-->Android 可以手动的弹起和收起软键盘，但是软键盘的弹起和收起没有任何回调，所以你在程序中不能知道软键盘的状态的变化。
解决办法就是计算当前 layout 的高度来判断键盘的状态。

* <https://gist.github.com/felHR85/6070f643d25f5a0b3674>
* <http://stackoverflow.com/questions/2150078/how-to-check-visibility-of-software-keyboard-in-android>
* <http://felhr85.net/2014/05/04/catch-soft-keyboard-showhidden-events-in-android/>
