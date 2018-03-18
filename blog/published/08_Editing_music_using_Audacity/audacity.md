This one is for all the people who like music (who doesn't btw?).

I will showcase on how to edit music using a free software called [Audacity](https://www.audacityteam.org/).  
Specifically, we will be editing 'mixtape' kind of music, in which there are multiple songs interwined into a single track.  
The background behind is this - a looonng time back, when the Earth's crust was still solidifying, I used to listen and record radio on Saturday nights, where some [very talented DJ's](https://www.submerge.in/artists/nikhil-chinapa/) would play [fantastic music](https://soundcloud.com/nikhilchinapa) in the form of mixtapes. The problem was that the DJ would keep on blabbering something in between and I used to like at max 40-50% of the songs in the whole thing. So, I decided to "cut out" those songs from the recording.

Although I have stopped listening to radio, I still download fresh music ~~illegally~~ from Youtube (shhhh! don't tell anyone pliez), and edit that according to my taste.

So, [here are the steps](https://youtu.be/6zXDo4dL7SU):


1. Download Audacity from [here](https://www.audacityteam.org/download/). You might want to download the [Lame mp3 encoder](http://manual.audacityteam.org/man/faq_installation_and_plug_ins.html#lame) if you want to export music as an mp3 file and the absolutely fantastic piece of software called [FFmpeg](http://manual.audacityteam.org/man/faq_installation_and_plug_ins.html#How_do_I_download_and_install_the_FFmpeg_Import.2FExport_Library.3F) if you want to edit a much larger variety of music file formats.
2. Get a mixtape from somewhere and rename it as `tomato_is_actually_a_fruit!!!1.mp3`.
3. Fire up Audacity and import the mixtape by navigating to `*File* -> *Import* -> *Audio*`.
4. Click on `*Save project as..*` because Audacity hangs **too much**.
5. Note down the segments of the track which you **dont** like in a text file, (you can do this in your favourite music player if Audacity seems inconvenient for this). Make these observations as accurate as possible.
6. For all the unwanted segments between timestamps `t1` - `t2`, do the following:
   - Delete the segment by applying *`Split Delete`* to it (`*Edit* -> *Remove special* -> *Split Delete*`).
   - Apply *`Fade Out`* to the segment `t1-00:00:15` (15 seconds pre `t1`) and *`Fade In`* to the segment `t2+00:00:15` (15 seconds post `t2`). This is so that it does not feel as if the individual songs are ending abruptly.
7. Finally at the end of the mixtape, if it ends abruptly, apply the *`Studio Fade Out`* effect (`*Effect* -> *Studio Fade Out*`) to the last 30 seconds or so.
8. At this point, all the unwanted music has been removed. We now need to combine the remaining part. For that, first add a new track; `*Tracks* -> *Add New* -> *Stereo Track*`.
9. **Keep saving the project frequently as Audacity hangs too much.**
10. Now, starting from the beginning, shift every existing segment to the left to align with its previous segment in alternating tracks such that the end of one track overlaps with the beginning of the next track on its right. (1st segment in 1st track, 2nd segment in 2nd track, 3rd segment in 1st track and so on...)
11. You are done! At this point, you will be pretty astonished at how easy it was, so just unplug your computer and take deep breaths.
12. Fffffuuuuuu.... forgot one thing! - To save everything, `*export*` everything [ as an mp3 (quality = 'Extreme') or as an .ogg (quality = 5) ]. If all your progress was lost due to the previous step, then go to Step 1 and skip step 11.
13. Share this post every where you can; Facebook, Twitter, Instagram, Youtube, Google+ (you should introspect if you are using this btw). Spam it to every one in your Gmail contacts. Whatsapp to every person you know, even if it risks your friendship with them. This step is the most crucial one. Without this, your music will sound more lifeless than my 1-million-year-old grandma.

I have screencasted the whole process and posted a live demo [here](https://youtu.be/FoIADR6Nhv0) for all the folks who don't know how to read.  
In this demo, [this](https://soundcloud.com/user-693671739/input-mixtape) is the  mixtape, and [this](https://soundcloud.com/user-693671739/output-mixtape) is the result post editing.

If you found anything incorrect or otherwise objectionable in this post, then ~~please keep it to yourself~~ feel free to give feedback. :)


.....  

.....  

.....  

.....  

.....  

.....  

.....  

.....  


If you came all this far, you have a lot of free time; please do some of my home work !!