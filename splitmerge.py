
import cv2 as cv
import numpy as np
# import matplotlib.pyplot as plt
# split RGB to R.G and B channel
img = cv.imread("photos/fish.png")
cv.imshow("fish_image",img)
blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r =cv.split(img)
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
color_b = cv.merge([b,blank,blank])
color_g = cv.merge([blank,g,blank])
color_r = cv.merge([blank,blank,r])
cv.imshow("color_blue",color_b)
cv.imshow("color_green",color_g)
cv.imshow("color_red",color_r)

# merge r,g,b, together again

merge = cv.merge([b,g,r])
cv.imshow("merge",merge)

cv.waitKey(0)