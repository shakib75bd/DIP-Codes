"""Task: Fourier Transform and Spectrum Visualization"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude = 20*np.log(np.abs(fshift)+1)
plt.figure(figsize=(8,4))
plt.subplot(1,2,1); plt.imshow(img, cmap='gray'); plt.title('Image')
plt.subplot(1,2,2); plt.imshow(magnitude, cmap='gray'); plt.title('Spectrum')
plt.axis('off'); plt.tight_layout(); plt.show()
# Low frequencies: center, high: edges; low freq = smooth, high = details.
