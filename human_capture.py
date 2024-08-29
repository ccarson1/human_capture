import cv2
from cvzone.PoseModule import PoseDetector


cap = cv2.VideoCapture('videos/dance.mp4')
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 800, 600)  

detector = PoseDetector()
posList = []

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)

    if bboxInfo:
        lmString = ''
        for lm in lmList:
            print(lm)
            lmString += f'{lm[0]},{img.shape[0]-lm[1]},{lm[2]},'
        posList.append(lmString)

    
    print(posList)

    cv2.imshow("Image", img)
    key  = cv2.waitKey(1)
    if key == ord('s'):
        with open("Animationfile.txt", "w") as f:
            f.writelines(["%s\n" % item for item in posList])


# import cv2
# from cvzone.PoseModule import PoseDetector

# cap = cv2.VideoCapture('videos/dance.mp4')
# cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Image", 800, 600)  

# detector = PoseDetector()


# movement_data = []

# while True:
#     success, img = cap.read()
#     if not success:
#         break

#     # Detect pose and get landmarks and bounding box info
#     img = detector.findPose(img)
#     lmList, bboxInfo = detector.findPosition(img)
    
#     # Store landmark positions
#     frame_data = {}
#     for i, landmark in enumerate(lmList):
#         frame_data[f'landmark_{i}'] = landmark

#     movement_data.append(frame_data)
    

#     cv2.imshow("Image", img)

# cap.release()
# cv2.destroyAllWindows()


# import json
# with open('movement_data.json', 'w') as f:
#     json.dump(movement_data, f)
