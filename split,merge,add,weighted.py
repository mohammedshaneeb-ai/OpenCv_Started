import cv2

# Reading Images
car = cv2.imread('./asset/car.jpg')
bird = cv2.imread('./asset/bird.jpg')

# Resizing Two Images to same scale
car = cv2.resize(car, (512, 512))
bird = cv2.resize(bird, (512, 512))

# Splitting images into 3 channels
b, g, r = cv2.split(bird)

# Merging Images
bird_merged = cv2.merge((b, g, r))

# Adding two Images
added = cv2.add(car, bird)

# Adding Images with Giving weight
weighted_add = cv2.addWeighted(car, .7, bird, .3, 0)

# Showing All Images Mentioned Above
cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)

cv2.imshow('car', car)
cv2.imshow('bird', bird)
cv2.imshow('bird_merged', bird_merged)
cv2.imshow('added', added)
cv2.imshow('weighted_add', weighted_add)


cv2.waitKey(0)
cv2.destroyAllWindows()
