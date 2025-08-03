# Task 2: Color Space Conversion and Histogram

import cv2
from matplotlib import pyplot as plt

# Load image
img = cv2.imread('photo.jpg')  # Replace with your actual image name if different

# Convert to color spaces
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Save each version
cv2.imwrite('photo_grayscale.jpg', gray)
cv2.imwrite('photo_hsv.jpg', hsv)
cv2.imwrite('photo_lab.jpg', lab)

# Display each version
titles = ['Grayscale', 'HSV', 'LAB']
images = [gray, hsv, lab]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.title(titles[i])
    if i == 0:
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_HSV2RGB if i == 1 else cv2.COLOR_LAB2RGB))
    plt.axis('off')
plt.show()

# Plot histogram for grayscale image
plt.figure()
plt.hist(gray.ravel(), 256, [0, 256])
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()
