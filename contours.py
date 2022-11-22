import cv2 as cv
import numpy as np

# contours

img = cv.imread("photos/fish.png")
cv.imshow("fish", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray_fish", gray)

# methods1: to get contours (better!!!)
# get the edge of the image with canny
blur = cv.blur(gray,(3,3),cv.BORDER_DEFAULT) # blur will make the contour smaller

canny = cv.Canny(blur,125,175)
cv.imshow("canny edges",canny)

# methods2： threshold binary the image, 变成只有黑河白的图片
# ret, thresh = cv.threshold(gray, 125, 125,
#                            cv.THRESH_BINARY)  # intensity higher then 125 will be white, and lower then 125 will be black
# cv.imshow("thresh_image", thresh)

# contours 轮廓 更加倾向于圈起来的圆圈
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("contour draw", blank)

cv.waitKey(0)

cv.destroyAllWindows()
