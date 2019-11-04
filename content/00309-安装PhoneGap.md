# 安装PhoneGap
- 2013-09-29 01:19:30
- 
- ubuntu,nodejs,phonegap,

<p>之前（<a href="http://www.binkery.com/post/306.html">http://www.binkery.com/post/306.html</a>）说了Node.Js的安装。安装Node.js后，type：</p>
<p>$sudo npm install -g phonegap</p>
<p>这个时候会下载很多文件，在经过一段时间后，出现了：</p>
<p>npm ERR! cb() never called!</p>
<p>npm ERR! not ok code 0</p>
<p>不知为什么，网上找了一下，有人说是因为大局域网捣乱，导致安装失败。有一招比较简单的方法：</p>
<p>编辑~/.npmrc 可能之前不存在这个文件，编辑保存就行。加入下面一行：</p>
<p>registry = http://registry.npmjs.vitecho.com </p>

<p>然后在试一下sudo npm install -g phonegap</p>
<p>这一次成功了，不明觉历啊。</p><p>总的来说，这次安装node.js 和 PhoneGap还是比较顺利的。很多原来还不是很明白，以后慢慢理解吧。</p><p>参考文章：</p><p><a>http://cnodejs.org/topic/4f9904f9407edba21468f31e</a></p>