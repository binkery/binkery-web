# ubuntu 安装 ant
- ubuntu,ant,apache,
- 2014-08-01 13:20:03


最简单的办法是<div>&nbsp; &nbsp; &nbsp;sudo apt-get install ant</div><div>这个办法可能比较慢，因为需要下载安装一些其他的依赖库，可能需要一些时间，网速也比较有点慢，所以找了其他的办法。</div><div><br /></div><div>Apache ant 的官网</div><div><br /></div><div><a href="http://ant.apache.org/bindownload.cgi">http://ant.apache.org/bindownload.cgi</a></div><div><br /></div><div>目前最新的是1.9.x ， 不过还是习惯找稍微旧一点点的 ， 在Old Ant Releases 里可以找到很多很多。</div><div>下载了一个.tar.gz文件，才几M，跟刚才比轻量了很多很多。</div><div>解压，tar -xf apache-ant-xxxx.tar.gz</div><div>移动到opt目录下 sudo mv apache-ant-xxx /opt/</div><div>配置环境变量</div><div><br /></div><div>sudo gedit /etc/profile</div><div><br /></div><div>添加</div><div>export ANT_HOME="/opt/apache-ant-xxx"</div><div>export PATH="$PATH:/opt/apache-ant-xxx/bin"</div><div><br /></div><div>保存后, source /etc/profile</div><div><br /></div><div>验证</div><div>ant -version</div><div>如果有版本信息，类似：</div><div>Apache Ant(TM) version 1.8.4 compiled on May 22 2012</div><div><br /></div><div>OK ， 搞定，收工。</div>