import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img2 = img[::2, ::2]
img3 = img[::4, ::4]
img4 = img[::8, ::8]

plt.figure(figsize=(10,4))
plt.subplot(1,4,1); plt.imshow(img, cmap='gray'); plt.title('original')
plt.subplot(1,4,2); plt.imshow(img2, cmap='gray'); plt.title('2 sample')
plt.subplot(1,4,3); plt.imshow(img3, cmap='gray'); plt.title('4 sample')
plt.subplot(1,4,4); plt.imshow(img4, cmap='gray'); plt.title('8 sample')

plt.tight_layout()
plt.show()
