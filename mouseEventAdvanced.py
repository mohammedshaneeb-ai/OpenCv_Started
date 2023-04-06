import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
car = cv2.imread('./asset/car.jpg')
cv2.imshow('Image', img)
cv2.imshow('car', car)


def img_callback(event, x, y, flags, parm):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(img, (x, y), 2, (0, 255, 255), 1)
        if len(points) >= 2:
            cv2.line(img, (x, y), points[-2], (0, 0, 255), 2)
        cv2.imshow('Image', img)


def car_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEHWHEEL:
        blue = car[y, x, 0]
        green = car[y, x, 1]
        red = car[y, x, 2]

        myColor = np.zeros((512, 512, 3), np.uint8)
        myColor[:] = blue, green, red
        cv2.imshow('color', myColor)


points = []
cv2.setMouseCallback('Image', img_callback)
cv2.setMouseCallback('car', car_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()
