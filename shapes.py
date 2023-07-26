import numpy as np
import cv2

img = np.zeros((500, 500, 3))
print(img.shape)

img[:] = 255, 0, 0

cv2.imshow("image", img)
cv2.waitKey(0)

# adding color to image
