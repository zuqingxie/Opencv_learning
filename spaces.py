
import cv2 as cv
# import matplotlib.pyplot as plt

img = cv.imread("photos/fish.png")
cv.imshow("fish_image",img)

# gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray_fish_image",gray)


# hsv
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv_fish_image",hsv)

# lab
lab =cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB image", lab)

#
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

cv.waitKey(0)