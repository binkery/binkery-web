# Android Touch 事件机制
- 2016-03-21 09:19:20
- Android
- android,touch,

<!--markdown-->Android Touch 事件机制。有很多通过 Log 输出的方式去分析　Android Touch　事件的分发机制，我这里是通过阅读源代码的方式来分析。

Note：这里贴出的代码有所删减。


<!--more-->

## View 的分析
### 从 setOnTouchListener 入手
我是以逆推的方式来分析。跟 Touch 有关的，首先想到是　setOnTouchListener。

    public void setOnTouchListener(OnTouchListener l) {
        getListenerInfo().mOnTouchListener = l;
    }

getListenerInfo() 是获取一个　ListenerInfo　类的实例，咱就不用关心它是怎么设计，怎么实现的，咱们就关心　mOnTouchListener 是怎么使用的。

### dispatchTouchEvent

然后在　dispatchTouchEvent(MotionEvent) 里找到了 mOnTouchListener 的使用。

    public boolean dispatchTouchEvent(MotionEvent event){
        ListenerInfo li = mListenerInfo;
        if (li != null && li.mOnTouchListener != null && (mViewFlags & ENABLED_MASK) == ENABLED && li.mOnTouchListener.onTouch(this, event)) {
            return true;
        }
        if(onTouchEvent(event)){
            return true;
        }
    }

在 dispatchTouchEvent() 方法里，如果 mOnTouchListener 不为空，就调用 mTouchListener.onTouch() 方法，如果返回　true ,那么　dispatchTouchEvent 也就返回 true .　如果　listener 返回　false ,那么就调用　onTouchEvent()　方法。咱们再去看看 onTouchEvent() 方法。

### onTouchEvent

onTouchEvent(MotionEvent) 方法比较长，我就不贴那么多代码。看方法的名字大概能猜出这段代码主要就是判断　View 是否获得焦点，是否需要触发　click 事件，或者　long click 事件，还有就是　setPressed 的状态等等。

    public boolean onTouchEvent(MotionEvent event){
        requestFocus();
        setPressed(true/false);
        performClick();
    }
	
这里就是执行　click 事件。

    public boolean performClick() {
        mOnClickListener.onClick(this);
    }

### 总结
一个 View 的 Touch 事件从 dispatchTouchEvent() 方法开始，如果这个 View 有 OnTouchListner ，则先调用 OnTouchListener 的回调，如果回调返回 true，则事件终止，如果事件返回 false，则调用 View 的 onTouchEvent() 方法。在 onTouchEvent() 方法有可能会触发 OnClickListener 的回调。

## ViewGroup 的分析
### dispatchTouchEvent

上面分析的是　View , View 的事件从哪来，肯定是从它的容器来，ViewGroup 就是所有容器的父类，咱们就去看看 ViewGroup 是怎么处理的。首先找到的是　dispatchTouchEvent(MotionEvent)

    public boolean dispatchTouchEvent(MotionEvent ev) 
	final boolean intercepted;
	intercepted = onInterceptTouchEvent(ev);
	if(!intercepted){
	    for(children){
	        dispatchTransformedTouchEvent(ev, false, child, idBitsToAssign)
	    }
	}

ViewGroup 的　dispatchTouchEvent() 方法首先调用的是　onInterceptTouchEvent(MotionEvent)　方法。如果 onInterceptTouchEvent() 返回　false,那么就遍历子控件，也就是　children　。

在　dispatchTransformedTouchEvent　里，如果 child 不为空，那么调用 dispatchTouchEvent(MotionEvent) 方法。如果　child 是　View ，那么就执行上面咱们分析的逻辑，如果是　ViewGroup ，那么就执行咱们现在分析的。

    private boolean dispatchTransformedTouchEvent(MotionEvent event, boolean cancel, View child, int desiredPointerIdBits)

        if (child == null) {
            handled = super.dispatchTouchEvent(event);
        } else {
            handled = child.dispatchTouchEvent(event);
        }

### onInterceptTouchEvent

在ViewGroup 里，onInterceptTouchEvent(MotionEvent) 很简单的只返回了　false.如果你自定义了一个ViewGroup，看你的需求重写这个方法。

    public boolean onInterceptTouchEvent(MotionEvent ev) {
        return false;
    }

在 ViewGroup 里没有找到　onTouchEvent 的方法，但是ViewGroup 继承于 View，所以，ViewGroup 也继承了 onTouchEvent 方法。

### 总结

