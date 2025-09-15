"""Task: Contrast Stretching"""
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
minV, maxV = img.min(), img.max()
stretched = ((img-minV)*255/(maxV-minV)).astype('uint8')
plt.figure(figsize=(8,4))
plt.subplot(1,2,1); plt.imshow(img, cmap='gray'); plt.title('Original')
plt.subplot(1,2,2); plt.imshow(stretched, cmap='gray'); plt.title('Stretched')
plt.axis('off'); plt.tight_layout(); plt.show()
# Stretching expands pixel range, enhancing contrast.
