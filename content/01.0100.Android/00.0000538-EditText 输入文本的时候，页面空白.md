# EditText 输入文本的时候，页面空白
- 2016-03-23 03:35:15
- Android开发中的那些坑
- 

<!--markdown-->在 EditText 获取到焦点后，软键盘弹出，页面内容出现了错误，比如文本框被遮盖，页面显示空白等。这是一个 Anroid 已知的bug，大概原因是全屏模式下，软键盘弹出后，高度计算错误。link ： <https://code.google.com/p/android/issues/detail?id=5497>

从 bug 号可以看出这是一个很早的 bug 了，而 Android 一直没有修改这个问题，大部分应用也只有在启动页面是全屏模式，在正式进入应用后，基本都不处于全屏模式，所以这个问题可能没有受到重视。直到　android 4.4 ,Android 引入了　Translucent 样式，浸入式的设计，让应用可以控制状态栏的颜色和样式，这个问题也就再次爆发了。下面是 stackoverflow 上的问答<http://stackoverflow.com/questions/19897422/keyboard-hiding-edittext-when-androidwindowtranslucentstatus-true> 。

## 解决办法：

最简单的解决办法就是不使用全屏模式，不使用 Translucent 样式。这属于规避问题，不是解决问题，这样的方案需要经过产品的授权。

还有一种解决方案，就是在 EditText　所在的布局的根布局设置 android:fitsSystemWindows="true" ，并且使用　SystemBarTintManager 库：

    new SystemBarTintManager(this).setStatusBarTintEnabled(true);

这样也可以搞定这个问题。