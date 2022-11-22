import cv2 as cv

import numpy as np

img = cv.imread("photos/fish.png")
cv.imshow("picture_name", img)



def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
# -x --> left,
# -y --> Up
# x --> Right
# y --> Down
translated = translate(img, -100, 100)
cv.imshow("translated", translated)

# Rotation
def rotate(img,angle,rotPoint= None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions= (width, height)
    return cv.warpAffine(img,rotMat,dimensions)
rotated= rotate(img,45)
cv.imshow("rotated",rotated)
cv.imshow("rotated_rotated",rotate(rotated,45))

# resize image

resized = cv.resize(img,(500,500))
cv.imshow("resized_image",resized)


flip = cv.flip(img,-1)
cv.imshow("flip_image",flip)

cropped = img[200:400,300:400]
cv.imshow("cropping",cropped)





cv.waitKey(0)
