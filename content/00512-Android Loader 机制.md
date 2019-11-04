# Android Loader 机制
- 2016-03-22 07:16:52
- 
- 

<!--markdown--># Android Loader 机制

Android 在 3.0 后引入了 Loader 机制，并且 v4 包提供了 support 。所以，看上去实用性还是很强的。

## 使用

使用其实还是比较简单，有以下几点：

1. 获取 LoaderManager . 在 Activity 和 Fragment 下，可以直接通过 get 的方式获取，也可以获取 support 的 LoaderManager。
2. 调用 initLoader(int id, Bundle args,LoaderCallbacks callback）方法。这个时候需要实现一个 callback。
3. 实现 callback 的 onCreateLoader(int id,Bundle args),这里，需要返回一个 Loader 实例。
4. 你可能需要写一个 Loader 的子类，主要得重写 loadInBackground() 方法。

这样，大体上，你的 demo 就能跑了。特别是如果你是照着网上很多例子写的，而那些例子也基本上都是照着 google 的官网写的，他们都用的是 CursorLoader 这个特殊的 Loader 。而我在打算自己写一个 Loader 的时候碰见了一些问题，因为我不能一用 Loader 就只能用 Cursor 吧？

想要用 Loader，就去看看 Loader 怎么用，在文档里看到这么一句话：Most implementions should not derive directly from this class , but instead inherit from SyncTaskLoader . 好吧，去看看 SyncTaskLoader 吧，结果官方给了一个很长很长的 demo，以及很短很短的说明。

于是我抛开文档，自己写试试吧，自定义了一个类，继承于 SyncTaskLoader，提示重写构造方法，提示重写 loadInBackground() 方法。都写好了，在 onCreateLoader() 方法 return 了一个自定义的 Loader 的实例。在 Activity onCreate 的时候调用了 initLoader() 方法，跑一下吧。结果毛都没有。加断点调试的时候，发现 loadInBackground() 方法根本没有调用，WTF。

最后查找了一下，在 stackoverflow 上，有个哥们说，你试试重写 onStartLoading() 方法，然后调用 forceLoad() 方法。试完了果然管用。一个很意外的坑啊。

## 感受

这里的感受，是对这个 API 设计的一些想法，不知道为啥这样设计。

* 首先，不能拿来直接用。SyncTaskLoader 还不是那种拿来直接能用的，对于开发者，特别是需要快速开发的，这样的设计很让人难以接受。
* 然后，学习成本高。一个 API 的设计的最终目标是好用，没有学习成本，如果还需要话很多时间去研究这个异步机制，怎么样才能避免犯错，怎么样才能用对，这个学习成本太高了。

## 思考

SyncTaskLoader 其实是封装了一个 SyncTask 在里面的，而 SyncTask 是被很多开发者抛弃的，除了跟这个 Loader 一样难用以外，还包括对线程控制不理想。


