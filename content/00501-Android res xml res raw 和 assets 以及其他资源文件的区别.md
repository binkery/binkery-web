# Android res/xml res/raw 和 assets 以及其他资源文件的区别
- 2016-03-22 03:37:33
- 
- 

<!--markdown--># Android res/xml res/raw 和 assets 以及其他资源文件的区别

Android 为了加速对资源文件的读取，在编译的时候已经对资源文件里的 xml 文件和 9.png 文件进行了处理，变成了你不需要关心的二进制数据，存放在了一个你不需要关心的位置。你只需要通过这个资源的 ID 就可以获取到你要的文件。


<!--more-->

为什么说加速了呢，因为 xml 的解析是需要一定的运算量的，对 xml 解析的分析，大家可以看看其他的文档，xml 解析有很多种，有占内存多速度快的，有占内存少但速度慢的，不管采用哪种方式，google 都认为在程序运行的时候去解析 xml 是很浪费的，于是他们设计成了在编译的时候解析 xml，然后输出一个二进制数据，在运行的时候，直接通过 id 去读取二进制数据，这样就提高了效率了。

除了 xml 外，9.png 也是一样的道理。

所以，我们放在 layout ，drawable ，values 目录下的 xml 文件都被优化了。

## res/xml

这个目录下的 xml 文件同样会被优化成为二进制数据，但是你在运行时可以获取到一个 XmlResoureceParser 的对象，像普通 xml 文件一样解析它。

    XmlResourceParser xml = getResources().getXml(R.xml.data);   

## res/raw

这个目录下的 xml 不会被编译成二进制形式，会原样的保留 xml 文件的格式。

    InputStream is = getResources().openRawResource(R.raw.rawtext);

这里获取到的是一个 InputStream ，也就是说，这里你放啥都行，不一定非得是 xml ，任何的文件都可以。

## assets

res/xml 和 res/raw 都会为资源文件生成一个 id，而 assets 目录下的文件就不会生成 id，而是通过文件名的方式来访问的。跟 res/raw 有啥区别呢？assets 是可以有目录结构的，而 res/raw 是没有目录的。

    AssetManager assets = getAssets();
    InputStream is = assets.open("xxx/xxx.xxx");


以上就是几个资源文件目录的区别。
