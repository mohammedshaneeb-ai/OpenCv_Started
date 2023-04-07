import numpy as np

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./asset/OpenCV_logo.png')
kernel = np.ones((2,2), np.float32)/4
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img,(5,5))
guassian_Blur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, (5))
bilateral_filter = cv2.bilateralFilter(img,9, 75,75)


images = [img,dst, blur, guassian_Blur, median, bilateral_filter]
titles = ['Original', '2Dconvolution','blur', 'guassian_blur', 'median', 'bilateral_filter']

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])

    plt.xticks([])
    plt.yticks([])

plt.show()