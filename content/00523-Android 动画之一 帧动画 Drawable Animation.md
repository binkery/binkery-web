# Android 动画之一 帧动画 Drawable Animation
- 2016-05-16 03:21:26
- Android
- 

<!--markdown-->帧动画让你可以一帧一帧的渲染资源文件里的图片，就像播放电影一样的。

# AnimationDrawable

AnimationDrawable 是帧动画的基础。

首先，你需要在 res/drawable/ 目录下创建一个 xml 文件。可以看出，帧动画是属于 draweble 系统的一部分。

xml 的结构是这样子的，根元素是 <animation\-list\> ，子元素是一个一个 <item\> 。一个 item 就是一帧。下面是官网的例子，直接抠过来了。

    <animation-list xmlns:android="http://schemas.android.com/apk/res/android"
        android:oneshot="true">
        <item android:drawable="@drawable/rocket_thrust1" android:duration="200" />
        <item android:drawable="@drawable/rocket_thrust2" android:duration="200" />
        <item android:drawable="@drawable/rocket_thrust3" android:duration="200" />
    </animation-list>

大概就是这样子，每个元素都有一些可以设置的属性，这里就先不依依描述了。大概就是可以定义动画的循环次数，还是无限循环啊，还有时长啊，之类的。


定义完动画 xml 文件，下面说说怎么使用。

    ImageView rocketImage = (ImageView) findViewById(R.id.rocket_image);
    rocketImage.setBackgroundResource(R.drawable.rocket_thrust);
    rocketAnimation = (AnimationDrawable) rocketImage.getBackground();
    rocketAnimation.start();

上面还是 Android 官网的列子。可以看出，帧动画是被当成背景使用的，所以，帧动画属于 View backgrond 系统的一部分。
在获取到一个 AnimationDrawable 对象后，通过调用 start() 方法就可以让动画动起来了。

# AnimationDrawable 的 Android 源码分析

咱们可以看到 AnimationDrawable 是通过 View.setBackgroundResource() 的方式使用的，xml 也是放置在 res/drawable/ 目录下的。于是，咱们去看看源码，首先从 View 这个类开始，看看 setBackgroundResourece() 方法。

    public void More ...setBackgroundResource(int resid) {
        if (resid != 0 && resid == mBackgroundResource) {
            return;
        }

        Drawable d = null;
        if (resid != 0) {
            d = mContext.getDrawable(resid);
        }
        setBackground(d);
        mBackgroundResource = resid;
    }

其实就是获取一个 Drawable 对象。然后找到 Drawable 这个类，android.graphics.drawable.Drawable 是一个抽象类，所以咱们需要去找它的实现类，实现类就是 AnimationDrawable 。


然后找到 AnimationDrawable 这个类。AnimationDrawable 是 Drawable 的一个子类。在这个类的注释里，咱们发现了下面的内容：

> An object used to create frame-by-frame animations, defined by a series of Drawable objects, which can be used as a View object's background.
> The simplest way to create a frame-by-frame animation is to define the animation in an XML file, placed in the res/drawable/ folder, and set it as the background to a View object. Then, call start() to run the animation.

说明咱们没有找错，就是它了。

咱们还找到，光 setBackgroundResource() 是不够的，还得调用 start 方法。咱们可以看到，AnimationDrawable 还继承了 Runnable 接口，当然了，不是调用了 start() 方法就表示它会在另外一个线程里了，这里的设计不是为了多线程，这个以后咱们再分析。start() 方法调用了run() 方法，run() 方法里调用的是 nextFrame() 方法，nextFrame() 调用了 setFrame() 方法，同时，还调用了 scheduleSelf() 方法，其中有个参数就是 duration，大概的意思是在规定的时候后还会在调用这一系列的方法，就这样一帧一帧的变化。

在 inflate() 方法里，从 xml 里解析出 drawable 信息，然后调用了 mAnimationState.addFrame() 方法。

