import cv2
import numpy as np

img1 = np.zeros((500, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

img2 = cv2.imread('./asset/binary_image.webp')
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))

bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img1, img2)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot = cv2.bitwise_not(img1)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)


cv2.imshow('BitAnd', bitAnd)
cv2.imshow('BitOr', bitOr)
cv2.imshow('BitXor', bitXor)
cv2.imshow('BitNot', bitNot)



cv2.waitKey(0)