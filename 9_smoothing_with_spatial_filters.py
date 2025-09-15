"""Task: Smoothing with Spatial Filters"""
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
smooth3 = cv2.blur(img, (3,3))
smooth5 = cv2.blur(img, (5,5))
plt.figure(figsize=(12,4))
for i, im in enumerate([img, smooth3, smooth5]):
    plt.subplot(1,3,i+1); plt.imshow(im, cmap='gray'); plt.title(['Original','3x3','5x5'][i])
plt.axis('off'); plt.tight_layout(); plt.show()
# Larger kernels blur more, reducing noise and details.
