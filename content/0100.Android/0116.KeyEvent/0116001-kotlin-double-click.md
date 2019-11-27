# Kotlin 中优雅的解决快速点击
- Kotlin,快速点击,双击,点击事件
- 时间：2019.11.25

在客户端开发经常碰见控件快速点击的问题。测试人员在进行暴力测试的时候，经常会对着某个按钮狂点，然后给我们提一堆 bug，解决这种 bug 不需要太高的技术要求，但是消耗了我们大量的工作量。

我们终究需要一种优雅的方案，来全面的避免类似问题的产生。

## 方案一 记录最后一次点击时间戳

在很多项目中都看到这样的工具类，**FastClickUtils**  这种工具类主要是获取当前时间戳，和上一次时间戳做比较，如果两个时间的间隔小于某个值，比如 1000 毫秒，那么认为是快速点击，直接 return。

    class FastClickUtils{
        private static final long mLastClickTime = 0L

        public static boolean isFastClick(){
            long time = System.currentTimeMills();
            if(time - mLastClickTime > 1000){
                return false;
            }
            mLastClickTime = time;
            return true;
        }

    }

    btn.setOnClickListener(new OnClickListener(){

        public void onClick(View view){
            if(FastClickUtils.isFastClick()){
                return;
            }
            // do somethings
        }
    });



这种方案有诸多缺点。 

 - 每个 click 事件都需要增加这么几行代码
 - 工具类全靠一个静态变量控制，不安全。
 - 万一多加了一次判断，那就完蛋了。
 - 容易忘。我们之前的项目大量采用这种方案，而开发中我们主要精力放在了业务功能的实现上，并没有特别关注快速点击的问题，有些测试人员会特别在意，在某一轮测试中，会集中提这类的bug，而有些测试人员并不关注。


## 方案二 封装一个 OnClickListener

和第一个方案类似，只是把代码封装到一个自定义的 OnClickLitener 中。

    abstract class SingleClickListener implements View.OnClickListener{

        private long mLastClickTime = 0L

        public void onClick(View view){
            // 
            if(time - mLastClickTime < 1000){
                onSingleClick(view);
            }
        }

        protected abstract void onSingleClick(View view);

    }


这个写法 mLastClickTime 为每个 SingleClickListener 私有的成员变量，防快速点击的作用范围缩小到具体的一个控件，避免了一个工具类，一个静态变量控制所有控件的点击事件的问题。

缺点就是多了一个类，刚开始可能不大习惯。习惯之后或者成为团队规范后，其实还好。


## 方案三 view.setEnabled(false) 避免快速点击

前面两种方案都是通过时间戳比较来判断快速点击的。而 **view.setEnabled(false)**  可以让控件失去点击事件的捕获。

可以在 **FastClickUtils** 中增加一个 lock 的方法，在控件第一个点击事件发生的时候，同时让控件置于 enable = false 的状态，1000 毫秒后，再让控制 enabled = true 。


    public static void lock(final View view) {
        view.setEnabled(false);
        view.postDelayed(new Runnable() {
            @Override
            public void run() {
                view.setEnabled(true);
            }
        }, 1000);
    } 

这种写法同样可以把防止快速点击的范围缩小到具体的控件上，避免了误伤。缺点和第一个方案类似，每个 click 事件都需要那么几行狗皮膏药的代码。

## 方案四 SingleClickListener 的 view.setEnabled(false) 版本

方案四其实就是方案二采用方案三的方案。优缺点和方案二大致相同。

## 方案五 Kotlin inline 

到了 Kotlin 时代，有一个更加优雅的解决办法。

    inline fun View.setOnSingleClickListener(crossinline onClick: () -> Unit, delayMillis: Long) {
        this.setOnClickListener {
            this.isClickable = false
            onClick()
            this.postDelayed({
                this.isClickable = true
            }, delayMillis)
        }
    }

通过 inline 关键字，给 View 及其所有子类拓展了一个 setOnSingleClickListener 方法。isClickable 替换了方案三的 setEnabled 只是避免 enbaled 变化后引起控件 state 样式的变化。

## 方案六 RxAndroid 方案

RxAndroid 也有比较优雅的方案，

    RxView.clicks(view)
        .throttleFirst(1, TimeUnit.SECONDS)
        .subscribe(new Consumer<Object>() {
            @Override
            public void accept(Object o) throws Exception {
                // do something
            }
         });

## 方案七 AOP 方案

这属于一种高（炫）级（技）的方案，利用 AOP 把工作交给编译器，好处是代码干净。

