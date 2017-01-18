# stop video on left mouse click and wait for right mouse click
# draw green window over selected area copy image to another window. 
# write selected image to file

import cv2
import numpy

rectBox = []
vc = cv2.VideoCapture('/Users/dc/videodemos/video_mouse.mov')

def mouse_capture(event, x, y, flags, param):
    global rectBox
    if event==cv2.EVENT_LBUTTONDOWN:
        print 'left down (x,y):',x,y
        rectBox = [(x,y)] 
        #print rectBox, len(rectBox)
        #cv2.waitKey(1000) #delay to allow selection of image
    elif event==cv2.EVENT_LBUTTONUP:
        rectBox.append((x,y))
        print 'left up (x,y):', x,y, "len:", len(rectBox)
        green_color = (0,255,0)
        cv2.rectangle(frame,rectBox[0], rectBox[1], green_color,2)
        cv2.imshow("video", frame)
        cv2.waitKey(1000)
        
ret_code, frame = vc.read()

cv2.namedWindow('video')
cv2.setMouseCallback('video', mouse_capture)

numFrame = 0;
while True:
    if len(rectBox)==2:
        print "len 2"
    if len(rectBox)==1:
        print 'draw point'
        cv2.circle(frame,(rectBox[0][0], rectBox[0][1]) , 1, (0,255,0))
        cv2.waitKey(10000)

    cv2.imshow('video', frame)
    numFrame+=1
    waitKey = cv2.waitKey(1) & 0xFF
    if waitKey == ord('q'):
        break
    ret_code,frame = vc.read()
    print numFrame, len(rectBox)


cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)

print 'done'
