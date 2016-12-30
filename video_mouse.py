import cv2
# this runs as a python program but is slow


refPt = []
value = 0

def foo(event):
    print "trackbar callback", event

def click(event,x,y,flags,param):
    global refPt, cropping
    #print "event:",event
    #print "flags:", flags
    #print "param:", param
    if event == cv2.EVENT_LBUTTONDOWN:
        print 'leftbuttondown x,y:', x,y
        refPt=[(x,y)]
    elif event == cv2.EVENT_LBUTTONUP:
        print 'leftbuttonup'
        refPt.append((x,y))
        green = (0,255,0)
        cv2.rectangle(image,refPt[0], refPt[1], green,2)
        #this rectangle is only for 1 frame. copy this to another window
        #imshow to show the green rectangle
        cv2.imshow("image",image)
        #this is the frame at time of mouse click, we can define mouse on
        #this
        #cv2.imshow("roi",clone)


if __name__ == "__main__":
    cap = cv2.VideoCapture('video_converted.mov')

    ret, image = cap.read()
    clone = image.copy()
    cv2.namedWindow("image")
    # cv2.namedWindow("current_frame")
    cv2.createTrackbar("trackbar", "image", 0, 0, foo)
    cv2.setMouseCallback("image", click)
    # cv2.setMouseCallback("current_frame", click)


    while True:
        cv2.imshow('image', image)
        ret,image = cap.read()
        clone = image.copy()
        #gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            image = clone.copy()
        elif key==ord('q'):
            break
        if len(refPt)==2:
            print "len==2"
            roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
            cv2.imshow("ROI", roi)
            cv2.waitKey(0)

    cap.release()
    cv2.destroyAllWindows()