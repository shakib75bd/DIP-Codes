"""Task: Bit-Plane Slicing"""
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
planes = [(img >> i) & 1 for i in range(7, -1, -1)]
plt.figure(figsize=(16,3))
for i, bp in enumerate(planes):
    plt.subplot(1,8,i+1); plt.imshow(bp*255, cmap='gray'); plt.title(f'Bit {7-i}')
plt.axis('off'); plt.tight_layout(); plt.show()
# MSB planes hold most image info, LSB planes show fine details/noise.
