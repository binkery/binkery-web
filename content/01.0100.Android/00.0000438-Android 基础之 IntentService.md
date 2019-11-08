# Android 基础之 IntentService
- Android,IntentService

IntentService 是 Service 的子类，主要的功能是在一个单独的线程里，处理来自主线程的任务，这些任务被放入到一个工作队列里，一个个顺序的执行。适用于那些不应该放在主线程去做，但是又不需要多线程的场景中。

IntentService 主要完成：

 - 创建一个线程。这个线程用来处理来自主线程的任务。Creates a default worker thread that executes all intents delivered to onStartCommand() separate from your application's main thread.
 - 创建一个队列。在同一时刻，只进行一个任务，这里没有多线程。Creates a work queue that passes one intent at a time to your onHandleIntent() implementation, so you never have to worry about multi-threading.
 - 自动停止。当任务队列里的任务都执行完成了，IntentService 会自动停止，释放资源，所以你不需要主动调用 stopSelf() 方法。Stops the service after all start requests have been handled, so you never have to call stopSelf().
 - 默认的，onBind() 方法返回 null 。Provides default implementation of onBind() that returns null.
 - 默认实现了 onStartCommand() 方法。这个方法会把任务放入到工作队列里，并且在工作线程里顺序执行。你需要做的就是实现 onHnadleIntent() 方法。Provides a default implementation of onStartCommand() that sends the intent to the work queue and then to your onHandleIntent() implementation.

下面是官方文档的例子

    public class HelloIntentService extends IntentService {
    
      /** 
       * A constructor is required, and must call the super IntentService(String)
       * constructor with a name for the worker thread.
       */
      public HelloIntentService() {
          super("HelloIntentService");
      }
    
      /**
       * The IntentService calls this method from the default worker thread with
       * the intent that started the service. When this method returns, IntentService
       * stops the service, as appropriate.
       */
      @Override
      protected void onHandleIntent(Intent intent) {
          // Normally we would do some work here, like download a file.
          // For our sample, we just sleep for 5 seconds.
          long endTime = System.currentTimeMillis() + 5*1000;
          while (System.currentTimeMillis() < endTime) {
              synchronized (this) {
                  try {
                      wait(endTime - System.currentTimeMillis());
                  } catch (Exception e) {
                  }
              }
          }
      }
    }

你需要做的事情就是 ： 
 - 写一个构造方法。有参无参随意，重点是需要调用父类的构造方法 super("service name"); 传递一个字符串，用来当作工作线程的名字。
 - 实现 onHandleIntent(Intent intent) 方法。这里写你具体的业务逻辑代码。

后续咱们来分析一下 IntentService 的源码，加深理解。<http://blog.binkery.com/android/service/intent_service_code.html>
