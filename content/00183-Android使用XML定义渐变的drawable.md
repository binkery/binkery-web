# Android使用XML定义渐变的drawable
- 2015-03-06 10:00:07
- Android
- android,xml,drawable,渐变,

<!--markdown-->不是什么东西都需要美术来做图，利用Android提供的线程的东西，也能作出一下效果出来。当然比较负责的效果就需要比较大的工作量了，而且也不一定能做到。一些简单的效果还是可以使用XML来定义的，省得美术做图了，一般来讲，效果不会差到哪去。


<!--more-->


    <?xml version="1.0" encoding="utf-8"?>
    <shape xmlns:android="http://schemas.android.com/apk/res/android" >
    
        <gradient
            android:angle="90"
            android:centerColor="#FF3f3f3f"
            android:centerY="0.5"
            android:endColor="#FF2c2c2c"
            android:startColor="#FF2c2c2c"
            android:type="linear"
            android:useLevel="false" />
    </shape>

上面的代码是一定一个渐变的背景。

官方文档：

### android:angle
Integer. 
The angle for the gradient, in degrees. 0 is left to right, 90 is bottom to top. It must be a multiple of 45. Default is 0.
0是从左到右渐变，90是从下到上渐变。要45的整数倍，说明是可以斜着渐变的。

### android:centerX
Float.
 The relative X-position for the center of the gradient (0 - 1.0).
X轴渐变中心点的位置（0 到1 的一个值）

### android:centerY
Float. 
The relative Y-position for the center of the gradient (0 - 1.0).
Y轴渐变中心点的位置 （0 到1 的一个值）

### android:centerColor
Color. 
Optional color that comes between the start and end colors, as a hexadecimal value or color resource.
中间点的色值

### android:endColor
Color. 
The ending color, as a hexadecimal value or color resource.
结束的色值

### android:gradientRadius
Float. 
The radius for the gradient. Only applied when android:type="radial".
只有在android:type="radial"的时候有效。

### android:startColor
Color. 
The starting color, as a hexadecimal value or color resource.
开始的色值。

### android:type
有三种类型
Keyword. 
The type of gradient pattern to apply. Valid values are:
* "linear"	A linear gradient. This is the default.
* "radial"	A radial gradient. The start color is the center color.
* "sweep"	A sweeping line gradient.

### android:useLevel
Boolean. 
"true" if this is used as a LevelListDrawable.
如果为true，将被当成LevelListDrawable使用。