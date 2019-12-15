# ubuntu 安装 chrome
- chrome,ubuntu,google,
- 2014-08-04 03:28:21


ubuntu 自带了firefox ， 但是我还是习惯使用chrome，<br /><br />
<div class="code">sudo apt-get install google-chrome-stable</div>
结果不能安装！！！<br /><br />只能下载安装了。<br /><br />
<div class="code">32位：<a target="_blank" href="https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb">https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb</a><br />
64位：<a target="_blank" href="https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb">https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb</a></div>
<p>下载完后，执行</p>
<div class="code">sudo dpkg -i google-chrome-xxxx.deb</div>
<p>提示错误。</p>
<div class="code">sudo apt-get -f install</div>
<p>安装依赖包，如果没有错误的话，安装成功了。（好像有点废话）<br /></p><p>在Applications -&gt; Internet 里能找到可爱的chrome</p><p><br /></p><p><br /></p><p><br /></p>