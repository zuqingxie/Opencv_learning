import cv2 as cv

import numpy as np
from caer.transforms import scale


# but opencv cannot handle with image which is bigger than windows screen
def rescaleFrame(frame, scale=0.75):
    # works for video, Image and camera
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # only for live camera
    capture.set(3,width)
    capture.set(4,height)
    pass

img = cv.imread("photos/Figure_1_.png")
cv.imshow("picture_name", img)

img_rescale = rescaleFrame(img)
cv.imshow("rescaled image", img_rescale)


capture = cv.VideoCapture(1) # 0 is the back-webcame 1is front camera and "path"
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.2)  # scale factor 0.2
    cv.imshow("video_name", frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
