# Bit-Plane Slicing

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

def bit_p(img,x):
	return ((img >> x) & 1) * 255

plt.figure(figsize=(20,5))
plt.title('8 Bit-Plane Slicing (0-7)')
plt.subplot(1,8,1); plt.imshow(bit_p(img,0), cmap='gray'); plt.title('Bit 0')
plt.subplot(1,8,2); plt.imshow(bit_p(img,1), cmap='gray'); plt.title('Bit 1')
plt.subplot(1,8,3); plt.imshow(bit_p(img,2), cmap='gray'); plt.title('Bit 2')
plt.subplot(1,8,4); plt.imshow(bit_p(img,3), cmap='gray'); plt.title('Bit 3')
plt.subplot(1,8,5); plt.imshow(bit_p(img,4), cmap='gray'); plt.title('Bit 4')
plt.subplot(1,8,6); plt.imshow(bit_p(img,5), cmap='gray'); plt.title('Bit 5')
plt.subplot(1,8,7); plt.imshow(bit_p(img,6), cmap='gray'); plt.title('Bit 6')
plt.subplot(1,8,8); plt.imshow(bit_p(img,7), cmap='gray'); plt.title('Bit 7')

plt.axis('off')
plt.tight_layout()
plt.show()
