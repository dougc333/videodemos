
import cv2
import numpy as np

#assumes BGR input
def BGRgrayscale(img):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def RGBgrayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def canny(img):
    # compute median of pixels, use this to set low/high threshold?
    median = np.median(img)
    sigma = 0.33
    lower = int(max(0, (1. - sigma) * median))
    upper = int(min(0, (1. + sigma) * median))

    return cv2.Canny(img, lower, upper)

def gaussian_blur(img):
    return cv2.GaussianBlur(img, (3, 3), 0)

def hough(img):
    print "calling hough"


#change color space from openCV BGR to matlabplot.pyplot RGB
def matlabRGB(img):
    return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
