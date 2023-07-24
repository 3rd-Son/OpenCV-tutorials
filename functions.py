# from color image to gray image

import cv2

img = cv2.imread("free-photo-of-people-walking-dogs-on-sidewalk-at-night.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY IMAGE", gray)


# bluring or image
blur_img = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow("BLUR IMAGE", blur_img)


# Edge Detection
imgCanny = cv2.Canny(img, 100, 100)
cv2.imshow("CANNY IMAGE", imgCanny)
cv2.waitKey(0)
