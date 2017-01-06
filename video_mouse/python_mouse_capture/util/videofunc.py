import cv2
import shutil
import os

#input capture device
#output store video as numpy 2d arrays in text files
def store_as_numpy(capture):
    try:
        ret_code,frame = capture.read()
    except:
        print 'cannot read from capture input'
    print ret_code
    print frame
    num = 0

    try:
        if os.path.isdir('temp'):
            shutil.rmtree('temp')
        else:
            os.mkdir('temp')
    except:
        print "temp dir problems"

    path = '/Users/dc/videodemos/video_js/python_mouse_capture/temp/'

    while (ret_code==True):
        try:
            f = open(path+str(num)+".txt",'w')
            f.write(str(frame))
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could not convert data to an integer."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise

        ret_code, frame = capture.read()


