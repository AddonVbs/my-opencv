import cv2 as cv

img = cv.imread("tmb_14441_4994.jpg")
cv.imshow("res",img)

img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",img1)

img2= cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("fgfg",img2)

cv.waitKey(0)