"""Task: Negative of an Image"""
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
neg = 255 - img
plt.figure(figsize=(8,4))
plt.subplot(1,2,1); plt.imshow(img, cmap='gray'); plt.title('Original')
plt.subplot(1,2,2); plt.imshow(neg, cmap='gray'); plt.title('Negative')
plt.axis('off'); plt.tight_layout(); plt.show()
# Negative image inverts intensities, making dark areas light and vice versa.
