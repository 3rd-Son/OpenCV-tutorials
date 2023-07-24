# from color image to gray image

import cv2

img = cv2.imread("free-photo-of-people-walking-dogs-on-sidewalk-at-night.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY IMAGE", gray)
cv2.waitKey(0)
