# Android 基础之 Intent Activity Actions
- 2016-03-22 07:14:58
- Android
- android,intent,action,

<!--markdown--># Standard Activity Actions

这是目前定义在 android.content.Intent 里的标准的 Activity Action 。一般在启动 Activity 的时候会使用。

##  ACTION\_MAIN 
* android.intent.action.MAIN 
* 以一个主入口启动，不期望接收到数据。
* 输入：nothing
* 输出：nothing

## ACTION\_VIEW
* android.intent.action.VIEW 
* 显示数据给用户。
* 输入：通过 getData() 可以获取到数据的 URI
* 输出：nothing

## ACTION\_ATTACH\_DATA
* android.intent.action.ATTACH_DATA 
* 用来表明一些数据被附加到某些位置。
* 输入：通过 getData() 可以获取到被添加的数据的 URI
* 输出：nothing

## ACTION_EDIT
* android.intent.action.EDIT 
* 为给定的数据提供可编辑的访问方式
* 输入：通过 getData() 获取需要编辑的数据的 URI
* 输出：nothing

## ACTION\_PICK
* android.intent.action.PICK 
* 从数据里选择一个项目，并且返回被选择的项
* 输入：通过 getData() 获取数据的目录的 URI （vnd.android.cursor.dir/*）
* 输出：被选中项的 URI

## ACTION\_CHOOSER
* android.intent.action.CHOOSER

## ACTION\_GET\_CONTENT 
* android.intent.action.GET_CONTENT 
* Allow the user to select a particular kind of data and return it. This is different than ACTION\_PICK in that here we just say what kind of data is desired, not a URI of existing data from which the user can pick. An ACTION\_GET\_CONTENT could allow the user to create the data as it runs (for example taking a picture or recording a sound), let them browse over the web and download the desired data, etc.

## ACTION_DIAL
* android.intent.action.DIAL Dial 
* 拨打指定的号码。在 UI 上会显示将要拨打的号码，允许用户确定呼叫。
* 输入: 如果没有输入，则启动空白的拨号器界面。否则，通过 getData() 可以获取到电话号码的 URI ， 或者 tel:URI 。
* 输出: nothing.

 - **ACTION_CALL** 
android.intent.action.CALL  
对某人执行一次呼叫。直接呼叫是有约束的，所以大部分应用使用ACTION_DIAL，并且不允许呼叫紧急电话（比如999，911之类的），但是ACTION_DIAL可以。
    Input: 如果没有，则空白拨号器启动。否则，getData() 提供电话号码的 URI 或者 tel: URL
    Output: nothing.

 - **ACTION_SEND** 
    android.intent.action.SEND 

 - **ACTION_SENDTO** 
    android.intent.action.SENDTO

 - **ACTION_ANSWER** 
    android.intent.action.ANSWER 
    处理一个呼入的电话
    输入：nothing
    输出：nothing

 - **ACTION_INSERT** 
    android.intent.action.INSERT 
    出入一个空的项到指定的容器。
    Input: getData() 获取放置数据的目录的URI(vnd.android.cursor.dir/*)
    Output:被创建的新的数据项的 URI

 - **ACTION_DELETE** 
    android.intent.action.DELETE 
    从容器里删除指定的数据项。
    Input: getData() 提供将要被删除的数据项的 URI
    Output: nothing.

 - **ACTION_RUN** 
    android.intent.action.RUN 
    不管什么意思，运行数据。应该是把给定的数据当成可执行的代码运行。
    Input: ? 目前只针对测试工具
    Output: nothing.

 - **ACTION_SYNC** 
    android.intent.action.SYNC 
    执行一个同步操作
    输入：?
    输出：?

 - **ACTION_PICK_ACTIVITY** 
    android.intent.action.PICK_ACTIVITY Pick an activity given an intent, returning the class selected.
    Input: get*Extra field EXTRA_INTENT is an Intent used with queryIntentActivities(Intent, int) to determine the set of activities from which to pick.
    Output: Class name of the activity that was selected.

 - **ACTION_SEARCH** 
    android.intent.action.SEARCH 
    执行一次搜索 search
    Input: getStringExtra(SearchManager.QUERY) 提供被搜索词。 If empty, simply enter your search results Activity with the search UI activated.
    Output: nothing.

 - **ACTION_WEB_SEARCH** 
    android.intent.action.WEB_SEARCH 
    执行一次网页搜索
    Input: getStringExtra(SearchManager.QUERY) 提供被搜索词。如果是一个http 或 https 的 URL ， 改网页将被打开。如果是一个搜索词为空，Google search 被打开。
    Output: nothing.

 - **ACTION_FACTORY_TEST** 
    android.intent.action.FACTORY_TEST  
    工厂测试的主入口。只有在设备以工厂测试模式启动的方式下使用。要求实现的包被安装在系统的镜像（system image）里。
    输入: nothing
    输出: nothing