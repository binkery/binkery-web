# Connecting the Google Nexus 7 to Ubuntu / Mintover USB
- 2015-03-06 09:53:01
- 操作系统与开发环境
- ubuntu,nexus,mtp,

<!--markdown-->Nexus7连到我的电脑上的时候，没有显示盘符，家里的电脑是win7的，不过没有注意到有没有显示盘符。好像4.0 4.1的都这样，不能像U盘那么简单。搜了一下，很多都是在nexus7上安装ubuntu的，这个很好，有空研究一下。


<!--more-->


I have had the pleasure of using a Nexus 7 for the past few days, and while it is a fantastic tablet all around, there is one minor roadblock I hit, which was connecting it to my Ubuntu laptop to transfer files via USB. The problem stems from the fact that the Nexus 7 uses theMedia Transfer Protocol (MTP), support for which included by default (yet) on Ubuntu.

But as with all things Linux, mounting the tab and transferring files was accomplished with only a few simple commands. 

Here is what I had to do: 

1. Open a terminal. 

2. Create a udev rules file for the Nexus 7 with it’s device id (18d1)


    sudo nano /etc/udev/rules.d/99-android.rules 

3. Paste the following contents into the, save and exit (ctrl+o, then ctrl+x): 


    # Nexus 7
    SUBSYSTEM=="usb", SYSFS{idVendor}=="18d1", MODE="0666" 

 
4. Make the file executable (gotta love the security on Linux) 


    sudo chmod +x /etc/udev/rules.d/99-android.rules 

 
5. Install the mtp libraries from the repos 


    sudo apt-get install libmtp-common libmtp-runtime libmtp9 mtpfsmtp-tools

 
如果上面的不成功，试一下下面这一个。还不行的话，搜一下ubuntu上安装mtp。 

    sudo apt-get install mtpfs libfuse-dev libmad0-dev

 
6. Create a mount point for the Nexus 7 and make it accessable to all users 


    sudo mkdir /media/nexus7
    sudo chmod 755 /media/nexus7 

7. Finally plug your Nexus 7 into an empty USB slot on your comptuer and run the following command on the terminal: 


    sudo mtpfs -o allow_other /media/nexus7

8. In a few seconds, the tablet should appear mounted as an external drive on your file browser. 

9. Note that these steps are applicable to all Debian based systems including Linux Mint 

10. When you are done moving files, unmount the mounted folder before unplugging the device. 


    sudo umount /media/nexus7