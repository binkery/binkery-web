# TextView android:drawablePadding 不起作用的时候
- 2015-03-06 10:03:28
- Android
- android,textview,padding,

<!--markdown-->在TextView的上下左右四个方向可以设置一个图片，这是一个很常用的布局方式，但是使用的时候总是碰到很多的意外情况。比如android:drawablePadding不起作用。


<!--more-->


百度，google了一下，总是能看见这么几个答案，但是那些都不足以解决我的问题。在具体的实战开发中，总能碰见很多很狗血的问题。

### android:drawableBottom
在text的下方输出一个drawable，如图片。如果指定一个颜色的话会把text的背景设为该颜色，并且同时和background使用时覆盖后者。

### android:drawableLeft
在text的左边输出一个drawable，如图片。

### android:drawablePadding
设置text与drawable(图片)的间隔，与drawableLeft、drawableRight、drawableTop、drawableBottom一起使用，可设置为负数，单独使用没有效果。

### android:drawableRight
在text的右边输出一个drawable，如图片。

### android:drawableTop
在text的正上方输出一个drawable，如图片。

在 stackoverflow 上找到一个老外的说法：

> android:drawablePadding will only create a padding gap between the text and the drawable if the button is small enough to squish the 2 together. If your button is wider than the combined width (for drawableLeft/drawableRight) or height (for drawableTop/drawableBottom) then drawablePadding doesn't do anything.

我认为是这样的，当你的 textview 设置 match_parent 的时候，是很可能出现这个问题的。这个时候 android:drawablePadding 是无效的，为啥无效不清楚，有时间看看源代码。

解决的办法就是想其他的办法了。肯定不是使用 android:drawablePadding 的方法来实现你要的了。