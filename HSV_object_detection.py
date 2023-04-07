import cv2
import numpy as np


def nothing(x):
    pass

cv2.namedWindow('Trackbar')
img = cv2.imread('./asset/ball.webp')
img = cv2.resize(img,(800,500))
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.createTrackbar('lh', 'Trackbar',0,255,nothing)
cv2.createTrackbar('ls', 'Trackbar',0,255,nothing)
cv2.createTrackbar('lv', 'Trackbar',0,255,nothing)
cv2.createTrackbar('uh', 'Trackbar',255,255,nothing)
cv2.createTrackbar('us', 'Trackbar',255,255,nothing)
cv2.createTrackbar('uv', 'Trackbar',255,255,nothing)

while True:
    cv2.imshow('Ball', img)

    l_h = cv2.getTrackbarPos('lh', 'Trackbar')
    l_s = cv2.getTrackbarPos('ls', 'Trackbar')
    l_v = cv2.getTrackbarPos('lv', 'Trackbar')
    u_h = cv2.getTrackbarPos('uh', 'Trackbar')
    u_s = cv2.getTrackbarPos('us', 'Trackbar')
    u_v = cv2.getTrackbarPos('uv', 'Trackbar')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(img,img, mask=mask)

    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cv2.destroyAllWindows()
