import cv2
import numpy as np

# stacking images together
img1 = cv2.imread("istockphoto-979251076-612x612.jpg")
img2 = cv2.imread("pexels-mehmet-turgut-kirkgoz-11758515.jpg")

print(img1.shape)

img2Resized = cv2.resize(img2, (612, 408))
print(img2Resized.shape)

# for horizontal stacking
hstack = np.hstack((img1, img2Resized))
cv2.imshow("horizontal image", hstack)
cv2.waitKey(0)

# for vertical stacking
vstack = np.vstack((img1, img2Resized))
cv2.imshow("vertical image", vstack)
cv2.waitKey(0)
