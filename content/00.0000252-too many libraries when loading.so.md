# too many libraries when loading *.so
- 2013-09-03 03:54:20
- Android
- android,源码,so,内核,
- so库超过上限,so库上线,too many libraries when load so,
- Android app 加载 so 库的时候，如果加载的 so 库过多，会触发 so 库上限的限制，报错 too many libraries when loading *.so 

在加载 so 库的时候，碰见这个问题，原因是因为加载的 so 库超过了 Android 系统定义的上限。上限的值定义在bionic/linker/linker.c 的 SO_MAX 这个常量上。

Binoic 是 Android 的内核，Bionic imposes a hard limit on the number of shared objects you can load at run time.There are a few ways to work around this issue:

If you're not using a huge pipeline that actually requires to load a number of plugins at runtime that makes you hit the limit, you can use GST_REGISTRY_REUSE_PLUGIN_SCANNER=no and it should work (This was implemented in GStreamer by commit dd9f244f033ba3978d6ee26d9205d29fdd862d7c, Oct 18/2011 so please check you have a recent enough version).

If your pipeline is complex enough so it makes you hit the limit no matter what. Then you have two alternatives:

The first one is to modify Android to change limit. You will be bumping SO_MAX to (for example) 128 in Android's bionic/linker/linker.c and rebuilding with make linker. Then you will need to install this customized version of Android on your device as it's explained in the Installing our bundle on the Nexus S section of this document.

SO_MAX 的值在不同的 Android os 版本上是不同的，估计不同的手机厂商也是会有不同。比较早的版本，比如 2.2 的，可能会是 64 或者其他值，4.0，4.1，4.2 的，可能是 128 或者 192 。修改这个值，可以通过自己修改源码，然后编译，刷机。

Another option is to explore building the plugins as static libraries. You can find a patch implementing this solution here: https://bugzilla.gnome.org/show_bug.cgi?id=667305

bionic/linker/linker.c source code : http://www.netmite.com/android/mydroid/bionic/linker/linker.c

