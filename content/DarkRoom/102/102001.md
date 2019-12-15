# Android onSaveInstanceState 的使用
- android,activity,onSaveInstanceState,
- 2018.05.23

onSaveInstanceState() 方法是 Activity 中用来保存数据的 API，它将方便你在 Activity 的生命周期中存储一些比较暂时性的数据。

## onSaveInstanceState 使用

### 存数据

重写 `onSaveInstanceState(Bundle savedInstanceState)` 方法，把你应用关心的数据存储到 `Bundle` 中。代码大概如下：

    @Override
    public void onSaveInstanceState(Bundle savedInstanceState) {
      super.onSaveInstanceState(savedInstanceState);
      // Save UI state changes to the savedInstanceState.
      // This bundle will be passed to onCreate if the process is
      // killed and restarted.
      savedInstanceState.putBoolean("MyBoolean", true);
      savedInstanceState.putDouble("myDouble", 1.9);
      savedInstanceState.putInt("MyInt", 1);
      savedInstanceState.putString("MyString", "Welcome back to Android");
      // etc.
    }

`Bundle` 中的数据是以键值对的形式存储的。NVP（Name-Value Pair）键值对。


### 取数据

在 Activity 的 `onCreate()` 和 `onRestoreInstanceState()` 方法中，你可以得到这个 `Bundle`。`onRestoreInstanceState()` 方法大概如下：

    @Override
    public void onRestoreInstanceState(Bundle savedInstanceState) {
      super.onRestoreInstanceState(savedInstanceState);
      // Restore UI state from the savedInstanceState.
      // This bundle has also been passed to onCreate.
      boolean myBoolean = savedInstanceState.getBoolean("MyBoolean");
      double myDouble = savedInstanceState.getDouble("myDouble");
      int myInt = savedInstanceState.getInt("MyInt");
      String myString = savedInstanceState.getString("MyString");
    }

这里有几篇官方的文档，建议阅读一下。

* [`onCreate`](http://developer.android.com/reference/android/app/Activity.html#onCreate(android.os.Bundle))
* [`onSaveInstanceState`](http://developer.android.com/reference/android/app/Activity.html#onSaveInstanceState(android.os.Bundle))

### 关于持久存储

`savedInstanceState` 只用来存储 Activity 有关系的数据，这些数据的生命周期和 Activity 相关。这种是数据可以认为是临时数据，并不是持久数据（persistent data）。一般情况下，它比较适合存储用户的临时表单数据之类的数据。

> Note that it is important to save persistent data in `onPause()` instead of `onSaveInstanceState(Bundle)` because the later is not part of the lifecycle callbacks, so will not be called in every situation as described in its documentation.

这个文档告诉我们如果有需要持久存储的数据，应该在 `onPause()` 方法中保存数据。事实上，`onSaveInstanceState(Bundle)` 方法并不是 Activity 生命周期的方法。

> This method is called before an activity may be killed so that when it
  comes back some time in the future it can restore its state. For
  example, if activity B is launched in front of activity A, and at some
  point activity A is killed to reclaim resources, activity A will have
  a chance to save the current state of its user interface via this
  method so that when the user returns to activity A, the state of the
  user interface can be restored via `onCreate(Bundle)` or
  `onRestoreInstanceState(Bundle)`.

`onSaveInstanceState(Bundle)` 方法会在 Activity 被 kill 掉之前调用。假设 Activity B 被启动，Activity A 可能会因为资源回收的原因，被 Kill 掉，那么当从 Activity B 回到 Activity A 的时候，你可以从 `onCreate(Bundle)` 或者 `onRestoreInstanceState(Bundle)` 方法获得之前保存的状态（state）。

需要持久的数据存储，你需要 SQLite 数据库、文件或者 preferences。[Saving Persistent State](http://developer.android.com/reference/android/app/Activity.html#SavingPersistentState) 这个文档告诉你如何存储数据。

该文章来源于 https://stackoverflow.com/questions/151777/saving-android-activity-state-using-save-instance-state，由[spacepage.top](https://spacepage.top/) 编辑和整理。
