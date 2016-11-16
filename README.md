angular.min.js so we dont have to put this in all the subdirectories
testprograms.ipynb has vlc demo program playing video. need a ui

use the command line 

/Applications/VLC.app/Contents/MacOS/VLC d4-101-at-spencer.asf to display the stream

/Applications/VLC.app/Contents/MacOS/VLC -vvv d4-101-at-spencer.asf --sout='#transcode{vcodec=h264,vb=800,scale=1}:std{access=file,mux=ts,dst=/Users/dc/Downloads/output.mp4}' to save the stream to output.mp4
play the mp4 in vlc. quicktime wont work


/Applications/VLC.app/Contents/MacOS/VLC d4-101-at-spencer.asf --sout='#transcode{vcodec=h264}:std{access=file,dst=/Users/dc/Downloads/output1.mp4}'
stores file output1.mp4. There is no display of the video. 
Use /Applications/VLC.app/Contents/MacOS/VLC /Users/dc/Downloads/output1.mp4


