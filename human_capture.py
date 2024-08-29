import cv2
from cvzone.PoseModule import PoseDetector


cap = cv2.VideoCapture('videos/dance.mp4')
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 800, 600)  

detector = PoseDetector()

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
