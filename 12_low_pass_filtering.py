"""Task: Low-Pass Filtering in Frequency Domain"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
rows, cols = img.shape; crow, ccol = rows//2, cols//2
mask = np.zeros_like(img); r = 30; mask[crow-r:crow+r, ccol-r:ccol+r] = 1
fshift_lp = fshift * mask
img_lp = np.fft.ifft2(np.fft.ifftshift(fshift_lp)).real
plt.figure(figsize=(8,4))
plt.subplot(1,2,1); plt.imshow(img, cmap='gray'); plt.title('Original')
plt.subplot(1,2,2); plt.imshow(img_lp, cmap='gray'); plt.title('Low-Pass')
plt.axis('off'); plt.tight_layout(); plt.show()
# Low-pass filter blurs image by removing high frequencies.
