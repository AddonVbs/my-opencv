import cv2 as cv
import numpy

img = cv.imread("tmb_14441_4994.jpg")
#cv.imshow("res",img)

img1 = cv.blur(img, (7,7))
cv.imshow("rf",img1)

gass = cv.GaussianBlur(img, (7,7),0)
cv.imshow("fdf",gass)

vi = cv.bilateralFilter(img,10,35,25)
cv.imshow("rtrt",vi)





cv.waitKey(0)