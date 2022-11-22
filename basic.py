import cv2 as cv

import numpy as np

img = cv.imread("photos/Figure_1_.png")
# cv.imshow("picture_name", img)

# gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

# Edge Cascade
canny = cv.Canny(blur, 25, 275)
cv.imshow("canny_edge", canny)

# dilate 扩张
dilate = cv.dilate(canny, (7, 7), iterations = 5)
cv.imshow("dilated_candy", dilate)

# Eroding 侵蚀
erode = cv.erode(dilate, (7, 7), iterations = 5)
cv.imshow("erode", erode)

# resize
resized = cv.resize(img, (1000, 500), interpolation = cv.INTER_CUBIC)
cv.imshow("resized_image", resized)

# cropped = cut
cropped = img[50:300, 200:600]
cv.imshow("cropped_image", cropped)

cv.waitKey(0)
