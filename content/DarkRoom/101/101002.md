# Android 用注解来提升代码质量
- Android,注解,annotation
- 2018.07.13

Android 提供了一个注解的 support 包，这个注解包配合 IDE 可以用来提升我的代码质量，很多人会因为觉得编写代码增加注解会显得很繁琐而放弃掉使用注解，但是却忽略了注解给代码带来的好处。

Android 提供了一个注解的 support 包，一般我们都不需要声明引入，新建项目或者引入其他 Android support 包的话，都会引入这个 support 包。

	dependencies {
    	compile 'com.android.support:support-annotations:22.2.0'
	}

使用最新版本就可以了。

这个 support 包有很多注解，建议项目中，能用的尽量都可以用一下。这样可以让工具来帮助你规避风险。

我们平时非常头疼的空指针异常，NullPointerException 一直是我们开发中最常见的问题。

## 过度保护

过度保护是一个比较常见的情况。在方法外面保护了一次，在方法里面又保护了一次，为什么会这样，因为大家都害怕空指针，所以在写代码的时候，不管会不会碰见，先判断一下再说，形成习惯了。这种情况没有任何的坏处，除了有点浪费和代码量冗余外，没有太多的副作用。

## 忘记保护

忘记保护是致命的，我们经常会因为这个摔跟头，很多的高级别 bug 都是他引起的。虽然我们以及凭借经验，进行了足够多的空判断了，但是总有那么多些出乎意外的事情发生。


## NonNull 和 Nullable

这是两个比较重要的注解 @NonNull 和 @Nullable 。这两个注解在一定程度上，可以帮助我们规避一些风险。比如下面的例子

	public void run1(@NonNull String name){

	}

	public void run2(String name){

	}

	public void test(){
		String name = null;
		run1(name);
		run2(name);
	}


相比 run2(String name) 方法，run1(@NonNull String name) 方法多了一个注解，所以当我们在调用 run2 方法的时候，如果存在 null 的情况，IDE 会对我们进行警告的。（别跟我说程序员可以忽略警告～～）

所以，这些注解的作用是帮助细心的你，发现问题，规避风险。你要不细心没就办法了～～

## 其他注解

其他注解可能使用频率不会那么高，但是也是很有用的，建议有能力的还是多用心关注一下，没有能力的也要关注。
