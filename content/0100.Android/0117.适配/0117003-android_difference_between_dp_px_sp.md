# 在 Android 中，“px”, “dip”, “dp” 和 “sp” 有哪些不同
- android,android-layout,user-interface,dimension,units-of-measurement,
- 2018.05.22

在 Android 中，“px”, “dip”, “dp” 和 “sp” 有哪些不同

## 问题 

在 Android 中，“px”, “dip”, “dp” 和 “sp” 有哪些不同？在 Android 各个单位中，有哪些不同。

* px
* dip
* dp
* sp

## 个人观点

这是一个 Android 入门的问题，对于很多刚入门 Android 开发的开发者来说。这几个单位是必须需要搞明白的。但是这些知识点并不是 Android 特有的，对于之前从事其它平台开发的开发者来说，这些并不陌生。这个问题来着 Stackoverflow，是一个比较高票的问答。

从大部分回答上可以看到，阅读 Android develpoer 官方文档是多么的重要。而这个事情被很多国内的开发者忽略掉了，我发现身边的很多同事并没有阅读官方文档的习惯，被墙和英文是一个比较大的原因，但我不认为是理由。办法总是比问题多的嘛，就像 stackoverflow 上，答案总是比问题多。


## 答案


以下来自 Android 开发者官方文档。 From the [Android Developer Documentation](http://developer.android.com/guide/topics/resources/more-resources.html#Dimension):

* **px**

    **Pixels** - 像素点，corresponds to actual pixels on the screen.

* **in**

    **Inches** - 英寸，物理的单位，based on the physical size of the screen. 1 Inch = 2.54 centimeters

* **mm**

    **Millimeters** - 毫米，物理单位。based on the physical size of the screen.

* **pt**

    **Points** - 点，物理单位，1 英寸有 72 个点。1/72 of an inch based on the physical size of the screen.

* **dp** or **dip**

    **Density** - 独立像素点，一个抽象的单位，参照物为 160 dpi 密度的屏幕，1 dp 等于 1px 。根据屏幕密度的不同，1 dp 实际等效的像素是不同的。independent Pixels - an abstract unit that is based on the physical density of the screen. These units are relative to a 160 dpi screen, so one dp is one pixel on a 160 dpi screen. The ratio of dp-to-pixel will change with the screen density, but not necessarily in direct proportion. Note: The compiler accepts both "dip" and "dp", though "dp" is more consistent with "sp".

* **sp**

    **Scale** - 也是一种抽象的单位，独立像素点。不同的是，这个单位的实际大小可能受用户设置的字体大小变化。一般被用来设置字体大小。independent Pixels - this is like the dp unit, but it is also scaled by the user's font size preference. It is recommended you use this unit when specifying font sizes, so they will be adjusted for both the screen density and user's preference.

From [Understanding Density Independence In Android](https://www.captechconsulting.com/blogs/understanding-density-independence-in-android):

    +----------------+----------------+---------------+-------------------------------+
    | Density Bucket | Screen Density | Physical Size | Pixel Size                    |
    +----------------+----------------+---------------+-------------------------------+
    | ldpi           | 120 dpi        | 0.5 x 0.5 in  | 0.5 in * 120 dpi = 60x60 px   |
    +----------------+----------------+---------------+-------------------------------+
    | mdpi           | 160 dpi        | 0.5 x 0.5 in  | 0.5 in * 160 dpi = 80x80 px   |
    +----------------+----------------+---------------+-------------------------------+
    | hdpi           | 240 dpi        | 0.5 x 0.5 in  | 0.5 in * 240 dpi = 120x120 px |
    +----------------+----------------+---------------+-------------------------------+
    | xhdpi          | 320 dpi        | 0.5 x 0.5 in  | 0.5 in * 320 dpi = 160x160 px |
    +----------------+----------------+---------------+-------------------------------+
    | xxhdpi         | 480 dpi        | 0.5 x 0.5 in  | 0.5 in * 480 dpi = 240x240 px |
    +----------------+----------------+---------------+-------------------------------+
    | xxxhdpi        | 640 dpi        | 0.5 x 0.5 in  | 0.5 in * 640 dpi = 320x320 px |
    +----------------+----------------+---------------+-------------------------------+

单位：

    +---------+-------------+---------------+-------------+--------------------+
    | Unit    | Description | Units Per     | Density     | Same Physical Size |
    |         |             | Physical Inch | Independent | On Every Screen    |
    +---------+-------------+---------------+-------------+--------------------+
    | px      | Pixels      | Varies        | No          | No                 |
    +---------+-------------+---------------+-------------+--------------------+
    | in      | Inches      | 1             | Yes         | Yes                |
    +---------+-------------+---------------+-------------+--------------------+
    | mm      | Millimeters | 25.4          | Yes         | Yes                |
    +---------+-------------+---------------+-------------+--------------------+
    | pt      | Points      | 72            | Yes         | Yes                |
    +---------+-------------+---------------+-------------+--------------------+
    | dp      | Density     | ~160          | Yes         | No                 |
    |         | Independent |               |             |                    |
    |         | Pixels      |               |             |                    |
    +---------+-------------+---------------+-------------+--------------------+
    | sp      | Scale       | ~160          | Yes         | No                 |
    |         | Independent |               |             |                    |
    |         | Pixels      |               |             |                    |
    +---------+-------------+---------------+-------------+--------------------+


更多可以参考 [Google Design Documentation](https://www.google.com/design/spec/layout/units-measurements.html#).

这里有一个应用可以计算真实设备的分辨率 [this](https://play.google.com/store/apps/details?id=com.faizmalkani.keylines&amp;hl=en)。

## 答案

这里有一遍来自 Android Developer 的文档，多屏幕适配 [Supporting Multiple Screens](http://developer.android.com/guide/practices/screens_support.html)

* **Screen size**

    屏幕大小 ，物理尺寸。Actual physical size, measured as the screen's diagonal.For simplicity, Android groups all actual screen sizes into four generalized sizes: small, normal, large, and extra-large.

* **Screen density**

    屏幕密度，在一个物理区域内，包含的像素点个数。通常用 dpi ，dots per inch 。比如，在一个固定的物理面积下，低密度屏幕（low）的像素点要比 正常的（normal）或者高密度（high）少。目前在 Android 平台上，把屏幕密度分为下面几种，low，medium，high，extra-high,extra-extra-high, extra-extra-extra-high.

    The quantity of pixels within a physical area of the screen; usually referred to as dpi (dots per inch). For example, a "low" density screen has fewer pixels within a given physical area, compared to a "normal" or "high" density screen. For simplicity, Android groups all actual screen densities into six generalized densities: low, medium, high, extra-high, extra-extra-high, and extra-extra-extra-high.

* **Orientation**

    方向。屏幕的方向，中文的说法是横屏和竖屏，英文是 landscape 和 portrait 。不同的设备有不同的默认屏幕方向，屏幕方向也可以在运行时被改变。

    The orientation of the screen from the user's point of view. This is either landscape or portrait, meaning that the screen'saspect ratio is either wide or tall, respectively. Be aware that not only do different devices operate in different orientations by default, but the orientation can change at runtime when the user rotates the device.

* **Resolution**

    分辨率，一个屏幕实际的物理像素点。

    The total number of physical pixels on a screen. When adding support for multiple screens, applications do not work directly with resolution; applications should be concerned only with screen size and density, as specified by the generalized size and density groups.

* **Density-independent pixel (dp)**

    dp，一个虚拟的像素点单位。dp 和物理像素点 px 有一定的换算关系。换算关系和屏幕的密度有关，在一个 240 dpi 密度的屏幕上，1dp 等于 1.5 像素点。dp 是平时在开发中运用比较多的一个单位。

    A virtual pixel unit that you should use when defining UI layout, to express layout dimensions or position in a density-independent way. The density-independent pixel is equivalent to one physical pixel on a 160 dpi screen, which is the baseline density assumed by the system for a "medium" density screen. At runtime, the system transparently handles any scaling of the dp units, as necessary, based on the actual density of the screen in use. The conversion of dp units to screen pixels is simple: `px = dp * (dpi / 160)`.  For example, on a 240 dpi screen, 1 dp equals 1.5 physical pixels. You should always use dp units when defining your application's UI, to ensure proper display of your UI on screens with different densities.


If you are any serious about developing an Android app for more than one type of device, you should have read the screens support development document at least once. In addition to that it is always a good thing to know the actual number of active devices that have a particular screen configuration.

- [Screen Sizes and Densities](http://developer.android.com/resources/dashboard/screens.html)
