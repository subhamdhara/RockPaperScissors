import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import random_choice


cap = cv2.VideoCapture(0)
w = cap.get(cv2. CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2. CAP_PROP_FRAME_HEIGHT)
cap.set(3, w*2)
cap.set(4, h*2)
w = cap.get(cv2. CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2. CAP_PROP_FRAME_HEIGHT)
print(w,h)
detector = HandDetector(detectionCon=0.8, maxHands=1)
state = ""
while True:
    success,img = cap.read()
    imgr = cv2.imread("resources/Rock Paper Scissors.png", cv2.IMREAD_UNCHANGED)
    img = cv2.flip(img, 180)
    hands, img = detector.findHands(img, flipType=False, draw=False)
    if hands:
        hand = hands[0]
        lmList1 = hand["lmList"]
        bbox1 = hand["bbox"]
        center1 = hand["center"]
        handType1 = hand["type"]
        fingers = detector.fingersUp(hand)
        if fingers == [0, 1, 1, 0, 0]:
            state = "scissors"
        elif fingers == [1, 1, 1, 1, 1]:
            state = "paper"
        elif fingers == [0, 0, 0, 0, 0]:
            state = "rock"
        else:
            state = ""
        print(state)
        cvzone.putTextRect(img, state, (bbox1[0]-12, bbox1[1]-20))
        # print(bbox1)
        cvzone.cornerRect(img, (bbox1[0]-20, bbox1[1]-20, bbox1[2]+20*2, bbox1[3]+20*2))
    img = cvzone.overlayPNG(img, imgr)
    img = cvzone.overlayPNG(img, random_choice.comp_choice(4)[1], (100,100))

    cv2.imshow("image", img)
    cv2.waitKey(1)
