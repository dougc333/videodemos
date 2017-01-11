python code showing how to select and extract images from video
1) write_video_as_images.ipynb showing how to write video

one confusing part is how to match codecs installed on your dev system to file extensions
this is different for each OS. 

another confusing part is the limitations of event capture in C++/UI which is specific to the platform you are working on. For example under MACOS 
to get destroyAllWindows() to work you have to use waitKey(1) after the destroyAllWindows call. Applicable and tested under Sierra MacOS. This is different for each platform

2) capture region in video playing. how to attach an event handler to the window under focus. This is different for each platform





