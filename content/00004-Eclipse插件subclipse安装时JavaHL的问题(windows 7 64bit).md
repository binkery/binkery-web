# Eclipse 插件 subclipse 安装时 JavaHL 的问题(windows 7 64bit)
- 2015-03-06 03:27:55
- 操作系统与开发环境
- Java,subclipse,Eclipse,64位,JavaHL,JavaHL找不到库

在 windows7 中 Java 和 eclipse 都可以是64位的。如果需要配置 subclipse，中间可能会碰见 JavaHL 找不到库的问题。下面是一次成功的配置过程。

 - 安装64位的 jdk ,安装文件为 jdk-6u21-windows-x64.exe，安装完成之后设置 JAVA_HOME 环境变量，并把 %JAVA_HOME%\bin 加入到 path 中，确保可以正常的运行 java 和 javac 两个命令。

 - 安装 Eclipse，它只需要解压缩就可以。安装文件为 eclipse-jee-helios-win32-x86_64.zip

 - 在 eclipse 里面安装新插件 subclipse, 其更新的地址为 http://subclipse.tigris.org/update_1.6.x ，更新完之后在eclipse里面创建项目的时候，有 SVN 的选项。但是现在还不能使用,这是因为没有64位的javaHL的库，具体原因请查看http://subclipse.tigris.org/wiki/JavaHL

 - 安装JavaHL,可以直接在 http://www.sliksvn.com/en/download 上下载安装文件，其安装文件为 Slik-Subversion-1.6.12-x64.msi，它中间包含了 JavaHL 的包，在安装的时候需要安装JavaHL支持。安装完成之后在其安装目录的bin下面有很多以 SlikSvn 开头的 dll 文件。

 - JavaHL的配置。subclipse 使用的 dll 文件名不是以 SlikSvn 开头，你可以复制所有的 SlikSvn 开头的 dll 文件(在 Slik SVN 安装目录下面的 bin 目录下)，然后重命名拷贝的文件，新文件名为原始文件名去掉 "SlikSvn-" 的前缀。在 eclipse 启动的时候，需要让 eclipse 找到这些 dll ,所以在 eclipse 的配置文件 eclipse.ini 中还需要添加启动参数 java.library.path,指向拷贝的 dll 的路径。这个参数直接加在 -vmargs 的下一行，下面是示例：

    -Djava.library.path=C:/Program Files/SlikSvn/bin

然后你重启 eclipse，现在就可以使用 subclipse 了。
