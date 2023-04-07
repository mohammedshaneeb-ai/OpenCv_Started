import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./asset/car.jpg')

img_gred = cv2.imread('./asset/gradient.jpeg')
_, th1 = cv2.threshold(img_gred, 130, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img_gred, 130, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img_gred, 130, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img_gred, 130, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img_gred, 130, 255, cv2.THRESH_TOZERO_INV)
_, th6 = cv2.threshold(img_gred, 130, 255, cv2.THRESH_MASK)

# We are converting BGR to RGB because matplotlib read images in RGB format
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow('car', img)

plt.imshow(img)
plt.xticks([])
plt.yticks([])

title = ['Binary', 'Binary_inverse', 'Trunc', 'Tozero', 'Tozero_inverse', 'Mask']
images = [th1, th2, th3, th4, th5, th6]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
