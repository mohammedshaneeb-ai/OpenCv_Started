import cv2

img = cv2.imread('./asset/sudoku.jpg.crdownload',0)

th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Sudoko', img)
cv2.imshow('thresh_Mean', th1)
cv2.imshow('thresh_Gaussian', th2)

cv2.waitKey(0)
cv2.destroyAllWindows()