import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread("lol.png")
cv.imshow("1",img)

img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',img1)

lap = cv.Laplacian(img1, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lap',lap)

soblex = cv.Sobel(img1,cv.CV_64F,1,0)
sobley = cv.Sobel(img1,cv.CV_64F,0,1)
combinate_sobol = cv.bitwise_or(soblex,sobley)

cv.imshow('sobel x ', soblex)
cv.imshow('sobol y ',sobley)
cv.imshow('comninate',combinate_sobol)


cv.waitKey(0)