import cv2 as cv
import numpy as np

img = cv.imread("photos/fish.png")
cv.imshow("fish_image", img)
blank = np.zeros(img.shape[:2], dtype="uint8") # mask size must the same as the original picture!!!!
cv.imshow("blank_image", blank)



mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
cv.imshow("mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked img", masked)
cv.waitKey(0)
