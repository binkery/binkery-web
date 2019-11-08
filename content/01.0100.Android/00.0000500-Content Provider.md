# Content Provider
- Android,ContentProvider

Content provider 是 Android 四大基本组件之一。官方给出的介绍如下：

> Content providers manage access to a structured set of data. They encapsulate the data, and provide mechanisms for defining data security. Content providers are the standard interface that connects data in one process with code running in another process.

重点信息有这么几个：

1. 提供数据的访问
2. 封装数据，以及数据安全
3. 在进程之间共享数据

## 访问

大多数情况下，咱们只需要会使用 Android 系统设计好的 Provider 就可以了。也就是从系统的 Provider 里访问数据。

**ContentResolver** 是使用 Provider 的关键。Context.getContentResolver()  可以获得一个 ContentResolver 对象。也就是说，这个方法不是 Activity 独有的，是 Context 的子类都有这个方法。


    mCursor = getContentResolver().query(
    UserDictionary.Words.CONTENT_URI,   // The content URI of the words table
    mProjection,                        // The columns to return for each row
    mSelectionClause                    // Selection criteria
    mSelectionArgs,                     // Selection criteria
    mSortOrder);                        // The sort order for the returned rows

query() 方法需要几个参数：URI，一个列名的字符串数组，一个 where 语句，一个 where 语句的参数字符串数组，一个order语句

返回就是一个 Cursor 对象。Cursor 的使用很简单，这里不做介绍。

系统已经提供了很多个 Rrovider ，每个都有自己的 URI，比如 照片，视频，音频，通讯录，通话记录，日程表，等等。具体 URI 的知识参考跟 URI 相关的文章。

### 安全问题

Provider 为不同进程的程序提供了访问同一个数据源的方法，这样就有安全问题，所以，一些 Provider 的访问需要权限的申请的。

## 修改，增加，删除

Provider 为不同进程的程序提供了访问同一个数据源的方法，一般可以理解为不同的 APP 访问同一个数据库。有的 APP 访问数据库只为了显示，比如我只打算显示通讯录列表，但是另外一个 APP 显示完列表还希望用户能直接修改这里的内容。Provider 也提供了这样的访问方式。

基本和 SQLiteOpenHelper 的使用方式一致。

## 创建 Provider

除了 Android 设计好的几个 Provider 外，你还可以自己创建 Provider。你创建好的 Provider 可以为你的其他程序（APP0）提供数据，也可以为你的合作伙伴提供数据。当然这个用得比较少，所以咱们这里也不多说。大概知道下面几个点就可以。

1. 可以创建 Provider
2. Provider 其实也是对 SQLite 的一种封装。
3. 自己设计的 Provider 的时候可以为 Provider 设计访问权限。
4. Provider 也可以完全私有的，跟一个普通的数据库没有区别。