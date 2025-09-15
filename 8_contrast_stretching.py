import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

#contrast streching
minV = img.min()
maxV = img.max()
stretched = ((img-minV)*255/(maxV-minV)).astype('uint8')

#plotting
plt.figure(figsize=(10,4))
plt.subplot(1,2,1); plt.imshow(img, cmap='gray');plt.title('Original')
plt.subplot(1,2,2); plt.imshow(stretched, cmap='gray');plt.title('Streched')
plt.tight_layout(); plt.show()
