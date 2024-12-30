import cv2 as cv
import numpy as np

img = cv.imread("tmb_14441_4994.jpg")
cv.imshow('cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('fg',blank)

mask = cv.rectangle(blank,(200,500),(355,555),255,-1)
cv.imshow("f",mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("f32",masked)

cv.waitKey(0)