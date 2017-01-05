Use the program VLC to create mp4 files from caltrans webcams

/Applications/VLC.app/Contents/MacOS/VLC -vvv  d4-N101-at-N1st.asx --sout='#transcode{vcodec=h264}:std{access=file,dst=/Users/dc/videodemos/traffictest.mp4}'

