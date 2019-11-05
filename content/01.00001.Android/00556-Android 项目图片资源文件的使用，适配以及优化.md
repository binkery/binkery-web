# Android 项目图片资源文件的使用，适配以及优化
- 2016-05-13 16:52:50
- Android
- android,适配,bitmap,bitmapfactory,优化,

<!--markdown--># 图片资源文件

## Android 项目中常见的图片文件格式

* png 支持 alpha 通道，无损压缩，体积大，
* jpg 不支持 alpha 通道，有损压缩，体积小，

计算机颜色常见的表达方式：ARGB，一个像素点的颜色由四个信息组成，A 是 Alpha,透明度，也称通透度。RGB 分别值 Red,Green,Blue 三颜色。ARGB 是一种颜色模式，颜色模式有很多种，png 使用的是 ARGB，也可以是 RGB（就是不包含 alpha 通道），jpg 使用的是 YUV 颜色模式。具体的区别可以去研究各种图形文件格式的标准定义。

jpg 是一种有损压缩格式，有损是因为它存储的是 YUV 颜色，也就是它在文件里存储的不是 RGB 颜色，在解码图片的时候，从文件中读取出数据，然后根据一定的算法，换算成 ARGB，这里肯定会有一些精度的损失。压缩模式也有很多种，一种是顺序式压缩，图像的信息从左到右，从上到下，采用这种压缩模式的图片，可以实现从上到下的加载显示方式；另外一种是递增式压缩，可以实现从模糊到清晰的渐进式加载。所以在 Android 项目中，如果想要实现渐进式加载，对要加载的图片还是有一些要求的。如果不是采用类似于递增式压缩的图片，是很难实现渐进式的加载实现的，即使实现了也是有悖初衷的。

## 文件结构

基本上，任何文件都包含头信息和文件主体。这个是计算机世界上通用的设计，包括文件和协议，都有头和主体（header & body）。

每个文件的前几个字节会标识文件的类型，比如Java 的 class 文件，前四个字节的内容是CAFE，在打开文件的时候，先读取前几个字节，判断该文件是不是当前程序能处理的格式。文件名的后缀不属于文件的内容，而属于文件系统（File System）。

除了前几个字节用来标识文件格式外，接下来的那些内容，直到文件的主体内容前，都被称为头信息，也可以称为 metadata 。每种文件都会定义字节的 metadata 信息，对于图片文件，metadata 会包含咱们最关心的图片大小，只需要解析头信息，就可以知道图片的大小了，于是咱们在使用 BitmapFactory.decode()的时候会推荐这样使用：

    BitmapFactory.Options options = new BitmapFactory.Options();
    options.inJustDecodeBounds = true;
    BitmapFactory.decodeFile(path, options);
    
这个时候 BitmapFactory 只读取图片的文件的头部的信息，所以返回的 bitmap 对象是空的，在获取到图片的宽高后，在根据比例去 decode 。

# 适配以及优化

我们知道，在 Android 开发中，有多个不同的 drawable 目录，这些目录的作用是为了做 Android 多分辨率适配的。除了默认的 drawable 目录外，还有 drawable-ldpi,drawable-mdpi 和 drawable-hdpi 。只是 Android 早期版本为三个不同密度屏幕设计的目录，后来又新增了 drawable-xhpi 和 drawable-xxhpi 以及 drawable-xxxhdpi。三个 x 的屏幕密度已经是相当高了，目前高端的手机有不少是这个屏幕密度的。而那些低密度屏已经慢慢的淡出了大家的视线。

mdpi 的屏幕密度为 160dpi
hdpi 的屏幕密度为 240dpi，为 mdpi 的 1.5 倍
xhdpi 的屏幕密度为 320dpi，为 mdpi 的 2 倍
xxhdpi 的屏幕密度为 480dpi，为 mdpi 的 3 倍
xxxhdpi 的屏幕密度为 640dpi，为 mdpi 的 4 倍

## 适配第一原则

适配的作用就是为了在不同分辨率，不同密度的屏幕上，都能看到我们期望的质量的图像。所以在有图像质量要求的场景下，该放哪个目录放哪个，该放几个放几个。

## 资源图片对 APK 文件大小的影响

每增加一个资源文件，APK 文件的大小的增大是可以肯定的。而实际上，一个资源图片被打包的时候，打包器还是会对资源进行一些优化的，但是由于 png 和 jpg 已经采用很高的压缩率的编码方式，所以这个优化只能说是很小的，你基本可以认为你增加的大小是约等于文件的大小的。

## 对应用程序安装后占用空间大小的影响

一直以来，我认为 Android 在安装 APK 文件的时候，不是简单的解压释放文件那么简单，会根据当前设备的一些信息，放弃一些资源文件，比如一张图片在不同的 drawable 目录下都存在，那么只会保留最适配的那张。但是，事实不是这样的。我增加了一张适配文件，安装后的体积还是增加了。

## 对运行时内存的影响

