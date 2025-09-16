import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

x = np.arange(img.shape[1])
noisy = (30*np.sin(2*np.pi*x/20)).astype('uint8')
noiseImage = np.tile(noisy, (img.shape[0], 1))
noise = cv2.add(img, noiseImage)

f = np.fft.fft2(noise)
fshift = np.fft.fftshift(f)

mask = np.ones_like(noise);
mask[:, 30:65]=0; mask[:, -65:-30]=0
fshift_nf = fshift*mask
filtered = np.fft.ifft2(np.fft.ifftshift(fshift_nf)).real

plt.figure(figsize=(15,5))
plt.subplot(1,3,1); plt.imshow(img, cmap='gray');plt.title('Original')
plt.subplot(1,3,2); plt.imshow(noise, cmap='gray');plt.title('Noisy')
plt.subplot(1,3,3); plt.imshow(filtered, cmap='gray');plt.title('Filtered')

plt.tight_layout(); plt.show()
