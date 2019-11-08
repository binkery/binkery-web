# Ubuntu下Android开发eclipse启动慢
- android,ubuntu,eclipse
- 2015-03-06 07:12:26


最近老碰到这个问题，在 Ubuntu 系统下，打开 eclipse，总是很慢，显示 Android SDK content loader，然后那个进度条一直都一动不动的。一小会 eclipse 就变暗了。我没有一直等下去，不知道什么时候能好，都是关了 Force Close，然后重新打开，反复好几次才能成功。很郁闷，本来好好的心情想写点代码的，结果啥心情都没了。不过我在公司的就没问题。网上查了一下，有人说是Documentation for Android SDK 没有下载完成，才会导致 eclipse 在打开的时候加载不了，于是从网络获取，所以导致了打开速度很慢，和假死（也许是真死了）。

不管怎么说，首先任务是先下载sdk的文档，把东西都更新全了。
