I recently upgraded to [Ubuntu 16 LTS](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes) from [Ubuntu 14 LTS](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes).  
Unlike my previous experiences, this time the process was not that smooth.  
When the *'upgrade'* option resulted in more than half of my manually installed software being removed, I thought it's rather better to do a fresh install instead.

While the new system looked pretty sharp with most of the things working well, there was one major problem: the suspend feature wasn't working, [thanks to a bug in the kernel related to AMD graphics](http://askubuntu.com/questions/761820/suspend-not-working-on-ubuntu-16-04-for-dell-3537).  
How I solved it is a story for another day.  

After exploring the new features for a while (which didn't take much time), I started setting up the system, installing a lot of software and copying some configuration files from the previous install.  

After playing for a while, I decided to backup my files on Google Drive using a [small application](https://github.com/Anmol-Singh-Jaggi/gDrive-auto-sync) I created a while back.  
Here I hit another road block; [notify-send](http://ss64.com/bash/notify-send.html) (the app used to create those [bubble notifications](http://i.stack.imgur.com/HGjE9.png) during the backup process) was simply refusing to run when run from cron.  
I remember it happening in Ubuntu 14 too; the reason was that the environment in which cron operates is [very minimalist](http://askubuntu.com/a/23438/173003), and *notify-send* required the presence of a certain environment variable [`DISPLAY=0:0`](http://askubuntu.com/a/472769/173003) to work.  
So, I easily fixed this problem by [adding the definition of that variable inside the cron script](https://github.com/Anmol-Singh-Jaggi/gDrive-auto-sync/blob/674c7ee67c686d5d148253e179d3cc20efef6872/gDrive-auto-sync/crontab.txt#L27).  

But this trick wasn't working anymore in Ubuntu 16 !  

After googling **a lot** and trying many different hacks, I finally [found the solution](http://unix.stackexchange.com/a/10126/42552):  

Turns out, apart from the variable `DISPLAY`, we need 2 more environment variables for *notify-send* to work:  
 - `DBUS_SESSION_BUS_ADDRESS=unix:abstract=/tmp/dbus-KqjYaobROx`  
 - `XAUTHORITY=/home/anmol/.Xauthority`  

But there's another catch; the value of `DBUS_SESSION_BUS_ADDRESS` refers to a location in the `/tmp` directory, which means that this value is temporary and is valid only for a single login session.  
So if I simply added this variable to the cron script, it wouldn't have worked after the next login.  

The only way to make it work was to get the value of this variable every time a new session starts.  

So, I wrote a small [shell script](https://github.com/Anmol-Singh-Jaggi/snippets/blob/6d8bcd444f445d1937ead29ba6c673d9d19dff66/snippets/create_notify_send_env.sh) to read these variables' values and output them to [another file](https://gist.github.com/Anmol-Singh-Jaggi/89953401a090b071c038ad132756a2aa) which was then [sourced in the backup script](https://github.com/Anmol-Singh-Jaggi/gDrive-auto-sync/blob/9a6e9435eb462ae6cf55c661e06ee80c83a57215/gDrive-auto-sync/run.sh#L5), thus making them accessible during the *notify-send* invocation.  
To make this shell script run on login automatically, I used Ubuntu's built-in [Startup Applications](https://help.ubuntu.com/16.04/ubuntu-help/startup-applications.html) to schedule it.  


***TIP:*** To simulate the environment under which cron operates and test whether a script runs as expected from cron, follow [these steps](http://stackoverflow.com/a/2546509/1925388).
