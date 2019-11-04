# AsyncTask 官方文档的简单翻译和理解
- 2015-03-06 07:03:18
- Android
- android,asynctask,

<!--markdown-->今天做项目遇到需要AsyncTask的东西，看了一下文档，这个类很好用，也很简单。

<!--more-->

> AsyncTask enables proper and easy use of the UI thread. This class allows to perform background operations and publish results on the UI thread without having to manipulate threads and/or handlers.

> An asynchronous task is defined by a computation that runs on a background thread and whose result is published on the UI thread. An asynchronous task is defined by 3 generic types, called Params, Progress and Result, and 4 steps, called onPreExecute, doInBackground, onProgressUpdate and onPostExecute.

这个类被用来在后台执行操作，并且通知UI线程，而不一定需要一个handler线程。

## AsyncTask's generic types

The three types used by an asynchronous task are the following:

* Params, the type of the parameters sent to the task upon execution.这是参数
* Progress, the type of the progress units published during the background computation.这是进度
* Result, the type of the result of the background computation.这是结果

## The 4 steps 一共有四个步骤

When an asynchronous task is executed, the task goes through 4 steps:

* **onPreExecute()**, invoked on the UI thread immediately（立即） after the task is executed. This step is normally used to setup the task, for instance by showing a progress bar in the user interface.
当一个task开始执行的时候，这个方法会被调用。这个方法可以不重写，我的那个项目中就没有用到，就看需求了。

* **doInBackground(Params...)**, invoked on the background thread immediately after onPreExecute() finishes executing. This step is used to perform background computation that can take a long time. The parameters of the asynchronous task are passed to this step. The result of the computation must be returned by this step and will be passed back to the last step. This step can also use publishProgress(Progress...) to publish one or more units of progress. These values are published on the UI thread, in the onProgressUpdate(Progress...) step.
在 onPreExecute()后，紧接着执行这个方法。

* **onProgressUpdate(Progress...)**, invoked on the UI thread after a call to publishProgress(Progress...). The timing of the execution is undefined. This method is used to display any form of progress in the user interface while the background computation is still executing. For instance, it can be used to animate a progress bar or show logs in a text field.
这个方法在 publishProgress(Progress...)被调用的时候执行。操作的执行时间是不明确的。在后台操作执行的时候，这个方法可以用来在UI显示一些进度或者日志之类的东西。

* **onPostExecute(Result)**, invoked on the UI thread after the background computation finishes. The result of the background computation is passed to this step as a parameter.
这个方法在整个操作执行完成后被调用。会获得一个Result对象。

## Cancelling a task取消task

A task can be cancelled at any time by invoking cancel(boolean). Invoking this method will cause subsequent calls to isCancelled() to return true. After invoking this method, onCancelled(Object), instead of onPostExecute(Object) will be invoked after doInBackground(Object[]) returns. To ensure that a task is cancelled as quickly as possible, you should always check the return value of isCancelled() periodically（周期地） from doInBackground(Object[]), if possible (inside a loop for instance.)通过调用cancel(boolean)，可以在任何时候停止这个task。
在调用这个方法后，isCancelled()将返回true。在这个方法被调用后，在 doInBackground(Object[])之后，onPostExecute(Object) 不会被调用，而是调用onCancelled(Object)。文档上建议在doInBackground(Object[])里周期性的检测isCancelled()的返回值。

## Threading rules规则

There are a few threading rules that must be followed for this class to work properly:

* The task instance must be created on the UI thread. 这个task必须在UI线程里被created
* execute(Params...) must be invoked on the UI thread. execute(Params...)也必须在UI线程里被调用
* Do not calcall onPreExecute(), onPostExecute(Result), doInBackground(Params...),  onProgressUpdate(Progress...) manually. 这几个方法不能手动调用。
* The task can be executed only once (an exception will be thrown if a second execution is attempted.)这个task只能被执行一次。再次执行的时候回thrown一个exception。


以上内容是 AsyncTask 官方文档的简单翻译，和自己的一些理解。