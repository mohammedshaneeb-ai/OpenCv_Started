import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('./asset/j.png')

kernal = np.ones((5,5), np.uint8)

erosion = cv2.erode(img,kernal,iterations=1)
dilation = cv2.dilate(img, kernal, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal, iterations=1)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernal, iterations=1)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernal, iterations=1)


images = [img, erosion, dilation, opening, closing, gradient]
titles = ['Original', 'Erosion','Dilation','Opening', 'Closing', 'Gradient']
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.title(titles[i])
    plt.imshow(images[i])

    plt.xticks([])
    plt.yticks([])


plt.show()
