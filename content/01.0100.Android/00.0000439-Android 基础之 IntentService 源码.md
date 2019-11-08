# Android 基础之 IntentService 源码
- Android,IntentService,源码

*IntentService* 位于 android.app 包下面，是 Service 的一个子类。用来帮助你在后台使用一个线程来执行一些来自主线程的任务。<http://blog.binkery.com/android/service/intent_service.html> 这里有对 IntentService 的一些分析，下面是 IntentService 的源码，看完源码就更明白了。我去掉了源码里带的注释。

    public abstract class IntentService extends Service {
        private volatile Looper mServiceLooper;
        private volatile ServiceHandler mServiceHandler;
        private String mName;
        private boolean mRedelivery;
    
        private final class ServiceHandler extends Handler {
            public ServiceHandler(Looper looper) {
                super(looper);
            }
    
            @Override
            public void handleMessage(Message msg) {
                onHandleIntent((Intent)msg.obj);
                stopSelf(msg.arg1);
            }
        }
    
        public IntentService(String name) {
            super();
            mName = name;
        }
    
        public void setIntentRedelivery(boolean enabled) {
            mRedelivery = enabled;
        }
    
        @Override
        public void onCreate() {
            super.onCreate();
            HandlerThread thread = new HandlerThread("IntentService[" + mName + "]");
            thread.start();
    
            mServiceLooper = thread.getLooper();
            mServiceHandler = new ServiceHandler(mServiceLooper);
        }
    
        @Override
        public void onStart(Intent intent, int startId) {
            Message msg = mServiceHandler.obtainMessage();
            msg.arg1 = startId;
            msg.obj = intent;
            mServiceHandler.sendMessage(msg);
        }
    
        @Override
        public int onStartCommand(Intent intent, int flags, int startId) {
            onStart(intent, startId);
            return mRedelivery ? START_REDELIVER_INTENT : START_NOT_STICKY;
        }
    
        @Override
        public void onDestroy() {
            mServiceLooper.quit();
        }
    
        @Override
        public IBinder onBind(Intent intent) {
            return null;
        }
    
        protected abstract void onHandleIntent(Intent intent);
    }

 - 构造器。IntentService 的子类的构造器必须调用该类的 IntentService(String name) 构造器，因为它需要一个字符串当成线程的名字。
 - IntentService 创建了一个工作线程。
 - IntentService 创建了一个工作队列。 ServiceHandler 是一个 Handler , 用它来实现队列的管理，它的 Looper 是工作线程的 Looper ,所以它和 IntentService 不再一个线程里，也就是不在主线程里。
 - 在 Handler 里，会先调用 onHandleIntent(Intent) 方法，然后调用 stopSelf();所以你不用关心 IntentService 生命周期的问题。
 - 你需要实现 onHandleIntent(Intent intent) 方法。你接受到的 Intent 就是主线程 startService 时发送的 Intent 。

看完代码，你就可以放心的使用了。

