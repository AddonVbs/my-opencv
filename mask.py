import cv2 as cv
import numpy as np

img = cv.imread("lol.png")
cv.imshow("1",img)

blank = np.zeros(img.shape[:2],dtype="uint8")

mask1 = cv.circle(blank.copy(),(800,400),300,255,-1)
maks = cv.rectangle(blank.copy(),(400,400),(200,30),255,-1)


masked = cv.bitwise_and(img,img,mask=maks)
cv.imshow("mask",masked)



cv.waitKey(0)