# Android 设置 Activity 透明
- 2015-03-06 13:54:28
- Android
- android,activity,样式,

<!--markdown-->想要给 Activity 色值为一个透明的颜色，这样新的 Activity 就可以像浮动在当前 Activity 上面一样，在某些场合下，能让应用看上去更加清爽一下。当然，很多整盅的应用也会这样子做。打开一个应用，但是这个应用是全透明的，跟没打开一样，还能看见桌面，但是一点屏幕的时候突然出现裂缝，碎屏。我就刚刚给朋友做了这么一个小应用。


要实现 Activity 透明，可以给 Activity 设置一个自定义的样式。

    <style name = "your name" parent = "@android:style/Theme">
    <item name = "android:windowBackground">@android:color/transparent</item>
    <item name = "android:windowNoTitle">true</item>
    <item name = "android:windowIsTranslucent" >true</item>
    </style>

Ok  ,这样基本搞定了，你的 Activity 是透明的了。