# mac 上 ssh 配置解决反应慢的问题
- mac,ssh,ssh-config,
- 2018.05.26

在 mac 系统上，用 ssh 登录远程服务器的时候，总是会有些卡顿。

## 问题

在 mac 系统上，用 ssh 登录远程服务器的时候，总是会有些卡顿。在用 ubuntu 的时候，没有明显感觉卡顿，但是在 mac 上能明显感觉到。

## 解决方案

修改 ssh_config 。

在 mac 系统上，这个文件在 `／etc/ssh/ssh_config`，找到这个文件，然后找到 `GSSAPIAuthentication` 这行，把注释取消掉。

我实际的测试是不需要重启或者其它操作，直接 ssh ，就可以感觉到速度的变化。
