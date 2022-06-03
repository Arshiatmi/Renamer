# Renamer

A Project To Rename All Files In A Folder ( In Some Specific Format ) For Example Rename All .mp4 Files.
# Example :

For Example In A Folder You Have These Files :

```
the_video_season01_part01.mp4
the_video_season01_part02.mp4
the_video_season01_part03.mp4
the_video_season01_part04.mp4
the_video_season01_part05.mp4
the_video_season01_part06.mp4
the_video_season01_part07.mp4
the_video_season01_part08.mp4
the_video_season01_part09.mp4
the_video_season01_part10.mp4
the_video_season01_part011.mp4
the_video_season01_part12.mp4
the_video_season01_part013.mp4
the_video_season01_part14.mp4
```
You Can Run This Program Like This :

`python3 Renamer.py --path /path/to/folder`

Then You Have To Enter : `mp4` And After That Just Enter The Name You Want To Rename.

For Example If You Enter `Video` Then Files Will Be :

```
Video1.mp4
Video2.mp4
Video3.mp4
Video4.mp4
Video5.mp4
Video6.mp4
Video7.mp4
Video8.mp4
Video9.mp4
Video10.mp4
Video11.mp4
Video12.mp4
Video13.mp4
Video14.mp4
```

*Important: This Program Will Rename With Creation Date. If A File Created Sooner, It Will Have A Smaller Number.*

You Can Do This Example With This Command Too :

`python3 Renamer.py --path "/path/to/folder" --mode 0 --delimiter "-" --name Video --format mp4`

Output Will Be :

```
Video-1.mp4
Video-2.mp4
Video-3.mp4
Video-4.mp4
Video-5.mp4
Video-6.mp4
Video-7.mp4
Video-8.mp4
Video-9.mp4
Video-10.mp4
Video-11.mp4
Video-12.mp4
Video-13.mp4
Video-14.mp4
```

**Available Modes:**
  - 0 : It Means Rename By Creation Time
  - 1 : It Means Rename By Last Modify Time
  - 2 : It Means Rename By Last Access Time

Now Nothing Will Be Asked And The Operation Is Done :)

( The of this project came from my friend : https://github.com/ProfessorMR )
