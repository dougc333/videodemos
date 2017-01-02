#python opencv_mouse.py. Assumes imagefile.jpg is in working directory

import cv2

refPt = []
cropping = False


def click(event,x,y,flags,param):
    global refPt, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        print 'leftbuttondown x:', x+" y:",y
        refPt=[(x,y)]
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        print 'leftbuttonup x:',x+" y:",y
        refPt.append((x,y))
        cropping = False
        green_color = (0,255,0)
        cv2.rectangle(image,refPt[0], refPt[1], green_color,2)
        cv2.imshow("image",image)




image = cv2.imread('imagefile.jpg')
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image",click)

while True:
    cv2.imshow("image",image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('r'):
        image = clone.copy()
    elif key==ord('c'):
        break
if len(refPt)==2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)

cv2.destroyAllWindows()




