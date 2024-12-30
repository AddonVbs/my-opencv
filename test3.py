import cv2 as cv
import numpy as np

black = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(black.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(black.copy(),(200,200),200,255,-1)
cv.imshow('rex', rectangle)
cv.imshow("flock", circle)

bit = cv.bitwise_and(rectangle,circle)
cv.imshow("fffg",bit)

bit1 = cv.bitwise_or(rectangle,circle)
cv.imshow("ff",bit1)

bit2 = cv.bitwise_xor(rectangle,circle)
cv.imshow("ffgf",bit2)

bit3 = cv.bitwise_not(circle)
cv.imshow("ffe",bit3)

cv.waitKey(0)