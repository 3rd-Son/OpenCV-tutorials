import numpy as np
import cv2

img = np.zeros((500, 500, 3))
print(img.shape)


# adding color to image
img[:] = 255, 0, 0


# adding line
cv2.line(img, (0, 0), (200, 200), (0, 0, 255))

# adding text
cv2.putText(
    img, "This is a text", (150, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (30, 255, 0)
)
cv2.imshow("image", img)
cv2.waitKey(0)