首先，一个图片资源最终显示在屏幕上的面积会影响其占用的内存大小。在其他条件相同的情况下，一个 200dp 宽高的 ImageView 会比一个 100dp 的占用内存多。

其次，在不考虑显示效果的情况下，最终显示面积相同的控件，其资源文件在低密度下比在高密度下占用内存高。比如一张背景图片被放在 drawable-ldpi 比放在 drawable-xxxhdpi 下占用的内存多。

在不指定 ImageView 控件大小的情况下，资源图片放在低密度目录下，最终显示面积会更大一些，资源图片放在高密度目录下，最终显示面积会变得更小。

在指定的 ImageView 控件大小的情况下，资源图片放在低密度目录下要更加清晰一些，放在高密度目录下，图像会变得模糊。

## 多出来的 mipmap 目录

在 Android 4.2 后，在使用 Android Studio 创建项目的时候，突然悄悄多了几个 mipmap 的目录，而里面一般只是放了一个应用的启动的图片，那么我们怎么使用这个目录呢，mipmap 和 drawable 有啥不同？

首先看看官方文档的说明：

    Mipmapping for drawables

    Using a mipmap as the source for your bitmap or drawable is a simple way to provide a quality image and various image scales, which can be particularly useful if you expect your image to be scaled during an animation.

    Android 4.2 (API level 17) added support for mipmaps in the Bitmap class—Android swaps the mip images in your Bitmap when you've supplied a mipmap source and have enabled setHasMipMap(). Now in Android 4.3, you can enable mipmaps for a BitmapDrawable object as well, by providing a mipmap asset and setting the android:mipMap attribute in a bitmap resource file or by calling hasMipMap().


就是说 mipmap 和 drawable 功能是相似的，那么怎么使用：

    drawable/
    For bitmap files (PNG, JPEG, or GIF), 9-Patch image files, and XML files that describe Drawable shapes or Drawable objects that contain multiple states (normal, pressed, or focused). See the Drawable resource type.
    mipmap/
    For app launcher icons. The Android system retains the resources in this folder (and density-specific folders such as mipmap-xxxhdpi) regardless of the screen resolution of the device where your app is installed. This behavior allows launcher apps to pick the best resolution icon for your app to display on the home screen. For more information about using the mipmap folders, see Managing Launcher Icons as mipmap Resources.

在目前为止，大部分场景下，咱们不需要把图片放在 mipmap 目录下。

## Bitmap

对于 Android 开发来说，由于 bitmap 的问题导致的 OOM 是咱们平时开发中需要注意的事情。当然，一般项目的中使用的框架已经基本上 hold 住这些问题了。

在 Bitmap 类中，封装了一个 byte[] ，就是这个 byte[] 占用了大量的内存。

比如手机拍摄的是一个 3000 × 4000 像素的图片，而咱们需要在屏幕上显示一个很小的缩略图。如果这张图片经过了 Android 系统的扫描，系统会为这张图生成一套缩略图，我们可以直接使用这套缩略图。而如果这套缩略图不符合咱们需要，或者系统没有扫描这张大图，那么我们需要自己去 decode 这张图片。如果我们直接去 decode 这张图，那么咱们将会占用 3000×4000×4 = 45.78 Mb 的内存，这样是很危险的。在上文中，咱们说了一种办法来减少 bitmap 的内存占用，先 decode 图片的头信息，获得宽和高后，在按比例去 decode 图片。在获得图片的原始宽高后，又假设咱们的手机屏幕是 720 宽的，在第二次 decode 的时候，BitmapFactory 会根据 options 对象的 inSampleSize 参数来等比例缩小图片，inSampleSize = 2 表示宽和高各取二分之一。很不幸，inSampleSize 只能是一个整数，而且只能是 2 的 N 次方。如果 inSampleSize = 4 ，宽和高分别为原始图片的四分之一，也就是 750 × 1000，这个大小是比较符合咱们期望的。如果咱们使用 inSampleSize = 4 去 decode 图片的话，这个时候的内存占用应该会是 750×1000×4 = 2.9 Mb，也就是刚才 45.78 的十六分之一，这样一下子就减少了很多内存占用了。咱们可以再进一步对 750 进行缩放，或者直接使用都是可以的。上面计算的时候，每个像素点都是以 4 个字节的占用去计算的，在使用 BitmapFactory decode 图片的时候，我们还可以通过设置 options 对象的 inPreferredConfig 参数来指定每个像素占用的字节数，默认是 ARGB_8888，也就是 4 个字节，如果我们设置为 RGB_565，则每个像素占用的是 2 个字节，这样内存占用还能再减少一半，也就是 1.45 Mb。在 Bitmap 类中，封装了一个 byte[]，默认情况下，这个数组的每四个单元用来表示一个像素点的颜色值，在使用 RGB_565 的情况下，这个数组的每两个单元用来表示一个像素点的颜色值。

所以，在咱们使用 BitmapFactory 手动 decode 图片的时候，需要咱们关心的参数就是 options.inSampleSize 和 inPreferredConfig ，这两个参数会影响到 bitmap 的体积，同样也会影响到图像的质量。

