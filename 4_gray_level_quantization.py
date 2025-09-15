"""Task: Gray-Level Quantization"""
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
levels = [2, 4, 8, 16, 256]
imgs = [(img//(256//l))*(255//(l-1)) for l in levels]
plt.figure(figsize=(15,3))
for i, im in enumerate(imgs):
    plt.subplot(1,5,i+1); plt.imshow(im, cmap='gray'); plt.title(f'{levels[i]} levels')
plt.axis('off'); plt.tight_layout(); plt.show()
# Fewer levels cause visible banding and loss of detail.
