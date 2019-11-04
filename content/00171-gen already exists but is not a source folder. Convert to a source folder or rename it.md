# gen already exists but is not a source folder. Convert to a source folder or rename it
- 2015-03-06 10:09:46
- 操作系统与开发环境
- android,eclipse,error,gen,

<!--markdown-->最近android项目老是弹出这个错误，很烦人。有时候把gen目录删除了，让eclipse重新生成一个就好了。不过有时候好好的，这个目录突然不出现在配置的源目录里了，很郁闷，不知道是什么原因造成的。


<!--more-->


    [ERROR]gen already exists but is not a source folder. Convert to a source folder or rename it

This is a common error and you can solve it following these steps:

* Right click on the project and go to “Properties”
* Select “Java Build Path” on the left
* Open “Source” tab
* Click “Add Folder…”
* Check “gen” folder and click Ok and Ok again
* Again right click on the project and in the “Andriod Tools” click on “Fix Project Properties”