import numpy as np
from ultralytics import YOLO
import cvzone
from cv2 import cv2
import math
import pokerhand

#detection using webcam
cap=cv2.VideoCapture(0);
cap.set(3, 640)
cap.set(4, 480)

# detection of vehicles in video file
#cap = cv2.VideoCapture("./resources/videos/poker_hand.mp4")

model = YOLO('./weights/pokerhand.pt')

classnames = {0: '10C', 1: '10D', 2: '10H', 3: '10S', 4: '2C', 5: '2D', 6: '2H', 7: '2S', 8: '3C', 9: '3D', 10: '3H', 11: '3S', 12: '4C', 13: '4D', 14: '4H', 15: '4S', 16: '5C', 17: '5D', 18: '5H', 19: '5S', 20: '6C', 21: '6D', 22: '6H', 23: '6S', 24: '7C', 25: '7D', 26: '7H', 27: '7S', 28: '8C', 29: '8D', 30: '8H', 31: '8S', 32: '9C', 33: '9D', 34: '9H', 35: '9S', 36: 'AC', 37: 'AD', 38: 'AH', 39: 'AS', 40: 'JC', 41: 'JD', 42: 'JH', 43: 'JS', 44: 'KC', 45: 'KD', 46: 'KH', 47: 'KS', 48: 'QC', 49: 'QD', 50: 'QH', 51: 'QS'}
#mask=cv2.imread("./resources/image/mask.png")

#tracking using sort library
#tracker=Sort(max_age=20,min_hits=3, iou_threshold=0.3)


while True:
    success, img = cap.read()
    detection_region=img
    results = model(detection_region, stream=True)
    hand=[]


    for r in results:
        boxes = r.boxes
        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            #print(x1, y1, x2, y2)

            # confidence
            conf = math.ceil((box.conf[0] * 100))
            #print(conf)

            # classname
            cls = box.cls[0]
            cls = int(cls)


            #only detecting PPE
            if cls:
            # cvzone.putTextRect(img, f'{classnames[cls]} {conf}', (max(0, x1), max(25, y1-20)), colorT=(255,255,0), colorB=(0,0,0), thickness=1, offset=2)

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255,0), 1)
                cv2.putText(img, f'{classnames[cls]} {conf}', (max(0, x1), max(10, y1 - 10)), cv2.FONT_HERSHEY_PLAIN, 1,
                        (0, 255, 0))
                hand.append((classnames[cls]))

    hand_type=set(hand)
    #print(hand_type)
    if(len(hand_type)==5):
        hand_text=pokerhand.find_poker_hand(hand_type)
        cvzone.putTextRect(img, f'{(hand_text)}', (50, 50), 3,3, (0,255,0))
    cv2.imshow("Detection region", detection_region)
    #cv2.waitKey(0)
    # Press Esc to exit the loop
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()