ViewGroup 的 Touch 事件也是从 dispatchTouchEvent 方法开始。会先调用 onInterceptTouchEvent() 方法，如果返回 true，表示事件被截住，不会传递给 children；如果返回 false，则事件会传递给 children。Children 可能是 View ，也可能是ViewGroup，但都会调用它们的 dispatchTouchEvent 方法。 

## Activity

ViewGroup 的 Touch 事件从哪来呢？应该是从 Activity 里来，咱们去看看 Activity 的代码。在Activity 里，发现了onTouchEvent(MotionEvent) 和 dispatchTouchEvent(MotionEvent) 方法，但是很不幸，它们都交给了一个叫 mWindow 的对象去处理了。不过可以知道的是 onTouchEvent 是在 dispatchTouchEvent() 里被调用的，这个设计跟 View/ViewGroup 是一致的。

    public boolean onTouchEvent(MotionEvent event) {
        if (mWindow.shouldCloseOnTouch(this, event)) {
            finish();
            return true;
        }
        return false;
    }

    public boolean dispatchTouchEvent(MotionEvent ev) {
        if (ev.getAction() == MotionEvent.ACTION_DOWN) {
            onUserInteraction();
        }
        if (getWindow().superDispatchTouchEvent(ev)) {
            return true;
        }
        return onTouchEvent(ev);
    }

### 总结
Activity 的 touch 事件都交给了 Window 处理。

## Window 

另外有句废话，通过看源码，你会发现，mWindow 有时候是直接使用，有时候是通过 getWindow() 获得的。好吧，怎么不关心他们的代码写得怎么样，咱们关心怎么实现的就行。Activity 的 dispatchTouchEvent() 方法调用的是 mWindow 的superDispatchTouchEvent() 方法， mWindow 是 Window 的一个实例，Window 又是一个抽象类。

    public abstract class Window

不过在 Window 类的注释上，咱们发现了这么一段话，大概意思是说 Window 有一个实现类 android.policy.PhoneWindow .

>The only existing implementation of this abstract class is android.policy.PhoneWindow, which you should instantiate when needing a Window.

### 总结
Window 是一个抽象类，并没有直接处理 Activity 交给它的 touch 事件，而是 Window 的子类 PhoneWindow 实现了 touch 事件的处理。

## PhoneWinow

PhoneWinow 其实在 com.android.internal.policy.impl 包里，找到 PhoneWindow 后，咱们找 superDispatchTouchEvent() 方法。

    @Override
    public boolean superDispatchTouchEvent(MotionEvent event) {
        return mDecor.superDispatchTouchEvent(event);
    }

### mDecor 的定义

PhoneWindow 调用 mDecor 的 superDispatchTouchEvent 方法。mDecor 是什么玩意？mDecor 是 DecorView 的一个实例。

    // This is the top-level view of the window, containing the window decor.
    private DecorView mDecor;

    // This is the view in which the window contents are placed. It is either
    // mDecor itself, or a child of mDecor where the contents go.
    private ViewGroup mContentParent;

### PhoneWindow.DecorView

PhoneWindow 定义了一个 DecorView 的实例mDecor，同时也定义了一个 ViewGroup 的实例 mContentParent，这个 ViewGroup 一会会用到。那么又是什么玩意呢？它是PhoneWindow 的一个内部类，继承于 FrameLayout ，也就是它是一个 View，也是一个 ViewGroup。

    private final class DecorView extends FrameLayout

### mDecor 的实例化

那么 mDecor 在什么时候创建呢？咱们找到了一个叫 installDecor() 的方法，这里实例化了 mDecor ,也实例化了 mContentParent .

    private void installDecor() {
        if (mDecor == null) {
            mDecor = generateDecor();
        }
        if (mContentParent == null) {
            mContentParent = generateLayout(mDecor);
        }
    }

generateDecor() 的方法很简单，就是 new 了一个 DecorView 对象。

    protected DecorView generateDecor() {
        return new DecorView(getContext(), -1);
    }

generateLayout 的方法就很复杂，其实也是实例化了一个 FrameLayout.代码我就不全贴出来了。

    protected ViewGroup generateLayout(DecorView decor){
        mDecor.startChanging();
        
        View in = mLayoutInflater.inflate(layoutResource, null);
        decor.addView(in, new ViewGroup.LayoutParams(MATCH_PARENT, MATCH_PARENT));
        mContentRoot = (ViewGroup) in;
        
        ViewGroup contentParent = (ViewGroup)findViewById(ID_ANDROID_CONTENT);
        
        mDecor.finishChanging();
	
        return contentParent;
    }

