# from color image to gray image

import cv2
import numpy as np

img = cv2.imread("free-photo-of-people-walking-dogs-on-sidewalk-at-night.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY IMAGE", gray)


# bluring or image
blur_img = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow("BLUR IMAGE", blur_img)


# Edge Detection
imgCanny = cv2.Canny(img, 100, 100)
cv2.imshow("CANNY IMAGE", imgCanny)


# Dilation and Erode
# for Dilationn
kernel = np.ones(
    (5, 5), np.uint8
)  # unassigned integer 8 bit, meaning value can range from 0 to 255
imgDilation = cv2.dilate(gray, kernel, iterations=2)
cv2.imshow("DILATED IMAGE", imgDilation)


# for erode
imgerod = cv2.erode(gray, kernel, iterations=2)
cv2.imshow("EROD IMAGE", imgerod)
cv2.waitKey(0)
