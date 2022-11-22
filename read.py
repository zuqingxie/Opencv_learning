
import cv2 as cv

import numpy as np

img = cv.imread("photos/Figure_1_.png")
cv.imshow("picture_name", img)

cv.waitKey(100000)

# but opencv cannot handle with image which is bigger than windows screen

# reading video

capture = cv.VideoCapture(0)
while True:
    isTrue,frame = capture.read()
    cv.imshow("video_name", frame)
    if cv.waitKey(20) & 0xFF ==ord('d'):
        break
capture.release()
cv.destroyAllWindows()