在 generateLayout 方法里，inflate 了一个 View ,并且把它加入到 mDecor(一个FrameLayout) 里。然后通过 findViewById() 方法，获取到一个 ViewGroup ,也就是最终的 mContentParent .mDecor.startChanging() 和 mDecor.finishChanging() 的作用是什么呢？鬼知道它们是干啥的，我贴出来就是想让大家看看，一会用 mDecor ,一会用 decor，这是几个意思？！

### mDecor 和 mContentParent 的关系

mDecor 和 mContentParent 的关系还不是很清晰，到底啥关系？现在咱们要去看看 findViewById() . PhoneWindow 没有这个方法，在 Window 里找到了。

    public View findViewById(int id) {
        return getDecorView().findViewById(id);
    }

它调用 getDecorView().findViewById(id) ，那么咱们找 getDecorView()。

    public abstract View getDecorView();

结果是一个抽象方法，那么咱们再回去 PhoneWindow 找，返回的是 PhoneWindow 的 mDecor。

    @Override
    public final View getDecorView() {
        if (mDecor == null) {
            installDecor();
        }
        return mDecor;
    }

也就是说，mContentParent = mDecor.findViewById(id)，这样就可以理解 mContentParent 和 mDecor 的关系了。但是它们俩的关系跟咱们 touch 事件有毛关系啊？

### DecorView.superDispatchTouchEvent(MotionEvent event)

咱们从 Activity 的 dispatchTouchEvent 一路追到 mDecor 来了,Activity 的 dispatchTouchEvent 其实就是调用  mDecor.superDispatchTouchEvent(event)， DecorView 的 superDispatchTouchEvent 的实现如下。

        public boolean superDispatchTouchEvent(MotionEvent event) {
            return super.dispatchTouchEvent(event);
        }

## DecorView 与 setContentView()

DecorView 的 super 就是 FrameLayout , FragmentLayout 是 ViewGroup 的子类，也就是咱们上面分析的。然后咱们写的布局 Layout 是怎么跟 mDecor 扯上关系的。咱们去看看 setContentView()。下面是 Activity 的代码。

    public void setContentView(int layoutResID) {
        getWindow().setContentView(layoutResID);
        initActionBar();
    }

Window 的 setContentView(int) 代码，是一个抽象方法，咱们去 PhoneWindow 找。

    public abstract void setContentView(int layoutResID);

### setContentView() 的最终实现

PhoneWindow 的 setContentView(int) 代码。这里是 Activity.setContentView 的最终实现。

    @Override
    public void setContentView(int layoutResID) {
        if (mContentParent == null) {
            installDecor();
        } 
        mLayoutInflater.inflate(layoutResID, mContentParent);
    }

installDecor() 方法就是实例化了 mDecor 和 mContentParent ， mDecor 是 mContentParent 的父容器，mContentParent 又是咱们通过 setContentview(int) 加载的 layout 的父容器。

所以，Activity 获取的 touch Event 通过 dispatchTouchEvent 最终交给了 mDecor 处理，mDecor 又是一个 View，它会调用它的 dispatchTouchEvent() 去处理分发 Touch Event。

### Activity 的 onTouchEvent() 方法
Activity 的 onTouchEvent() 方法最终也交给 PhoneWindow 的 DecorView ， DecorView 继承于 FrameLayout ，重写了 onTouchEvent() 方法：

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        return onInterceptTouchEvent(event);
    }

在 onTouchEvent() 方法里，直接调用 onInterceptTouchEvent(). onInterceptTouchEvent() 的代码我就不贴了，因为我没有看懂，大概就是对 Touch 事件的 X、Y 轴做边界检查。

## 总结

* Touch 事件从 Activity 的 dispatchTouchEvent() 开始，然后交给 View/ViewGroup 的 dispatchTouchEvent() 。如果 View/ViewGroup 的 dispatchTouchEvent() 没有消费，就交给Activity 的 onTouchEvent() 。

* ViewGroup 的 dispatchTouchEvent() 会先调用 onInterceptTouchEvent().如果 ViewGroup 的 onInterceptTouchEvent() 返回 true ，事件就不交给 ViewGroup 的 Children。如果 onInterceptTouchEvent() 返回 false，那么事件就继续交给 Children 的 dispatchTouchEvent()。

* View 的 dispatchTouchEvent() 会先调用 View 的 OnTouchListener 的回调，如果没有 OnTouchListener 或者 OnTouchListener 没有消费，就交给 OnTouchEvent() 方法。
