import cv2
import numpy as np
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)


def click_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = str(x) + ' '+str(y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x, y), font, 1, (0, 0, 255), 2)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y),15,(0,255,0),2)
        cv2.imshow('image', img)

cv2.setMouseCallback('image', click_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()


