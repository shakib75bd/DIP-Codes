import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Smoothning with Laplacian filter
lap = cv2.Laplacian(img, cv2.CV_64F)
imgL = cv2.convertScaleAbs(img+lap)
#plotting
plt.figure(figsize=(15,5))
plt.subplot(1,2,1); plt.imshow(img, cmap='gray'); plt.title('Original')
plt.subplot(1,2,2); plt.imshow(imgL, cmap='gray'); plt.title('Sharpened')
plt.tight_layout(); plt.show()
