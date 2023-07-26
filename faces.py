# import cv2


# facescascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
# img = cv2.imread("faces.jpeg")
# imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = facescascade.detectMultiScale(img, 1.1, 4)

# for x, y, w, h in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
# cv2.imshow("girlface", img)

# cv2.waitKey(0)


# ------VIDEO----

import cv2


facescascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = facescascade.detectMultiScale(gray, 1.1, 4)
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("Video", img)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
