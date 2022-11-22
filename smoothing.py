
import cv2 as cv


img = cv.imread("photos/fish.png")
cv.imshow("fish_image",img)

# average blur
average = cv.blur(img, (3,3),)
cv.imshow("average blur", average)

# Gaussian blur perticial weights in every pixel

gaussian = cv.GaussianBlur(img,(3,3),0)
cv.imshow("gaussian blur",gaussian)

# median blur

median = cv.medianBlur(img,3)
cv.imshow("median blur", median)

# Bilateral will keep the edges but still blur others
bilateral = cv.bilateralFilter(img,5,30,30)
cv.imshow("bilateral blur",bilateral)

cv.waitKey(0)