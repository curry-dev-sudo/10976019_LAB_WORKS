# Task 1: Image Loading and Grayscale Conversion

import cv2
from matplotlib import pyplot as plt

# Load original image
img = cv2.imread('photo.jpg')  # Make sure photo.jpg is in the same directory or uploaded
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save grayscale image
cv2.imwrite('photo_gray.jpg', gray)

# Display both images
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Grayscale Image")
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.show()
