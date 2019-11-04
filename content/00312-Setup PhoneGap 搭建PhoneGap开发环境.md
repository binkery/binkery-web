# Setup PhoneGap 搭建PhoneGap开发环境
- 2014-09-05 07:18:44
- 
- android,ubuntu,nodejs,phonegap,sdk,

<p>这是在公司一个项目里，做前期调研的时候，需要用到PhoneGap，我在自己的Ubuntu的机器上搭建的过程和遇到的一些问题，整理后有了下面这个文章。这是当成一个说明文档发给了其他同事，所以用英文写的。The following are the steps of the setup PhoneGap develope environment for android and some problems that I meet .</p>

<p>
1 . Install Node.js in your ubuntu 安装Node.js<br />
<span class="Apple-tab-span" style="white-space:pre">	</span>1 ) Download the Node.js package from nodejs.org 下载node.js，官网：nodejs.org<br />
<span class="Apple-tab-span" style="white-space:pre">	</span>2 ) Extract the .tar.gz file 解压<br />
<span class="Apple-tab-span" style="white-space:pre">	</span>3 ) Type the commands in the terminal 在命令行里输入<br />
</p><div class="code">
$ ./configure<br />
$ make<br />
$ make install
</div>
<p></p>
<p>2 . Install PhoneGap 安装PhoneGap<br /><span class="Apple-tab-span" style="white-space:pre">	</span>$sudo npm install -g phonegap</p>
<p>3 . create PhoneGap App 创建一个 PhoneGap 应用<br />
</p><div class="code">
$ phonegap create app-name<br />
$ cd app-name<br />
$ phonegap build android</div>
<p></p>

<p>4 . After build successful , your can import the android project to your eclipse . build 成功后，就可以把Android 项目导入到eclipse 里了。<br />
<span class="Apple-tab-span" style="white-space:pre">	</span>The project locate at app-name/platforms/android</p>


 <p>problems maybe encountered 可能会遇到的一些问题:</p>
<p>(1)  make failed . make 失败<br />
<span class="Apple-tab-span" style="white-space:pre">	</span>
error message like : "make[1]:g++: Command not found "<br />
<span class="Apple-tab-span" style="white-space:pre">	</span>
solution:没有安装g++，下面的命令行安装g++<br />
</p><div class="code">
$ sudo apt-get install g++
</div>
<p></p>
<p>(2) install PhoneGap failed PhoneGap 安装失败<br />
<span class="Apple-tab-span" style="white-space:pre">	</span>error message like :<br />
</p><div class="code">
npm ERR! cb() never called!<br />
npm ERR! not ok code 0<br />
</div>
<span class="Apple-tab-span" style="white-space:pre">	</span>solution 修改.npmrc 文件，增加一个仓库。<br />
<div class="code">
$ gedit ~/.npmrc<br />
</div>
<span class="Apple-tab-span" style="white-space:pre">		</span>
type below line and save file.<br />
<div class="code">
registry = http://registry.npmjs.vitecho.com
</div><p></p>
<p>(3) phonegap build android failed<br />
<span class="Apple-tab-span" style="white-space:pre">	</span>error message like   <br />
</p><div class="code">
detecting Android SDK environment...<br />
using the remote environment<br />
</div>
<span class="Apple-tab-span" style="white-space:pre">	</span>
It means that It do not find the android environment , but in fact you have android sdk in your ubuntu . 这个环境变量的问题，默认一般没有把 Android SDK 的目录加入到环境变量里，但是PhoneGap 会去环境变量里查找 Android SDK ，如果没有的话，会使用远程的环境，但是远程的环境经常会失败，而且会很卡，你懂的。解决很简单，把下面的路径添加到环境变量里就OK 了。<br /><span class="Apple-tab-span" style="white-space:pre">	</span>solution:<br />
<span class="Apple-tab-span" style="white-space:pre">		</span>Add both ~/android-sdk-linux/platform-tools/ and ~/android-sdk-linux/tools/ to your PATH<p></p>