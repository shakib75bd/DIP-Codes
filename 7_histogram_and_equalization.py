"""Task: Histogram and Histogram Equalization"""
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
eq = cv2.equalizeHist(img)
plt.figure(figsize=(10,4))
plt.subplot(2,2,1); plt.imshow(img, cmap='gray'); plt.title('Original')
plt.subplot(2,2,2); plt.imshow(eq, cmap='gray'); plt.title('Equalized')
plt.subplot(2,2,3); plt.hist(img.ravel(),256); plt.title('Orig Hist')
plt.subplot(2,2,4); plt.hist(eq.ravel(),256); plt.title('Eq Hist')
plt.tight_layout(); plt.show()
# Equalization spreads intensities, improving contrast.
