# Android 获取 cache 目录失败 ContextImpl: Failed to ensure directory
- 2016-03-23 03:16:04
- Android
- Android,cache
- getExternalCacheDir失败,getCacheDir失败,getExternalCacheDir异常,Failed to ensure directory,
- Android 中调用 context.getExternalCacheDir() 或者 context.getCacheDir() 的时候，会报一个错误 Failed to ensure directory。这种错误一般出现在 app 卸载不彻底的情况下，重启手机可以搞定。

# ContextImpl: Failed to ensure directory

在通过 context.getExternalCacheDir() 或者 context.getCacheDir() 类似的方法获取文件的时候，可能会报以下的错误：

> ContextImpl: Failed to ensure directory: /storage/sdcard1/Android/data/com.binkery.allinone/cache

在 Stackoverflow 上找到的答案，基本可以忽略这个错误提示。

## Answer 1 :

This happened to me when uninstalling the app and reinstalling it. But probably the resources of the app (com.xxxx.app in your case) had a reference not released.

The solution was quite simple: just stop and relaunch the emulator, or reboot the phone should do the trick.

这里解释获取 cache 目录失败的原因是卸载 app 并且重新安装的时候，某些 app 的资源因为没有释放没有被彻底删除掉，导致的失败。重启手机可以解决这样的问题。

另外吐槽一下小米手机，通过 adb 在小米手机上安装应用程序，经常会出现各种各样的安装失败。

## Answer 2 :

This is because you are connected to your development machine, and cannot write to the emulated storage on it.
        
link ：<http://stackoverflow.com/questions/27736608/android-failed-to-ensure-directory-when-getexternalfilesdirnull>

另外一种可能是你连接的设备是一个开发机，并且你不能写入文件到它的存储器中。这种一般比较少。
