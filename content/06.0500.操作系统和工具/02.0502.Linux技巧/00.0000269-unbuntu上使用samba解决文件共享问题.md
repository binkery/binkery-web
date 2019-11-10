# unbuntu上使用samba解决文件共享问题
- ubuntu,windows,共享,samba,局域网,
- 2013-08-28 12:34:37


<p>需要在ubuntu上和windows7上共享文件，在windows7上各种设置很麻烦，经过一番折腾也没有成功，很郁闷，最后使用这种方式解决问题。</p>
<p>SMB（Server Messages Block，信息服务块）是一种在局域网上共享文件和打印机的一种通信协议，它为局域网内的不同计算机之间提供文件及打印机等资源的共享服务。SMB协议是客户机/服务器型协议，客户机通过该协议可以访问服务器上的共享文件系统、打印机及其他资源。通过设置“NetBIOS over TCP/IP”使得Samba不但能与局域网络主机分享资源，还能与全世界的电脑分享资源。</p>
<p>1 安装<br> 
sudo apt-get install samba<br>
</p>
<p>
查看安装是否成功。<br>
sudo dpkg -l samba*<br>
</p>
<p>
binkery@binkery:~$ sudo dpkg -l samba*<br>
Desired=Unknown/Install/Remove/Purge/Hold<br>
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend<br>
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)<br>
||/ Name Version Description<br>
+++-================================================================================================================<br>
ii samba 2:3.6.3-2ubuntu2.6 SMB/CIFS file, print, and login server for Unix<br>
un samba-client <none> (no description available)<br>
ii samba-common 2:3.6.3-2ubuntu2.6 common files used by both the Samba server and client<br>
ii samba-common-bin 2:3.6.3-2ubuntu2.6 common files used by both the Samba server and client<br>
un samba-tools <none> (no description available)<br>
un samba4 <none> (no description available)<br>
un samba4-clients <none> (no description available)<br>
un samba4-common <none> (no description available)<br>
</p>

<p>
2.创建目录，修改权限<br>
//创建目录<br>
mkdir /home/binkery/share<br>
//修改权限<br>
chmod 777 /home/binkery/share<br>
</p>

<p>
3 . 修改配置<br>
//拷贝一份备份<br>
sudo cp /etc/samba/smb.conf /etc/samba/smb.conf_backup<br>
//编辑修改<br>
sudo gedit /etc/samba/smb.conf<br>
</p>

<p>
<p>
(1)找到 security = user 替换成<br>
security = binkery //这里也可以设置为share，这时访问就不需要用户名和密码了。那么就不需要映射用户和添加用户与密码<br>
username map = /etc/samba/smbusers //这个文件一会需要创建和编辑<br>
</p>

<p>
(2)添加到后面/etc/samba/smb.conf这个文件的最后<br>
//开始<br>
[Share]<br>
comment = Shared Folder with username and password<br>
path = /home/binkery/share<br>
public = yes<br>
writable = yes<br>
valid users = binkery<br>
create mask = 0700<br>
directory mask = 0700<br>
force user = nobody<br>
force group = nogroup<br>
available = yes<br>
browseable = yes<br>
//结束 共12行<br>
</p>

<p>
(3)修改编码，找到［global］把 workgroup = MSHOME 改成 :<br>
//开始<br>
workgroup = WORKGROUP<br>
display charset = UTF-8<br>
unix charset = UTF-8<br>
dos charset = cp936<br>
//结束 ,共4行<br>
经过上面三步的修改，保存。<br>
</p>
<p>
4.添加访问用户及密码<br>
添加用户<br>
sudo useradd binkery<br>
设置密码/修改密码也是这个命令<br>
sudo smbpasswd -a binkery<br>
创建修改文件/etc/samba/smbusers<br>
sudo gedit /etc/samba/smbusers<br>
在新建立的文件内加入下面这一行并保存<br>
new = “binkery”<br>
删除网络使用者<br>
sudo smbpasswd -x binkery<br>
</p>
<p>
5 测试和启动<br>
//测试<br>
sudo testparm<br>
//启动<br>
sudo nmbd restart<br>
</p>
<p>
6 . 在windows访问。<br>
这样，在win7命令行中输入\\linux ip，就可以访问你linux下的文件了。<br>
可以在windows上创建一个盘符映射，相当好用。这样我的Ubuntu的台式机和Windows笔记本拷贝文件就方便了很多很多。<br>
</p>
