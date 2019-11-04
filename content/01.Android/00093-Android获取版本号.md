# Android获取版本号
- 2015-03-06 08:07:12
- Android
- android,版本号,

<!--markdown-->类：android.os.Build.VERSION
常量：public static final SDK

常量：public static final int SDK_INT
说明：The user-visible SDK version of the framework; its possible values are defined in Build.VERSION_CODES

类：android.os.Build.VERSION_CODES

说明：Enumeration of the currently known SDK version codes. These are the values that can be found in SDK. Version numbers increment monotonically with each official platform release.

public static final int BASE

October 2008: The original, first, version of Android. Yay!

Constant Value: 1 (0x00000001)

......

public static final int ICE_CREAM_SANDWICH_MR1

Android 4.0.3.

Constant Value: 15 (0x0000000f)

Note： 

This SDK_INT is available since Donut (android 1.6 / API4)

so make sure your application is not retro-compatible with Cupcake (android 1.5 / API3)when you use it or your application will crash(thanks to Programmer Bruce for the precision).

before 1.6, SDK can be used.

这是Android获取版本号的方法，以1.6之前通过Build.SDK获取版本的字符串，1.6之后用SDK_INT获取int值的版本号。总是感觉这样用得不是很爽，小细节的东西。

版本的迭代还是很快的。