import cv2
import numpy as np


img = cv2.imread("card.jpeg")
width, height = 250, 350
pts1 = np.float32(
    [[234, 60], [341, 53], [254, 213], [367, 203]]
)  # https://www.mobilefish.com/services/record_mouse_coordinates/record_mouse_coordinates.php
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutpout = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("card", img)
cv2.imshow("cardoutput", imgOutpout)

cv2.waitKey(0)
