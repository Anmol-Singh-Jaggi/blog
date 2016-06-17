So, today I was trying to create a Windows USB installer.  

*'Now what could go wrong with this simple task'*, you might ask. But you, my friend, are underestimating me.

As soon as I inserted the pen drive, a [notification](http://imgur.com/kMKtz3m) popped up saying that all the drivers have been installed successfully.  
However, there was one *small* problem; it was not getting listed under *My Computer*.  

I searched online for this problem and found that this could be due to the pen drive either being unformatted or just not having any labels assigned to it.

So I opened [*Disk Management*](http://imgur.com/YZrlG8i) in order to format it.  

But since Windows *Disk Management* shows *ext4* partitions and unformatted partitions [without any labels](http://imgur.com/OEIPvze), I somehow deleted both the pen-drive as well as my Linux swap partitions (and got a direct nomination for the *Most absent-minded person ever* award).

I thought to myself: *"This shouldn't be that big of a problem. Swap space is anyway just required for paging and hibernation, which are not critical for the functioning of an OS; I'll just boot into Ubuntu and reformat the Swap partition correctly."*

But as soon as I rebooted the system, instead of the usual boring [GRUB menu](http://imgur.com/E2buC4m), I got a prompt with an error message saying [*'error: unknown filesystem'*](http://imgur.com/jhW0IRf).  

I googled the error message and [found a way](http://askubuntu.com/a/495993/173003) to somehow boot into Ubuntu.  

After logging in, I reformatted the swap partition following the instructions given [here](http://askubuntu.com/a/180735/173003), and rebooted the system once again.  
But this time the boot process took an unusually long time.  
I searched about this problem and [found](http://askubuntu.com/a/180735/173003) that one of the reasons of a slow boot could be that the system is unable to mount a partition due to invalid UUID in the `/etc/fstab` file.  

And it was indeed the problem in my case; apparently, after reformatting the swap partition, its UUID changes.   

So I updated the fstab file with the correct UUID and, lo and behold, the boot time was back to normal.
