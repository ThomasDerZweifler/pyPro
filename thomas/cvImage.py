import cv2 as cv
import sys
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("img/test.png")

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("image", img)

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
plt.imshow(hist, interpolation = 'nearest')
plt.show()

k = cv.waitKey(0)

