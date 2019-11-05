# HTML5 viewport 的一点试验
- 2014-08-02 03:50:53
- 
- html5,viewport,

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">Viewport</span><span style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">是<span lang="EN-US">html5</span>里的东西，在很多网站上，为了在移动设备上有更好的用户体验，使用了<span lang="EN-US">viewport</span>这么一个东西。我把<span lang="EN-US">viewport</span>理解成一个缓冲，<span lang="EN-US">html</span>页面首先被绘制到这个缓冲上，然后再被投影到屏幕上。下面是对手头上几个不同的设备针对<span lang="EN-US">viewport</span>做了个简单的实验。记录下了不同<span lang="EN-US">viewport</span>设置下，获取到的屏幕宽度的区别。每一项两组数据，横屏时的数据和竖屏的。<span lang="EN-US"><o:p></o:p></span></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">viewport content=””<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">nexus 4 980*1324 980*509<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">ipad2 980*1185 980*644<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">HTC 603e 980*1408 980*453<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">Viewport content=”width=device-width”<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">Ipad2 768*928 768*504<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">603e 320*460 534*247<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">N4 384*519 598*311<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">Viewport content=”width=480”<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">N4 480*648 598*311<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">Ipad 768*928 1024*672<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">603e 480*690 534*247<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">Viewport content=”width=800”<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">603e 800*1150 800*370<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">Ipad 800*967 1024*672<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt">N4 800*1081 800*416<o:p></o:p></span></p>

<p class="MsoNormal"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;
mso-bidi-font-family:Arial;color:#333333;background:white;mso-font-kerning:
0pt"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal" style="margin-left:21.0pt;mso-para-margin-left:2.0gd"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;mso-bidi-font-family:
Arial;color:#333333;background:white;mso-font-kerning:0pt">Viewport </span><span style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;mso-bidi-font-family:
Arial;color:#333333;background:white;mso-font-kerning:0pt">默认值为<span lang="EN-US">980px</span>，不给<span lang="EN-US">width</span>设置值的话，默认使用<span lang="EN-US">980.<o:p></o:p></span></span></p>

<p class="MsoNormal" style="margin-left:21.0pt;mso-para-margin-left:2.0gd"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;mso-bidi-font-family:
Arial;color:#333333;background:white;mso-font-kerning:0pt">width=device-width </span><span style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;mso-bidi-font-family:
Arial;color:#333333;background:white;mso-font-kerning:0pt">为每个设备的默认值，在<span lang="EN-US">ipad</span>上，横屏和竖屏的宽度是一致的，所以在翻转的时候，加上<span lang="EN-US">ios</span>自带的旋转效果，整个页面看上去非常的顺畅，其他设备横竖屏时的宽度并不一致，所以<span lang="EN-US">UI</span>可能需要略微调整。<span lang="EN-US"><o:p></o:p></span></span></p>

<p class="MsoNormal" style="margin-left:21.0pt;mso-para-margin-left:2.0gd"><span style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;mso-bidi-font-family:
Arial;color:#333333;background:white;mso-font-kerning:0pt">当<span lang="EN-US">width</span>设定的值大于<span lang="EN-US">device-width</span>默认值，取设定的值，当设定的值小于<span lang="EN-US">device-width</span>默认值，取<span lang="EN-US">device-width</span>默认值。<span lang="EN-US"><o:p></o:p></span></span></p>

<p class="MsoNormal" style="margin-left:21.0pt;mso-para-margin-left:2.0gd"><span lang="EN-US" style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;mso-bidi-font-family:
Arial;color:#333333;background:white;mso-font-kerning:0pt"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal" style="margin-left:21.0pt;mso-para-margin-left:2.0gd"><span style="font-size:12.0pt;font-family:&quot;微软雅黑&quot;,&quot;sans-serif&quot;;mso-bidi-font-family:
Arial;color:#333333;background:white;mso-font-kerning:0pt">分析多个网站，大多数网站都使用<span lang="EN-US">width=device-width</span>来适配。但是有部分网站对<span lang="EN-US">ipad</span>没有使用<span lang="EN-US">viewport</span>技术，可以认为他们把<span lang="EN-US">ipad</span>归到<span lang="EN-US">PC</span>的范围了。</span></p>