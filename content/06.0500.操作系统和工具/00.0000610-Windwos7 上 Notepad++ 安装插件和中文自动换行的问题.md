# Windwos7 上 Notepad++ 安装插件和中文自动换行的问题
- 2018-09-01 04:49:21
- 开源项目
- windows7,notepad++,
- Notepad++安装插件,Notepad++中文自动换行
- Notepad++ 是一款优秀的文本编辑器，良好的可扩展性，意味着它有大量优秀的插件。不过，默认的情况下，Notepad++ 的中文展示并没有那么友好。

Windows10 + 机械硬盘简直不能忍受，于是换成 Windows 7 + 固态硬盘，顿时爽快了。

Windows 上的文本编辑器，我一直都是习惯用 Notepad++ ，习惯就好，就是中文换行总是很别扭。

首先，需要下载插件，一个叫 NppExec 插件。访问 <https://sourceforge.net/projects/npp-plugins/files/> 这个目录，可以看到 NppExec 这个插件，看起来是非常热门的插件，下载量不少。然后确定一下你的 Notepad++ 的版本，32 位还是 64 位。我的是 32 位，下载完后，解压，把解压后的文件放在 Notepad++ 安装目录下一个 plugins 子目录下。然后重启一下 Notepad++ 就可以了。

重启后，在 插件 菜单里，就多了一个 NppExec 的插件。点击 Plugins->NppExec->Execute... 

    sci_sendmsg SCI_SETWRAPMODE SC_WRAP_CHAR
    npp_console 0

这是一个脚本，写完了，保存，给这个脚本起一个名字。

然后再 Plugins->NppExec->Advanced Options... ，在右边的高级选项（Advanced options）里，有一个 Execute this script when Notepad++ starts，在下拉选择框里，选择你刚才写的那个脚本。 OK 就好了。
