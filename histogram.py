import cv2 as cv
import numpy as np

img = cv.imread("photos/fish.png")
cv.imshow("fish_image", img)
# blank = np.zeros(img.shape[:2], dtype="uint8") # mask size must the same as the original picture!!!!
# cv.imshow("blank_image", blank)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

gray_hist = cv.

cv.waitKey(0)
