# Andoid 动画之二 视图动画 View Animation
- 2016-05-16 03:22:49
- Android
- android,动画,视图动画,补间动画,

<!--markdown-->You can use the view animation system to perform tweened animation on Views.看看官网的说明，View Animation 后面跟这一个 system ，说明视图动画是一套完整的动画系统。视图动画（View Animation）也经常被称为 Tween Animation，国内大多翻译为补间动画。

## Tween animation

先说说什么是 tween animation，跟帧动画不一样，帧动画是一帧一帧完整的渲染资源图片，而补间动画呢，通过给定的两个关键帧的参数，系统按照一定的算法计算出每一帧的图像。

## 帧

先说说帧，在一个时刻，你看见的图像是一帧，你看到的屏幕内容的变化，移动，都是通过一帧一帧不停的渲染到屏幕上的。假设屏幕的刷新频率是 60hz，那么相当于 16.67 ms 刷新一次屏幕。在帧动画里，咱们一般把 item 称为 帧，但是它跟屏幕渲染的帧明显不是等同的。假设咱们设置每item 的时长为 200 ms，也就是说，这个 item 将大概在屏幕保留 200 ms，而屏幕可能已经刷新了好几帧了。注意：这里不考虑丢帧等乱七八糟的情况。

在回到补间动画，补间动画通过给对象设置关键帧的参数，让系统自动去计算每帧具体渲染的图片。补间动画可以设置的参数有：位置 position，大小 size，旋转 rotation 和透明度 transparency。

## Android 实现

一般在项目里，咱们有两种方式使用补间动画，一种是 xml 定义，一种是 Java Code。

### xml

补间动画有个专门的目录 res/anim/ 。在这个目录下的每个文件的根元素可以是 <alpha\>,<scale\>,<translate\>和 <rotate> ，当然，如果一个组合动画的话，根元素还可以是 <set\> 。<set\> 里除了 <alpha\>等元素外，还可以是 <set\>。

上一个官网的例子： 

    <set android:shareInterpolator="false">
        <scale
            android:interpolator="@android:anim/accelerate_decelerate_interpolator"
            android:fromXScale="1.0"
            android:toXScale="1.4"
            android:fromYScale="1.0"
            android:toYScale="0.6"
            android:pivotX="50%"
            android:pivotY="50%"
            android:fillAfter="false"
            android:duration="700" />
        <set android:interpolator="@android:anim/decelerate_interpolator">
            <scale
               android:fromXScale="1.4"
               android:toXScale="0.0"
               android:fromYScale="0.6"
               android:toYScale="0.0"
               android:pivotX="50%"
               android:pivotY="50%"
               android:startOffset="700"
               android:duration="400"
               android:fillBefore="false" />
            <rotate
               android:fromDegrees="0"
               android:toDegrees="-45"
               android:toYScale="0.0"
               android:pivotX="50%"
               android:pivotY="50%"
               android:startOffset="700"
               android:duration="400" />
        </set>
    </set>


对应的 Java 代码： 

    ImageView spaceshipImage = (ImageView) findViewById(R.id.spaceshipImage);
    Animation hyperspaceJumpAnimation = AnimationUtils.loadAnimation(this, R.anim.hyperspace_jump);
    spaceshipImage.startAnimation(hyperspaceJumpAnimation);

### Java 实现

刚才上面的 Java 代码不是补间动画的 Java 实现，这里是配合 xml 文件，执行动画。咱们刚才可以看到，xml 文件中包含了 <set\>,<alpha\> 等元素，这些元素其实都是有其对应的 Java 类的，<set\> 对应的就是 AnimationSet，AnimationSet 是 Animation 的子类，除了 AnimationSet 之外，Animation 还有这么几个子类：AlphaAnimation,RotateAnimation,ScaleAnimation,TranslateAnimation 。补间动画的 Java 代码实现说的是，你可以通过创建 Animation 对象，然后调用 View 的 startAnimation 方法来实现动画。

