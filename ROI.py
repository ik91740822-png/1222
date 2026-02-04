import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")

roi = img[120:400, 120:300]
cv2.imshow("ROI",roi)
cv2.moveWindow('ROI',500,50)

imgGray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)
img[120:400, 120:300] = imgGray

cv2.imshow("img",img)
cv2.imshow("Gray",imgGray)

cv2.waitKey(0)
