# Git hooks 在我的网站的运用
- git,hooks
- 2018.07.12

通过 git hooks ，可以实现在代码或者文章内容修改提交后，触发服务端 python 代码重新生成 html 网页。

我的网站是一个 nginx + html 的纯静态网站。nginx 的配置很简单，html 纯静态网页是我通过 python 脚本生成的。

我在自己的服务器上搭建了一个 git 服务器，其实就是安装了 git。新建了一个 git 项目，这个项目主要有三个目录，一个 artilces 目录，一个 source 目录，一个 html 目录。

## articles 目录

articles 目录存放的是我写的文档，以 markdown 格式编写。

## source 目录

source 目录下，是一些 python 脚本，其实没有多少行代码，就是读取 article 目录下的文章，然后生成 html 页面。生成的 html 文件就存放在 html/ 目录下/

## html 目录

html 目录就是网站的实际目录了，nginx 的 conf 会指向这个目录，也就是我的网站的跟目录。当然这个目录的大部分以 .html 后缀的文件是在 .gitignore 列表中的。

## 没有 git hooks 之前

没有 git hooks 之前，我在本地修改好脚本，或者文章后，git push 到服务器上，然后 ssh 登录到我的服务器，进行 git pull，并且执行 python 脚本。这样我就可以看到的修改后的内容了。

这样比较麻烦，后来我用 crontab 写定时任务，每隔多长时间自动 git pull 一下，然后执行 python 脚本。但是总觉得这很浪费，因为我也是比较懒的，经常很长时间不会写东西的。设置多长时间都是问题。

## git hooks 解决

最理想的情况是在我有东西提交的时候，才会去执行这些操作了。于是 git hooks 可以解决我的需求。因为是自己搭建的 git 服务，很容易就搞定了，找到这个项目的 git 目录，有个 hooks 的子目录，找到 post-receive.sample ，把它重命名为 post-receive ，并且把你要的操作写到这个脚本里，那么在客户端发起 push 请求的时候，会自动触发这个脚本，执行你想要的操作。这样就实现了我的需求了。

以后修改网站或者文章的时候，只需要在本地操作了，不需要 ssh 登录到远程服务器了。就是这样～～
