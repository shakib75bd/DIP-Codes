"""Task: Notch Filtering for Periodic Noise Removal"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
x = np.arange(img.shape[1]); noise = (30*np.sin(2*np.pi*x/20)).astype('uint8')
noise_img = np.tile(noise, (img.shape[0], 1))
noisy = cv2.add(img, noise_img)
f = np.fft.fft2(noisy); fshift = np.fft.fftshift(f)
mask = np.ones_like(noisy); mask[:, 60:65] = 0; mask[:, -65:-60] = 0
fshift_nf = fshift * mask
filtered = np.fft.ifft2(np.fft.ifftshift(fshift_nf)).real
plt.figure(figsize=(12,4))
plt.subplot(1,3,1); plt.imshow(img, cmap='gray'); plt.title('Original')
plt.subplot(1,3,2); plt.imshow(noisy, cmap='gray'); plt.title('Noisy')
plt.subplot(1,3,3); plt.imshow(filtered, cmap='gray'); plt.title('Filtered')
plt.axis('off'); plt.tight_layout(); plt.show()
# Notch filter removes periodic noise at specific frequencies.
