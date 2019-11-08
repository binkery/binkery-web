# Internal Storage And External Storage
- Android,内部存储,外部存储


## 内部存储 Internal Storage

一般我们可以直接通过 API 在内存存储里创建文件，写文件，读取，删除。这些文件都是 Application 私有的，一般其他应用没法访问，也不能修改和删除，这些文件会在应用被卸载的时候一同删除。用户也可以在设置里的应用管理中清除数据的方式删除。这里如果放太多文件，或者太大文件的话，可能会导致内部存储不够用。

	openFileOutput(String filename,Context.MODE_PRIVATE);
	openFileInput(Strnig filename,Context.MODE_PRIVATE);

modes 总共就四种:

 * MODE\_PRIVATE 默认的 mode
 * MODE\_APPEND 追加，如果文件存储，写入的内容追加到文件的末尾
 * MODE\_WORLD\_READABLE 已过期，忽略
 * MODE\_WORLD\_WRITEABLE 已过期，忽略

我们可以在编译的时候，把文件放在项目的 res/raw/ 目录下，然后通过 *openRawResource()* 已经 *R.raw.<filename\>* 的方式去读取文件，但是不能写。其他相关的资源访问可以参考这篇文章 ： <http://blog.binkery.com/android/resource/android_xml_raw_assets.html>


### 缓存文件 Saving cache files

Android 也提供了一个临时的缓存方式。通过 getCacheDir() 获取一个同样只属于你的应用的，位于内部存储空间的目录。你可以把你需要的临时缓存文件放在这个目录下。

当设备处于一个低内部存储可用的情况下，Android 会删除这些缓存来释放空间。但是，你不要依赖于系统，系统不到万不得已，不会轻易去帮你清理的，所以，一般来说，你需要自己管理好这个缓存目录，及时清理，设置一个合理的上限。这个目录也会在应用被卸载的时候被删除。

### Other useful methods

* getFilesDir() 
	
	获取系统给你的应用分配的内部存储目录的绝对路径。

* getDir() 

	创建或者打开一个目录，位于你的内部存储空间

* deleteFile()

	 删除文件

* fileList()
	
	获取你的应用创建的文件的数组


## 外部存储 Using the External Storage

Android 设备还提供了一个外部存储（External Storage），这个外部存储可能是像 sdcard 那样，可以移除的，也可能是内置到手机里的，但他们都属于外部存储，相对于你的应用来说的，存放在外部存储空间的文件是全世界可读的（world-readable），用户也可以通过一些方式修改这些文件，比较连接到电脑后修改他们。

> 注意: 外部存储可能会暂时变得不可用，比如用户连接到他的电脑上，或者 sdcard 被用户拿掉，都是可能发生的。所以你存放在外部存储空间的文件是不安全的。不安全不代表不能用！！！

### 设置权限 Getting access to external storage

读写 external storage 需要权限，Android 在不同版本对 external storage 权限管理做了一些修改，这里不具体描述了。

### 检测状态 Checking media availability

刚才说了，外部存储可能暂时处于一个不可用的状态，所以在使用前，需要先检测一下状态，getExternalStorageState() 这个方法用来检测当前外部存储设备的状态。当外部存储设备不可用的时候，你可能需要提示用户或者干一些别的事。

### 共享文件 Saving files that can be shared with other apps

虽然你写在外部存储空间的文件是全世界可读的，但并不能很好和其他应用共享，因为别人不知道你具体写在哪个目录了，你也不知道别人都写在哪了。为了让各个应用愉快的交流，Android 提供了一个公共目录，比如 Music/ 是音乐，Pictures/ 是图片，Ringtones/ 是铃声。

通过调用 getExternalStoragePublicDirectory() 已经相对应的参数，比如 DIRECTORY\_MUSIC, DIRECTORY\_PICTURES, DIRECTORY\_RINGTONES 等，你可以获取到你想要的目录，你把你的文件存放在这些目录，系统的多媒体扫描程序会自动对他们进行扫描，放在铃声目录下的音频文件会出现在铃声的列表里，就是这个意思。

### 对多媒体扫描隐藏 Hiding your files from the Media Scanner

在你创建的外部存储的目录下，创建一个 .nomedia 的空文件，注意，是一个隐藏文件。这样子，Media Scanner 就不会对这个目录下的多媒体文件进行扫描了。你放在这个目录下的一些小图片也不会出现在系统的相册里了。就是这个意思。 However, if your files are truly private to your app, you should save them in an app-private directory.


### Saving files that are app-private

如果你不希望你的文件被别人使用，但是又得放在外部存储，那么你可以创建一个私有的目录。通过调用 getExternalFilesDir() 方法，系统给你分配一个目录。

> Note: 当用户卸载应用后，这个目录下的文件也会被删除的。同时，系统的多媒体扫描也不会去扫描这些文件的。 

有些时候，一个设备会把内置的存储空间开辟出一个外部存储空间，虽然他也提供了sdcard 的插槽。在低于 4.3 及以下的系统中，这个时候，如果你调用 getExternalFilesDir() ，获得到的是从内置存储空间划分出来的外部存储空间，而不是 sdcard 的空间。从 4.4 开始，getExternalFilesDirs() 返回的是一个数组，包括了虚拟的外部存储空间和真实的sdcard 的外部存储空间，数组的第一个元素是虚拟的外部存储空间。如果你想在 4.3 及以下的设备中也有同样的操作，可以使用支持包提供的 api ：ContextCompat.getExternalFilesDirs()。虽然他返回的也是一个数组，但是数组只有一个元素。

> 注意：通过 getExternalFilesDir() 和 getExternalFilesDirs() 获取到的目录下的文件不被 MediaStore 扫描，但是其他拥有 READ\_EXTERNAL\_STORAGE 权限的应用是可以访问的，所以，你需要完全限制这些文件的访问，那么还是放在内部存储空间吧。

### 缓存文件 Saving cache files

通过调用 getExternalCacheDir() 可以获取一个位于外部存储空间的缓存目录，在应用卸载的时候，这些文件会被删除。

和上面的 ContextCompat.getExternalFilesDirs() 相似，你可以调用 ContextCompat.getExternalCacheDirs() 来获取外部空间的缓存目录。

> Tip: 特别提示好好管理好你的缓存文件，及时删除没用的缓存文件。


更多内容，访问 <http://developer.android.com/guide/topics/data/data-storage.html> 官方文档。

## 小结

* 内部存储空间是最私密的，不受干扰的，但是一般来说，空间是宝贵的
* 内部存储空间和外部存储空间都有缓存目录，但是一定要自己管理好
* 外部存储空间有可能是从内部存储空间虚拟出来的，特别对于那些有外置sdcard 的设备，外部存储空间 ！= sdcard 空间。
* 只要是外部存储空间的文件，都是全世界可读的，只是系统自己比较有节操，但是其他 App 就不一定了。
* Android 提供了公共目录，希望得到共享的，大可以尽量放进去