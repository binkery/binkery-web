# build.gradle 文件中的 Android SDK Build Tools version
- Android,Gradle,SDK
- 2018.07.17

在 Android Gradle Plugin 3.0.1 中，最低的 Android SDK Build Tools 是 26.0.2，而我声明的 25.0.0 将被忽略掉。

今天新建了一个 Android 项目的时候，无意中发现了这么一个 warning 。

> Warning:The specified Android SDK Build Tools version (25.0.0) is ignored, as it is below the minimum supported version (26.0.2) for Android Gradle Plugin 3.0.1.
> Android SDK Build Tools 26.0.2 will be used.
> To suppress this warning, remove "buildToolsVersion '25.0.0'" from your build.gradle file, as each version of the Android Gradle Plugin now has a default version of the build tools.

之前一直使用版本较低的 Gradle 插件，并没有发现这个问题，说明新的 Gradle 插件定义了最低的 SDK Build Tools 的版本，至少在 Android Gradle Plugin 3.0.1 版本上，Build Tools 的最低版本是 26.0.2 。

这就提示我在正式项目中如果升级了 Gradle Plugin 版本的话，那么对应的 Build Tools 版本会被动升级的。Build Tools 被动升级的话，我需要考虑到其他同时开发环境是否有对应的版本，需要提示他们升级。同时 Jenkins 构建服务器的打包环境也需要检查一下，是否需要升级。
