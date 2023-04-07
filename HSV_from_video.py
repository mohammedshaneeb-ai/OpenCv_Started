import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lg = np.array([37, 43, 16])
    ug = np.array([89, 255, 255])

    mask = cv2.inRange(hsv, lg, ug)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Video', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Res', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
