# Android 专题之广播
- 2016-03-22 03:55:08
- 
- 

<!--markdown--># Android 专题之广播

BroadcastReceiver 是 Android 的基础组件之一，其主题就是广播 Broadcast 。在 Android 里，系统和应用程序之间，应用程序和应用程序之间，应用程序的各个组件之间，都可以通过广播相互传递消息。

## 基础知识
[BroadcastReceiver 的基本知识](http://www.binkery.com/archives/91.html)


## BroadcastReceiver 的实现

要接收广播，首先你需要实现 BroadcastReceiver ，实现 BroadcastReceiver 很简单，继承于它，然后它就一个方法需要实现，onReceive() 。这个方法会在接收到广播的时候被调用。

    public class MyBroadcastReceiver extends BroadcastReceiver{
     
     　　public void onReceive(Context context, Intent intent){
            //do somethings
        }
    }

注意：BroadcastReceiver 实例在接收到广播的时候被实例化，然后 onReceive() 方法被调用，然后这个实例就被销毁了。所以，onReceive() 方法不能做太复杂的操作，系统只给你 10 秒钟的时间，否则可能会有 ANR 发生。在这个方法里也不适合开启线程，因为一旦 BroadcastReceiver 的实例被回收后，这个线程就无主了，很容易被系统 kill 掉的。

## 注册方式

实现完 BroadcastReceiver 后，我们需要注册，注册有两种：

> You can either dynamically register an instance of this class with Context.registerReceiver() or statically publish an implementation through the <receiver> tag in your AndroidManifest.xml.

1. 代码注册，比如在 Activity 的 onResume() 注册，在 onPause() 注销。


    IntentFilter filter = new IntentFilter("android.provider.Telephony.SMS_RECEIVED");  
    MyBroadcastReceiver receiver = new MyBroadcastReceiver();  
    registerReceiver(receiver, filter); 

注销

    unregisterReceiver(receiver);



2. 在 AndroidManifest.xml  \<receiver\> 标签里注册。


    <receiver android:name=".MyBroadcastReceiver">  
         <intent-filter>  
              <action android:name="android.intent.action.BOOT_COMPLETED"/>  
              <action android:name="android.provider.Telephony.SMS_RECEIVED"/>  
         </intent-filter>  
    </receiver>  


android:name 注明了接收者，intent-filter 注明了接收的过滤器，每个 action 注明了这个接收者会响应哪些具体的广播。

## 发送广播

有消费广播的地方，就有产生广播的地方。

    Context.sendBroadcast()

我们可以看到，分发广播的是 Context，不只是 Activity。


## 广播的分发机制

整个广播的分发机制有几个核心的类：Context,BroadcastReceiver,IntentFilter,Intent.其中 Intent 携带了广播所需要的数据，IntentFilter 声明了广播的规则。广播的分发和注册销毁都是通过 Context 来进行的。

## 普通广播

普通广播可以认为广播的接收者同一个时刻接收到同一个广播，虽然实际他们不可能同时占用CPU，但是可以大概的认为是同一时刻。它能保证所有接收者都能接收到，不相互影响。

## 有序广播

有序广播的意思就是广播的接收者之间是有优先级的。优先级高的优先接收处理广播，并且有权终止广播的继续发送。

## 粘性广播

## LocalBroadcastManager

当你期望你发出广播只在你的应用程序里被其他组件接收到，而不广播给其他应用程序的时候，一个本地广播会更加适合你。它更加高效，更加安全，节能环保。

## 系统广播