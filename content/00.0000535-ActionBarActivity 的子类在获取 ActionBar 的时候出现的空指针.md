# ActionBarActivity 的子类在获取 ActionBar 的时候出现的空指针
- 2017-12-15 15:01:52
- Android开发中的那些坑
- android,actionbar,

<!--markdown-->当一个 Activity 继承于 ActionBarActivity，并且使用了  <item name="android:windowNoTitle">true</item> 样式，或者在 Java 代码中调用了 requestWindowFeature( Window.FEATURE\_NO\_TITLE);  的情况下，就会出现这样的 bug。

## 空指针日志
    java.lang.NullPointerException: Attempt to invoke virtual method 'android.content.Context android.app.ActionBar.getThemedContext()' on a null object reference
    at android.support.v7.app.ActionBarImplICS.getThemedContext(ActionBarImplICS.java:287)
    at android.support.v7.app.ActionBarImplJB.getThemedContext(ActionBarImplJB.java:20)
    at android.support.v7.app.ActionBarActivityDelegate.getMenuInflater(ActionBarActivityDelegate.java:98)
    at android.support.v7.app.ActionBarActivity.getMenuInflater(ActionBarActivity.java:71)
    at android.app.Activity.onCreatePanelMenu(Activity.java:2921)
    at android.support.v4.app.FragmentActivity.onCreatePanelMenu(FragmentActivity.java:224)
    at android.support.v7.app.ActionBarActivity.superOnCreatePanelMenu(ActionBarActivity.java:232)
    at android.support.v7.app.ActionBarActivityDelegateICS.onCreatePanelMenu(ActionBarActivityDelegateICS.java:147)
    at android.support.v7.app.ActionBarActivity.onCreatePanelMenu(ActionBarActivity.java:199)
    at android.support.v7.app.ActionBarActivityDelegateICS$WindowCallbackWrapper.onCreatePanelMenu(ActionBarActivityDelegateICS.java:285)
    at com.android.internal.policy.impl.PhoneWindow.preparePanel(PhoneWindow.java:601)
    at com.android.internal.policy.impl.PhoneWindow$DecorView.dispatchKeyShortcutEvent(PhoneWindow.java:2450)
    at android.view.ViewRootImpl$ViewPostImeInputStage.processKeyEvent(ViewRootImpl.java:4742)
    at android.view.ViewRootImpl$ViewPostImeInputStage.onProcess(ViewRootImpl.java:4681)
    at android.view.ViewRootImpl$InputStage.deliver(ViewRootImpl.java:4188)
    at android.view.ViewRootImpl$InputStage.onDeliverToNext(ViewRootImpl.java:4241)
    at android.view.ViewRootImpl$InputStage.forward(ViewRootImpl.java:4207)
    at android.view.ViewRootImpl$AsyncInputStage.forward(ViewRootImpl.java:4344)
    at android.view.ViewRootImpl$InputStage.apply(ViewRootImpl.java:4215)
    at android.view.ViewRootImpl$AsyncInputStage.apply(ViewRootImpl.java:4401)
    at android.view.ViewRootImpl$InputStage.deliver(ViewRootImpl.java:4188)
    at android.view.ViewRootImpl$InputStage.onDeliverToNext(ViewRootImpl.java:4241)
    at android.view.ViewRootImpl$InputStage.forward(ViewRootImpl.java:4207)
    at android.view.ViewRootImpl$InputStage.apply(ViewRootImpl.java:4215)
    at android.view.ViewRootImpl$InputStage.deliver(ViewRootImpl.java:4188)
    at android.view.ViewRootImpl$InputStage.onDeliverToNext(ViewRootImpl.java:4241)
    at android.view.ViewRootImpl$InputStage.forward(ViewRootImpl.java:4207)
    at android.view.ViewRootImpl$AsyncInputStage.forward(ViewRootImpl.java:4377)
    at android.view.ViewRootImpl$ImeInputStage.onFinishedInputEvent(ViewRootImpl.java:4547)
    at android.view.inputmethod.InputMethodManager$PendingEvent.run(InputMethodManager.java:2331)
    at android.view.inputmethod.InputMethodManager.invokeFinishedInputEventCallback(InputMethodManager.java:1955)
    at android.view.inputmethod.InputMethodManager.finishedInputEvent(InputMethodManager.java:1946)
    at android.view.inputmethod.InputMethodManager$ImeInputEventSender.onInputEventFinished(InputMethodManager.java:2308)
    at android.view.InputEventSender.dispatchInputEventFinished(InputEventSender.java:141)
    at android.os.MessageQueue.nativePollOnce(Native Method)
    at android.os.MessageQueue.next(MessageQueue.java:148)
    at android.os.Looper.loop(Looper.java:151)
    at android.app.ActivityThread.main(ActivityThread.java:5691)
    at java.lang.reflect.Method.invoke(Native Method)
    at java.lang.reflect.Method.invoke(Method.java:372)
    at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:959)
    at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:754)

## 原因分析

目前可以确定的是，这是 google support v7 包中 ActionBarActivity 的 bug，以下是这两个 issue 的链接：

1. <https://code.google.com/p/android/issues/detail?id=61394>
2. <https://code.google.com/p/android/issues/detail?id=66873>

问题的原因是，如果一个 Activity 继承于 ActionBarActivity，并且在 theme 中设置 <item name="android:windowNoTitle">true</item> 或者在代码中调用 requestWindowFeature( Window.FEATURE\_NO\_TITLE)。
那么在这个 Activity，如果手机上有物理 MENU 键的话，用户点击 MENU ，Activity 中创建 menu panel 的过程中，如果它是 ActionBarActivity 的子类，那么就会试图去获取 ActionBar，而这个时候因为是 NO TITLE 的，所以 ActionBar 是空的，而 Google 的 support 中的代码并没有做好这个保护，所以就会出现一个空指针异常。而这个异常不仅仅是在 MENU 键的时候出现，长按某个 View，在试图弹出 ContextMenu 的情况下也会出现这样的问题，以及任何 getSupportActionBar() 都会返回 null，如果没有做非空判断直接调用 ActionBar 的方法的话，也会出现空指针。

所以，对于网上一个 workaround 的 solution，在 Activity 中屏蔽 MENU 按钮只是一个临时的方案，并不能根本解决这个问题。

解决问题的办法有：

1. 不使用 ActionBarActivity ，事实上，ActionBarActivity 也已经被 Google 抛弃了。
2. 使用 ActivityBarActivity 的话，不要使用带 <item name="android:windowNoTitle">true</item> 的样式，或者调用 requestWindowFeature( Window.FEATURE_NO_TITLE);
3. 使用新的 support 包，在新的 support 包，如果你使用了 ActionBar，IDE 会提示你过期的，并且建议使用 android.support.v7.app.AppCompatActivity 代替。即使你使用的是 ActionBarActivity，那么这个 ActionBarActivity 也是继承于 AppCompatActivity，并且是一个空的实现。

针对 Google 的那两个 issue，最终 Google 也没有真正的解决，从 v7 19.0.1 到 21，直到 22 的时候，ActionBarActivity 被 AppCompatActivity 替代，issue #61394 被设置为 Obsolete。

## 参考

* <http://stackoverflow.com/questions/22430731/nullpointerexception-in-android-support-v7-app-actionbarimplics-getthemedcontext>