具体不同的动画 xml 元素属性和 Animation 子类的属性基本都是对应的，这里不一一描述了。原理知道了，剩下的就是查文档的事了。

## Android 源码

咱们可以看到，不管是是 XML 实现，还是 Java 实现，无非就是构造出一个 Animation 对象，然后调用 View.startAnimation() 方法。

咱们前面说了，Animation 是一个抽象类，AnimationSet 和 AlphaAnimation 等都是它的子类。startAnimation() 方法调用了 setAnimation() 方法，调完后还调用了 invalidate() 方法。咱们这里先不讨论 invalidate() 方法怎么执行的，咱们回到 Animation 这个类里，咱们看到下面这个方法，这个方法就是动画的一个关键方法。

    /**
     * Gets the transformation to apply at a specified point in time. Implementations of this
     * method should always replace the specified Transformation or document they are doing
     * otherwise.
     *
     * @param currentTime Where we are in the animation. This is wall clock time.
     * @param outTransformation A transformation object that is provided by the
     *        caller and will be filled in by the animation.
     * @return True if the animation is still running
     */
    public boolean getTransformation(long currentTime, Transformation outTransformation) {
        if (mStartTime == -1) {
            mStartTime = currentTime;
        }

        final long startOffset = getStartOffset();
        final long duration = mDuration;
        float normalizedTime;
        if (duration != 0) {
            normalizedTime = ((float) (currentTime - (mStartTime + startOffset))) /
                    (float) duration;
        } else {
            // time is a step-change with a zero duration
            normalizedTime = currentTime < mStartTime ? 0.0f : 1.0f;
        }

        final boolean expired = normalizedTime >= 1.0f;
        mMore = !expired;

        if (!mFillEnabled) normalizedTime = Math.max(Math.min(normalizedTime, 1.0f), 0.0f);

        if ((normalizedTime >= 0.0f || mFillBefore) && (normalizedTime <= 1.0f || mFillAfter)) {
            if (!mStarted) {
                fireAnimationStart();
                mStarted = true;
                if (USE_CLOSEGUARD) {
                    guard.open("cancel or detach or getTransformation");
                }
            }

            if (mFillEnabled) normalizedTime = Math.max(Math.min(normalizedTime, 1.0f), 0.0f);

            if (mCycleFlip) {
                normalizedTime = 1.0f - normalizedTime;
            }

            final float interpolatedTime = mInterpolator.getInterpolation(normalizedTime);
            applyTransformation(interpolatedTime, outTransformation);
        }

        if (expired) {
            if (mRepeatCount == mRepeated) {
                if (!mEnded) {
                    mEnded = true;
                    guard.close();
                    fireAnimationEnd();
                }
            } else {
                if (mRepeatCount > 0) {
                    mRepeated++;
                }

                if (mRepeatMode == REVERSE) {
                    mCycleFlip = !mCycleFlip;
                }

                mStartTime = -1;
                mMore = true;

                fireAnimationRepeat();
            }
        }

        if (!mMore && mOneMoreTime) {
            mOneMoreTime = false;
            return true;
        }

        return mMore;
    }

其中调用了 applyTransformation() 方法，而这个方法在 Animation 里是一个空的方法，于是咱们去找它的子类看看，我找了 AplhaAnimation 这个类，方法的实现如下：


    /**
     * Changes the alpha property of the supplied {@link Transformation}
     */
    @Override
    protected void applyTransformation(float interpolatedTime, Transformation t) {
        final float alpha = mFromAlpha;
        t.setAlpha(alpha + ((mToAlpha - alpha) * interpolatedTime));
    }


通过一个计算，给 Transformation 更改了以下属性。在 View 的 draw(Canvas canvas) 方法里，在往 Canvas 上渲染的时候，会根据 Animation 对象和 Transformation 对象的相关的值，把当前的 View 渲染到 Canvas 上。所以，咱们可以看出，视图动画，View 本身的属性没有变化，变化的是渲染的时候。
