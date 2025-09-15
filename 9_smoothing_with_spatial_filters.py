import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Smoothning with spatial filter
img3 = cv2.blur(img, (3,3)) #3x3 filter
img5 = cv2.blur(img, (5,5)) #5x5 filter

#plotting
plt.figure(figsize=(15,5))
plt.subplot(1,3,1); plt.imshow(img, cmap='gray'); plt.title('Original')
plt.subplot(1,3,2); plt.imshow(img3, cmap='gray'); plt.title('3x3')
plt.subplot(1,3,3); plt.imshow(img5, cmap='gray'); plt.title('5x5')
plt.tight_layout(); plt.show()
