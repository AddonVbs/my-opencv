import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("lol.png")
cv.imshow("main",img)

#img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray', img_gray)

img_hist = cv.calcHist([img_gray],[0],None,[256],[0,256])
plt.figure()
plt.title('gray his')
plt.xlabel('bins')
plt.ylabel(' # of pixels')
plt.plot(img_hist)
plt.xlim([0,256]) 
plt.show()


cv.waitKey(0)