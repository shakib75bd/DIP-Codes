import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

#Low pass filtering in freq domain
f = np.fft.fft2(img)
fshift=np.fft.fftshift(f)

rows,cols = img.shape
crow = rows//2
ccol = cols//2

mask = np.zeros_like(img);
mask[crow-30:crow+30 , ccol-30:ccol+30] = 1

fshift_lp = fshift * mask
img_lp = np.fft.ifft2(np.fft.ifftshift(fshift_lp)).real

plt.figure(figsize=(10,5))
plt.subplot(1,2,1); plt.imshow(img, cmap='gray');plt.title('Original')
plt.subplot(1,2,2); plt.imshow(img_lp, cmap='gray');plt.title('Low-pass')

plt.tight_layout(); plt.show()
