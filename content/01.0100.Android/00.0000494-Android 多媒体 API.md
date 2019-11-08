# Android 多媒体 API
- Android,多媒体

Android 对多媒体的支持算是比较坎坷，很多 API 都是在最近的几次更新才加上的。这就导致了很多 App 为了适配大部分机器，需要花很多精力。丰富的 API 会给开发者更多的选择，相信会越来越好吧～～

另外，要理解这些 API ，可能还是需要不少的音视频相关的一些知识的，什么编码，解码，文件格式啥的，反正我就有很多看不懂的，唉～～白在 Real 混了那么多年了，还是很多东西没学会。


# MediaFormat

多媒体格式的封装。

# MediaExtractor

MediaExtractor facilitates extraction of demuxed, typically encoded, media data from a data source.

从一个数据源中提取多路的编码数据。

数据源就是一个文件，比如音频文件或者视频文件。视频文件会包含音频数据和视频数据。

这个工具可以帮助你把一个文件里的各种音视频数据包一个一个的读取出来。

# MediaCodec

MediaCodec class can be used to access low-level media codec, i.e. encoder/decoder components.

多媒体的编解码工具类。注意它的功能是编解码，既有编码，又有解码。

如果是编码，输入的是原始的数据，输出的是编码后的数据。

如果是解码，输入的编码后的数据，输出的是解码后的数据。

有点废话～～

# AudioRecord 
The AudioRecord class manages the audio resources for Java applications to record audio from the audio input hardware of the platform.

就是录音。根据你指定的音频格式，录制得到的是指定格式的音频数据包。当你得到数据包后，可以选择播放，或者写入文件。

# AudioTrack
The AudioTrack class manages and plays a single audio resource for Java applications. 

和 AudioRecord 相反，它是用来播放的。你需要告诉它将要播放的音频格式，然后把数据包叫给它，它就会播放出来。

# FaceDetector
Identifies the faces of people in a Bitmap graphic object.
人脸识别。
这个类很简单，你给它一个 Bitmap 对象，它返回给你一个 Face 数组。Face 也很简单，里面封装了脸部的一些信息，比如两只眼的距离，以及一些我还没搞懂的数据。

# ExifInterface
This is a class for reading and writing Exif tags in a JPEG file.
喜欢拍照玩单反的人都知道 Exif ，其实就是一张照片，也就是 JPEG 文件的头信息。里面的数据很多，比如照片的宽度，高度，旋转角度，快门时间，曝光时间，拍摄时间，ISO，经度，纬度等等。

# MediaCrypto
MediaCrypto class can be used in conjunction with MediaCodec to decode encrypted media data. Crypto schemes are assigned 16 byte UUIDs, the method isCryptoSchemeSupported(UUID) can be used to query if a given scheme is supported on the device.

对多媒体数据的加密，通过一个 UUID 来对数据进行加密。

# MediaRecorder
Used to record audio and video.
用来录制视频或者音频。
这个类的功能会非常的强大，但是目前还在完善中。
可以指定一个音频输入，一个视频输入，然后合成一个视频。
比如，音频可以是麦克风，也可以是手机里的某个音乐文件。视频可以是前后某个摄像头，也可以是本地的一个视频文件，还可以是当前的屏幕。
这样就很好玩了，可以录制游戏视频，还可以制作假唱视频（音频使用本地的mp3，视频用摄像头，然后你冲着摄像头对口型，OMG，嗷嗷的～～）

# MediaRouter

MediaRouter allows applications to control the routing of media channels and streams from the current device to external speakers and destination devices.

# Image
A single complete image buffer to use with a media source such as a  MediaCodec.

# ImageReader
The ImageReader class allows direct application access to image data rendered into a Surface

# MediaMuxer
MediaMuxer facilitates muxing elementary streams. Currently only supports an mp4 file as the output and at most one audio and/or one video elementary stream. 

视频文件的合成。目前支持一路音频，一路视频，合成一个最终的视频文件，目前是mp4文件。

功能和 MediaRecorder 有点相似，但是 MediaRecorder 从 API 1 就有了，直到 API 19，视频源还只是摄像头。

MediaMuxer 使用起来会复杂一些，但是它支持的更多更好。

# MediaPlayer
这个就比较熟悉了，指定一个音频或者视频文件，它就可以播放了。如果是视频的话，可以给它一个 surface ，它会把视频画面画到 surface 上。
