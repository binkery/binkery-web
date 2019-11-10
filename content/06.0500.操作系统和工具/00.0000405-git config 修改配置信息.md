# git config 修改配置信息
- git,版本管理,
- 2015-03-06 13:44:40

    git config

列出当前的配置信息。

    git config -l

修改配置信息

    git config key value

例如：

    git config user.name binkery

默认的，修改的是本地的，或者说是局部的，作用和下面的相同。

    git config --local user.name binkery

需要修改全局：

    git config --global user.name binkery

git 加载配置信息，先加载用户目录下的 .git 隐藏目录下的配置文件config，然后在加载 git 所在目录下的 .git 隐藏目录下的配置文件config，后加载的覆盖先加载的。

你也可以直接修改 config 文件，这是一个普通的文本文件。