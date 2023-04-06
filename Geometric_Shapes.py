import cv2 as cv


img = cv.imread('./asset/car.jpg', 1)
cv.line(img, (100, 50), (50, 100), (255, 0, 0), 10)
cv.circle(img, (200, 200), 80, (255, 0, 0), 5)
cv.rectangle(img, (100, 100), (200,200), (0, 0, 255), 10)
cv.putText(img, "Lambo", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

cv.imshow('Profile', img)

cv.waitKey(0)
