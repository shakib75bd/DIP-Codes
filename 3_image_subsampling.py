"""Task: Image Subsampling"""
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img2 = img[::2, ::2]
img4 = img[::4, ::4]
img8 = img[::8, ::8]
plt.figure(figsize=(10,4))
for i, im in enumerate([img, img2, img4, img8]):
    plt.subplot(1,4,i+1); plt.imshow(im, cmap='gray'); plt.title(f'Factor {2**i}')
plt.axis('off'); plt.tight_layout(); plt.show()
# Subsampling reduces resolution and details, making the image blockier.
