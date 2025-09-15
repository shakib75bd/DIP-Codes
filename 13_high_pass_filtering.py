"""Task: High-Pass Filtering in Frequency Domain"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
rows, cols = img.shape; crow, ccol = rows//2, cols//2
mask = np.ones_like(img); r = 30; mask[crow-r:crow+r, ccol-r:ccol+r] = 0
fshift_hp = fshift * mask
img_hp = np.fft.ifft2(np.fft.ifftshift(fshift_hp)).real
plt.figure(figsize=(8,4))
plt.subplot(1,2,1); plt.imshow(img, cmap='gray'); plt.title('Original')
plt.subplot(1,2,2); plt.imshow(img_hp, cmap='gray'); plt.title('High-Pass')
plt.axis('off'); plt.tight_layout(); plt.show()
# High-pass filter enhances edges and fine details.
