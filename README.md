angular.min.js so we dont have to put this in all the subdirectories
testprograms.ipynb has vlc demo program playing video. need a ui

use the command line 

/Applications/VLC.app/Contents/MacOS/VLC d4-101-at-spencer.asf to display the stream

/Applications/VLC.app/Contents/MacOS/VLC -vvv  d4-N101-at-N1st.asx --sout='#transcode{vcodec=h264}:std{access=file,dst=/Users/dc/videodemos/traffictest.mp4}'
This creates the file and if VLC is working do a ls -al to see the file grow. Wont see the display. 
Kill this by stopping the VLC instance. The asf file doesnt seem to reliably work? 


/Applications/VLC.app/Contents/MacOS/VLC d4-101-at-spencer.asf --sout='#transcode{vcodec=h264}:std{access=file,dst=/Users/dc/Downloads/output1.mp4}'
stores file output1.mp4. There is no display of the video. 
Use /Applications/VLC.app/Contents/MacOS/VLC /Users/dc/Downloads/output1.mp4


testvideo.html extracts frames from video only works on firefox; mp4 codec not in chrome

TestVideoSource.html canvas/video HTML5 elements. Playback video from html5 source, add opencv in JS to frames

