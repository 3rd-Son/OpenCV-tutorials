import cv2

# print("sucessfully")

# # Reading images
# img = cv2.imread("pexels-chikinbun-10867806.jpg")
# cv2.imshow("first image", img)
# cv2.waitKey(0)

# # reading videos
# vid = cv2.VideoCapture("pexels-kampus-production-8730551 (2160p).mp4")
# while True:
#     success, img = vid.read()
#     cv2.imshow("first video", img)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# using laptop camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("first video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
