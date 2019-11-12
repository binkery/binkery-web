# Android 流量统计 TrafficStats
- Android,统计,工具,流量,trafficstats,

Android 提供了流量统计的工具类 android.net.TrafficStats , 这个统计包括字节数的发送和接收，网络包的发送和接收，所有的接口，包括移动数据接口，并且可以统计每个UID的传输。




这个统计不能保证在所有平台可用，如果不支持的话，在该类的所有的方法调用会返回UNSUPPORTED(值为-1).

这个类提供的都是静态方法。

//获取通过移动数据发送和接收的流量。Rx 是 接收，Tx 是发送，bytes 是字节数，packets 是数据包数量。统计从设备启动开始。

    static long getMobileRxBytes() 
    static long getMobileRxPackets() 
    static long getMobileTxBytes() 
    static long getMobileTxPackets()

//获取通过所有网络接口传输的流量。统计数据由网络层统计，所以包括 TCP 和 UDP 包。Rx 接收，Tx 发送，bytes 字节数，packets 数据包数量。也是从设备启动开始。

    static long getTotalRxPackets()
    static long getTotalRxBytes()
    static long getTotalTxBytes()
    static long getTotalTxPackets()

//根据UID 获取流量数据。每个应用有个 UID ，可以通过这个 UID 知道该应用一共产生了多少流量。

    static long getUidRxBytes(int uid)
    static long getUidRxPackets(int uid)
    static long getUidTxBytes(int uid)
    static long getUidTxPackets(int uid)

// 获取通过TCP 方式传输的流量数据。从 API Level 18 开始过期了。因为从 18 开始，传输层的统计不可用了。

    static long getUidTcpRxBytes(int uid)
    static long getUidTcpRxSegments(int uid)
    static long getUidTcpTxBytes(int uid)
    static long getUidTcpTxSegments(int uid)

// 获取通过 UDP 方式传输的流量数据，在API Level 18 开始过期了。

    static long getUidUdpRxBytes(int uid)
    static long getUidUdpRxPackets(int uid)
    static long getUidUdpTxBytes(int uid)
    static long getUidUdpTxPackets(int uid)

// 下面的方法是用来统计某个线程或者Socket产生的流量数据，可以通过DDMS 工具来分析网络的使用情况

    static void incrementOperationCount(int tag, int operationCount)
    static void incrementOperationCount(int operationCount)
    
    static void clearThreadStatsTag() 
    static int getThreadStatsTag()
    static void setThreadStatsTag(int tag)
    
    static void tagSocket(Socket socket)
    static void untagSocket(Socket socket)
