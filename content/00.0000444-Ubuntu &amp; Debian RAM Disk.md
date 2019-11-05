# Ubuntu &amp; Debian RAM Disk
- 2016-03-22 02:24:35
- 
- 

<!--markdown--># Ubuntu & Debian RAM Disk

## What is RAM Disk

A RAM disk or RAM drive is a block of RAM (primary storage or volatile memory) that a computer's software is treating as if the memory were a disk drive(secondary storage)

## Why Use RAM disk

 - Speed 
    RAM > SSD > HDD
 - Capacity & Price
    HDD > SSD > RAM

But we have more RAM[4GB]

## How to make RAM disk
Use tmpfs

    $shell > sudo mkdir /media/ramdisk
    $shell > sudo mount -t tmpfs tmpfs /media/ramdisk

Mount on Start Up
Edit file /etc/fstab add to last line

    tmpfs /media/ramdisk tmpfs defaults,mode=1 777 0 0

And reboot system

 ## Squashfs!!
Compressed real-only file system for Linux. SquashFS compresses files , inodes and directories , and supports block sizes up to 1 MB for greater compression.
SquashFS is also free software(licensed under the GPL) for accessing SquashFS filesystems.SquashFS is intented for general real-only file system use and in comstrained block device/memory system ( e.g. embedded systems) where low overhead is needed.
The standrand version of SquashFS uses gzip compression , although there is also a project that brings LZMA compression to SquashFS.

## Make squashfs file
Install squashfs tools

    sudo apt-get install squashfs-tools

Create .sqsh file

    mksquashfs /usr/lib/jvm/java-6-sun-1.6.0.21 /home/binkery/jdk6.sqsh

Unsquash

    unsquashfs [option] target [file/directories to extract]

## Make Java run In RAM

### step 1. Create RAM disk
Use tmpfs

    $shell > sudo mkdir /media/ramdisk
    $shell > sudo mount -t tmpfs tmpfs /media/ramdisk

Mount on Start Up
Edit file /etc/fstab add to last line

    tmpfs /media/ramdisk tmpfs defaul,mode=1 777 0 0

### step 2. Create Java squashfs
Install squasfsh tools

    sudo apt-get install squashfs-tools

create .sqsh file

    mksquashfs /usr/lib/jvm/java-6-sun-1.6.0.21 /home/binkery/jdk6.sqsh

### step 3. Mount Java to RAM

    $shell > sudo mount /home/binkery/jdk6.sqsh /media/ramdisk -t squashfs -o loop

Make it permanant on startup
Edit /etc/fstab add line 

    /home/binkery/jdk6.sqsh /media/ramdisk squashfs ro,defaults,loop 0 0

### step 4. Set Java to default

    sudo update-alternatives --install "/usr/bin/java/" "/media/ramdisk/bin/java" 1

check install java complete

    sudo update-alternatives --config java

And choose java in ram.

Finish.






