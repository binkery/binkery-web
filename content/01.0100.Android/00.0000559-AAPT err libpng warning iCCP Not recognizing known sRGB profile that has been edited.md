# AAPT err libpng warning: iCCP: Not recognizing known sRGB profile that has been edited
- Android,png,aapt,libpng,aapt报错,iccp报错,
- 2018-08-23 02:16:01

## update

2018.08.23

最近很长时间没有更新博客，也没有时间过来打理博客，本来是想就这样放着，也没有功夫维护。但是今天比较意外的打开博客，看了一眼，看到有几个留言，于是顺便回复了一下。在回复留言的时候发现有段英文的，我的英文并不好，每太注意，以我以往的经验，一般都是一些广告，所以我并不在意，一会删掉就是了。当我回复完前面几个后，仔细一看，发现并不是这样的。这是一位外国网友，Lukkie Mathews，他/她并不会说中文，但是他/她还是和我分享了一个图片压缩的工具，一个在线工具，是一个网页。<https://www.websiteplanet.com/zh-hans/webtools/imagecompressor/> 在这个网页里，可以对 50M 以下的图片进行压缩。

这种类似功能的在线工具其实挺多的，但是我还是很想感谢 Lukkie Mathews 同学，因为我本来已经基本放弃这个博客了～～

Many thanks to you , Lukkie Mathews。

留言地址 ： <https://binkery.com/about.html#comment-395>

## AAPT 日志

在使用 Android Studio 开发应用的时候，经常在编译的时候看见以下的 error log：

    AAPT err(1728717418): xxx.png: libpng warning: iCCP: Not recognizing known sRGB profile that has been edited

这个问题主要是因为在项目中，使用了一些不是很规范的 png 图片。美术在提供 png 图片的时候，可能跟他们使用的 PhotoShop 工具有关，在生成 png 图片的时候，在文件的头部加入了一些特殊的元数据(invalid metadata)。

## 名词解释

iCC：International Color Consortium <https://en.wikipedia.org/wiki/International_Color_Consortium>
ICCP 就是 iCC profile。
每个 png 图片中都有一个 iCCP 的 chunk。

## 解决办法

可以借助一些工具来处理这种问题。pngcrush 和 optipng 工具来进行优化。

    pngcrush -ow -rem allb -brute -reduce image.png
    optipng -o7 image.png

在 linux 系统上，可以通过脚本来批处理：

    #!/bin/sh

    for i in `find . -name "*.png"`; do
        pngcrush -ow -rem allb -brute -reduce $i
        optipng -o7 $i
    done

在 Windows 上，


    @echo off
    set /p UserInputPath= What Directory would you like?
    cd %UserInputPath%
    for /r %%i in (*.png) do ( pngcrush -ow -rem allb -brute -reduce "%%i" & optipng -o7 "%%i" )

工具的地址：

* [pngcrush](http://pmt.sourceforge.net/pngcrush/)
* [optipng](http://optipng.sourceforge.net/)

## 参考文档：

<http://stackoverflow.com/questions/32882958/android-studio-libpng-warning-iccp-not-recognizing-known-srgb-profile-that-h>

http://www.libpng.org/pub/png/
