import cv2 as cv

import numpy as np

# img = cv.imread("photos/Figure_1_.png")
# cv.imshow("picture_name", img)


# draw a rectangle and blank
blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow("blank_image",blank)
blank[200:300,300:400] = 0,255,0
color = (0,0,255)
cv.rectangle(blank,(0,0),(300,200),color,thickness=15)   # thickness=cv.FILLED


# # draw a circle
# cv.circle(blank,(300,300),50,(255,33,33),thickness=-1) # thickness=cv.
# cv.line(blank,(20,200),(300,500),(200,234,67),thickness=10) # thickness=cv.10
#
# # write text in image
# cv.putText(blank, "Hello", (300,300), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)


cv.imshow("Green_blank",blank)



cv.waitKey(0)
