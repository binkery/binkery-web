# ubuntu上的ffmpeg 和 mediainfo
- 2013-09-04 03:05:25
- 
- ubuntu,工具,ffmpeg,mediainfo,转码,

<p>ffmpeg的安装：</p>
<p>sudo apt-get install ffmpeg</p>
<p>检查支持的格式</p>
<p>ffmpeg -formats</p>
<p>转码：下面是把一个mov文件转成mp4文件，codec的信息都保留。</p>
<p>ffmpeg -i in.mov -acodec copy -vcodec copy out.mp4&nbsp;</p>
<p>这个速度很快，一会就ok了。</p>
<p>mediainfo</p>
<p>sudo apt-get install mediainfo</p>
<p>使用更简单了。</p>
<p>mediainfo videopath</p>
<p>打印输出这个文件的信息。很详细很全。</p>