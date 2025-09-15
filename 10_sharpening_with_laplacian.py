"""Task: Sharpening with Laplacian Filter"""
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F)
sharp = cv2.convertScaleAbs(img + lap)
plt.figure(figsize=(8,4))
plt.subplot(1,2,1); plt.imshow(img, cmap='gray'); plt.title('Original')
plt.subplot(1,2,2); plt.imshow(sharp, cmap='gray'); plt.title('Sharpened')
plt.axis('off'); plt.tight_layout(); plt.show()
# Laplacian enhances edges, making features more distinct.
