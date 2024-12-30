import cv2 as cv 
import numpy as np 
img = cv.imread("testOpencv/elif.png")
cv.imshow("r",img)
blank = np.zeros(img.shape[:2],dtype="uint8")
cv.imshow("ff",img)

img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img = cv.GaussianBlur(img,(3,3),0)

mask = cv.rectangle(blank.copy(),(1400,1500),(400,500),255,-1)
masked = cv.bitwise_and(img,img,mask=mask)

cv.imshow("mask",masked)




cv.waitKey(0)