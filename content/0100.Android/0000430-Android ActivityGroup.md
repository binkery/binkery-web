# Android ActivityGroup
- Android,activity,activitygroup,

从名字上，ActivityGroup 是 Activity 的 Group ， 也就是管理多个 Activity 的。一般来说，每个 Activity 有自己相应的一些业务逻辑和用户交互界面，ActivityGroup 可以让多个 Activity 的交互变得更加灵活多样一些，典型的就是 TabActivity 就是 ActivityGroup 的一个子类，通过 Tab 的切换，呈现多个不同的 Activity 。这样，ActivityGroup 主要负责Activity 的切换和显示，并不需要关心每个Activity的具体实现。如果没有Activity，那么开发者要嘛就需要把这些 N 多的功能模块放到一个 Activity 里去管理，Activity 要负责好各个界面的跳转，也要管理各个界面内的业务逻辑，累死掉算了。


但是由于 ActivityGroup 并不是那么的好用，所以在 Android 3.0 之后，Android 加入了 Fragment ，使用了更加灵活的方式，官方也把 ActivityGroup 打入了冷宫，已经被标志为过期的，对于 Android 3.0 以下的版本， Android 也提供了支持的 jar 包。

这样其实，把之前 ActivityGroup 的功能交给了 Activity 去完成，把之前 Activity 的功能交给了 Fragment 去完成。虽然这样理解比较简单粗暴，但是还是有效的。这样做好像没有什么实质的改变，但是 Fragment 要比 Activity 轻量一些，而且也更加方便管理了。Fragment 可以嵌套使用，可以组合使用，总之，Android 在设计的时候，已经充分的考虑到了 ActivityGroup 的缺点，也充分考虑了具体的需求。