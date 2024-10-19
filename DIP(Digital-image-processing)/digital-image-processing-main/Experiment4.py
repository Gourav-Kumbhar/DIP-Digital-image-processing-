import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('flower.jpg')

height, width, _ = image.shape

gray_image = np.dot(image[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)

plt.imshow(gray_image)
