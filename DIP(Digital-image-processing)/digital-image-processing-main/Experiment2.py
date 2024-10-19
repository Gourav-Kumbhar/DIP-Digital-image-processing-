import cv2
import matplotlib.pyplot as plt

image_path = 'Images/flower.jpg' 
image = cv2.imread(image_path)
b, g, r = cv2.split(image)

# Calculate the histograms for each channel
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Plot the histograms
plt.figure(figsize=(12, 6))

plt.title('Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(hist_b, color='blue')
plt.plot(hist_g, color='green')
plt.plot(hist_r, color='red')
plt.xlim([0, 256])
plt.show()