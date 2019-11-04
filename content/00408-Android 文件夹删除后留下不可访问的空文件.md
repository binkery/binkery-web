# Android 文件夹删除后留下不可访问的空文件
- 2015-03-06 13:39:11
- Android
- android,文件,目录,

<!--markdown-->自己做了一个简单的 Android 文件管理器，现在碰见了一个问题，就是在删除一个文件夹的时候，会留下一个同名的空文件，0 字节，不能被删除。我在我的 Nexus 4 ， Android OS 4.4.4 上，多次出现删除 sdcard 目录下的 baidu 和 tencent 的目录时，出现这个问题。这两个是目录很明显是百度和腾讯的 APP 创建的目录，但是问什么删不掉呢。我查找了一些资料，但是都没有解决这个问题。


<!--more-->


首先，删除一个目录，Java 没有提供删除非空目录的方法，只能通过递归去实现。这个没有问题，网上也有很多这样的代码，都是 OK 的。

删除文件之后，有人说需要给系统发送一个广播，让系统扫描一下 sdcard 。

    sendBroadcast(new Intent(Intent.ACTION_MEDIA_MOUNTED, Uri.parse("file://" + Environment.getExternalStorageDirectory())));

但是，这个很不幸，在 Android 4.4 里，这个广播被禁止了，系统不希望一个 APP 能发起这样的广告，这样会把系统累死掉的，这个我能理解。

Android 在后来的版本中，在 MediaStore 中增加了 Files 这个类。但是现在提供的API 和文档都很少，不过还是可以通过这样的方式获取到 URI 的。

    Uri u = MediaStore.Files.getContentUri("external");

然后去 query 结果，我测试的结果是，这个数据库里，确实还存在被我删掉的目录下的文件的记录。如果是这样的话，那么出现空文件的现象是可以说得过去的。但是怎么删除呢？先删文件再删数据库？还是先删数据再删文件？ 在我纠结这得花多少功夫去做的时候，发现有人说在 Android 4.4+ ，禁止 APP 往 sdcard 上非 APP 所属的目录下写文件。也就是说，Android 不打算让 APP 随意在 SD card 上写文件，系统会提供给你一个特定的目录，大家分别写在自己的目录下。这个方法必须是一个好方法，我也认为很有必要这样子做。但是好像不是这样子的，至少我之前还删掉了很多别人的文件和目录呢。这是哪里出现的问题呢。

> "Apps must not be allowed to write to secondary external storage devices, except in their package-specific directories as allowed by synthesized permissions."

针对这个问题，有人提出了一个方案，大概的意思跟我之前的差不多，从数据库里删除文件记录。但是很悲剧的是，有人提出了，在他的测试手机中，这个方案行不同，删除记录的时候出现错误。另一个哥们也说了，在他的非 root 的手机里，读写sdcard 畅通无阻，压根没有这个限制。

好了，最后问题来了，到底问题出现在哪了？

接着研究了。随便说一句，Google 的碎片化，让人头疼的绝对不是分辨率，尺寸的碎片化，这种功能上的碎片化才是最让人头疼的。魔鬼啊。

附上几个 stackoverflow 的连接。

* http://stackoverflow.com/questions/4430888/android-file-delete-leaves-empty-placeholder-in-gallery
* http://stackoverflow.com/questions/1248292/how-to-delete-a-file-from-sd-card
* http://stackoverflow.com/questions/4646913/android-how-to-use-mediascannerconnection-scanfile/4646955#4646955
* http://stackoverflow.com/questions/2170214/image-saved-to-sdcard-doesnt-appear-in-androids-gallery-app