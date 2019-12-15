# Android 所有的网络信息 NetworkInfo
- Android,网络,


获取 Android 的网络信息，需要使用 ConnectivityManager 这个类。


Class that answers queries about the state of network connectivity. It also notifies applications when network connectivity changes. Get an instance of this class by calling **Context.getSystemService(Context.CONNECTIVITY_SERVICE)**.

The primary responsibilities of this class are to:
1. Monitor network connections (Wi-Fi, GPRS, UMTS, etc.)

2. Send broadcast intents when network connectivity changes

3. Attempt to "fail over" to another network when connectivity to a network is lost

4. Provide an API that allows applications to query the coarse-grained or fine-grained state of the available networks

    ConnectivityManager mManager = (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
    NetworkInfo[] infos = mManager.getAllNetworkInfo();

通过上面的代码，能获取到一个 NetworkInfo 的数组，除了咱们关心的 wifi 和 mobile 外，还有一些特殊的网络链接。


 - "MOBILE";//移动数据连接,不能与连接共存,如果wifi打开，则自动关闭
 - "WIFI";//wifi服务，当激活时，默认情况下，所有的数据流量将使用此连接。
 - "MOBILE_MMS";//运营商的多媒体消息服务
 - "MOBILE_SUPL";//平面定位特定移动数据连接
 - "MOBILE_DUN";//网络桥接，很老的一个网络
 - "MOBILE_HIPRI";//高优先级的移动数据连接。相同的为{TYPE_MOBILE}，但路由的设置是不同的。只有请求的进程将有机会获得移动的DNS服务器。
 - "WIMAX";//全球互通微波存取数据连接
 - "BLUETOOTH";//蓝牙
 - "DUMMY";//虚拟连接
 - "ETHERNET";//以太网 
 - "MOBILE_FOTA";
 - "MOBILE_IMS";
 - "MOBILE_CBS";
 - "WIFI_P2P";//通过wifi直连wifi