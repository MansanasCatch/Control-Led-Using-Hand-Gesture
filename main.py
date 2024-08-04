import cv2
from cvzone.HandTrackingModule import HandDetector
import controller as cnt

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # With Draw

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right

        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmarks points
            bbox2 = hand2["bbox"]  # Bounding Box info x,y,w,h
            centerPoint2 = hand2["center"]  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type Left or Right

            fingers2 = detector.fingersUp(hand2)
            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)  # with draw

        print(fingers1)
        #[Thumb, Index, Middle, Ring, Little]
        up_finger = []
        if lmList1:
            cnt.led("")
            if fingers1[0] == 1:
                up_finger.append("Thumb")
                cnt.led("1")
            if fingers1[0] == 0:
                cnt.led("6")
            if fingers1[1] == 1:
                up_finger.append("Index")
                cnt.led("2")
            if fingers1[1] == 0:
                cnt.led("7")
            if fingers1[2] == 1:
                up_finger.append("Middle")
                cnt.led("3")
            if fingers1[2] == 0:
                cnt.led("8")
            if fingers1[3] == 1:
                up_finger.append("Ring")
                cnt.led("4")
            if fingers1[3] == 0:
                cnt.led("9")
            if fingers1[4] == 1:
                up_finger.append("Little")
                cnt.led("5")
            if fingers1[4] == 0:
                cnt.led("0")

        cv2.putText(img,','.join(up_finger), (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
