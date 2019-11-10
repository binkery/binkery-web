# Ubuntu apt-get update Could not get lock/var/lib/apt/lists 错误
- ubuntu,apt-get,update,
- 2014-08-01 13:20:11


刚才用apt-get update 的时候报了这么一个错误。<br /><br />binkery@binkery:/var/lib/apt/lists$ sudo apt-get update<br />E: Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)<br />E: Unable to lock directory /var/lib/apt/lists/<br /><br />解决办法：<br />1 。 ps -e | grep apt<br />找出现在正在是不是有apt进程在运行。有的话就kill掉。没有的话，那有可能就不是这个问题了。<br /><br />sudo killall apt-get<br /><br />2 . 删除 /var/lib/apt/lists/lock 这个目录。<br /><br />sudo rm /var/lib/apt/lists/lock<br />或者 <br />sudo mv /var/lib/apt/lists/lock /其他目录<br /><br />然后<br /><br />sudo apt-get update<br /><br />这个时候就OK 了。<br /><br />收工。