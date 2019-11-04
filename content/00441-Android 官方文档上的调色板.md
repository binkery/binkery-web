# Android 官方文档上的调色板
- 2014-12-01 16:41:07
- Android
- android,

<!--markdown-->下面是 Android 官方文中 <http://developer.android.com/design/style/color.html> 列举的几个颜色，这些颜色被放在了开发者网站上，Google 应该不是随便就瞎给的，应该是挺好看的颜色的。原谅我实在没有艺术细胞，就是觉得挺好看的，但是不知道为啥好看，也不知道有多好看。Google 也提供了下载，但是很不幸，下载完的内容不会看，除了 value.txt 和 NOTICE.txt 能直接打开外，其他的不知道怎么打开。value.txt 提供的颜色比较少，而且很不幸是页面上方的那几个颜色，但这几个颜色你通过网页上鼠标停留就可以获取到了。


<!--more-->


后来我在stackoverflow 上找到了答案，也有人问同样的问题。<http://stackoverflow.com/questions/12761655/how-to-use-android-color-swatches> 。在答案里，已经有人详细介绍应该使用什么样的软件并且怎么打开对应的文件了。不过更好的是，有人把颜色的色值都给列出来了，大好人啊。

其实也有另外一招，我也经常用，stackoverflow 上也有人说了，就是找一个取色器的小软件就搞定了。不过既然有人已经整理出来了，那么直接拿来用吧。

先来十个颜色，就是官方文档上部分的十个颜色色值。

<span style="background:#33B5E5">#33B5E5</span>
<span style="background:#0099CC">#0099CC</span>

<span style="background:#AA66CC">#AA66CC</span>
<span style="background:#9933CC">#9933CC</span>

<span style="background:#99CC00">#99CC00</span>
<span style="background:#669900">#669900</span>

<span style="background:#FFBB33">#FFBB33</span>
<span style="background:#FF8800">#FF8800</span>

<span style="background:#FF4444">#FF4444</span>
<span style="background:#CC0000">#CC0000</span>







下面是每个颜色从 01 到 15 的渐变颜色
![http://www.binkery.com/usr/uploads/2014/12/1371500947.png][1]

    <?xml version="1.0" encoding="utf-8"?>
    <resources>
    
    <color name="blue01">#0099CC</color>
    <color name="blue02">#079DD0</color>
    <color name="blue03">#0FA1D3</color>
    <color name="blue04">#16A5D7</color>
    <color name="blue05">#1DA9DA</color>
    <color name="blue06">#24ADDE</color>
    <color name="blue07">#2CB1E1</color>
    <color name="blue08">#33B5E5</color>
    <color name="blue09">#50C0E9</color>
    <color name="blue10">#6DCAEC</color>
    <color name="blue11">#8AD5F0</color>
    <color name="blue12">#A8DFF4</color>
    <color name="blue13">#C5EAF8</color>
    <color name="blue14">#E2F4FB</color>
    
    <color name="purple01">#9933CC</color>
    <color name="purple02">#A041D0</color>
    <color name="purple03">#A750D3</color>
    <color name="purple04">#AC59D6</color>
    <color name="purple05">#B368D9</color>
    <color name="purple06">#BA75DC</color>
    <color name="purple07">#C182E0</color>
    <color name="purple08">#C58BE2</color>
    <color name="purple09">#CB97E5</color>
    <color name="purple10">#CF9FE7</color>
    <color name="purple11">#D6ADEB</color>
    <color name="purple12">#DDBCEE</color>
    <color name="purple13">#E5CAF2</color>
    <color name="purple14">#F5EAFA</color>
    
    <color name="green01">#669900</color>
    <color name="green02">#6DA000</color>
    <color name="green03">#75A800</color>
    <color name="green04">#7CAF00</color>
    <color name="green05">#83B600</color>
    <color name="green06">#8ABD00</color>
    <color name="green07">#92C500</color>
    <color name="green08">#99CC00</color>
    <color name="green09">#A8D324</color>
    <color name="green10">#B6DB49</color>
    <color name="green11">#C5E26D</color>
    <color name="green12">#D3E992</color>
    <color name="green13">#E2F0B6</color>
    <color name="green14">#F0F8DB</color>
    
    <color name="orange01">#FF8A00</color>
    <color name="orange02">#FF9105</color>
    <color name="orange03">#FF9909</color>
    <color name="orange04">#FFA00E</color>
    <color name="orange05">#FFA713</color>
    <color name="orange06">#FFAE18</color>
    <color name="orange07">#FFB61C</color>
    <color name="orange08">#FFBD21</color>
    <color name="orange09">#FFC641</color>
    <color name="orange10">#FFD060</color>
    <color name="orange11">#FFD980</color>
    <color name="orange12">#FFE3A0</color>
    <color name="orange13">#FFECC0</color>
    <color name="orange14">#FFF6DF</color>
    
    <color name="red01">#CC0000</color>
    <color name="red02">#D30A0A</color>
    <color name="red03">#DB1313</color>
    <color name="red04">#E21D1D</color>
    <color name="red05">#E92727</color>
    <color name="red06">#F03131</color>
    <color name="red07">#F83A3A</color>
    <color name="red08">#FF4444</color>
    <color name="red09">#FF5F5F</color>
    <color name="red10">#FF7979</color>
    <color name="red11">#FF9494</color>
    <color name="red12">#FFAFAF</color>
    <color name="red13">#FFCACA</color>
    <color name="red14">#FFE4E4</color>
    
    
    </resources>


  [1]: http://www.binkery.com/usr/uploads/2014/12/1371500947.png