# RTP 信息头中 sequence 和 timestamp 在Android 4.4 中强制检测
- 2015-03-06 13:58:18
- 计算机网络
- android,播放器,rtsp,rtp,

<!--markdown-->在Android 4.4 的 MediaPlayer 上，会对 RTP 数据包的 sequence 和 timestamp 进行检查，如果任一信息缺失，都可能引起 MediaPlayer 崩溃。


<!--more-->


    F/MyHandler(30851): ./frameworks/av/media/libstagefright/rtsp/MyHandler.h:1428 CHECK(GetAttribute((*it).c_str(), "seq", &val)) failed.
    
    F/MyHandler(31253): ./frameworks/av/media/libstagefright/rtsp/MyHandler.h:1437 CHECK(GetAttribute((*it).c_str(), "rtptime", &val)) failed.​

所以在收到客户端发送的 PLAY 请求的时候，不管是 resume 还是 seek ，都需要在 RTP 包的 HEADER 里面加上 sequence 和 timestamp 信息。

在 Android 4.4 （可能是4.3）之前，如果是非 seek 的 PAUSE PLAY 请求，也就是 PLAY 请求没有带 range 信息，这种情况下，RTP 包可以不带 sequence 和 timestamp 信息，我们可以这样理解，默认认为数据包到达的顺序是正确的，并且中间不出现丢包的情况，所以 sequence 和 timestamp 可以认为是冗余的数据，不是必须的。但是在 4.4 （也可能是4.3开始），MediaPlayer 会检查每个包的 HEADER 信息里有没有包含这些信息。