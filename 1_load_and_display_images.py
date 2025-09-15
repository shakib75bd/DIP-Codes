"""Task: Load and Display Images"""
import cv2
import matplotlib.pyplot as plt
img_gray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('image.jpg')
plt.figure(figsize=(8,4))
plt.subplot(1,2,1); plt.imshow(img_gray, cmap='gray'); plt.title('Grayscale')
plt.subplot(1,2,2); plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)); plt.title('Color')

plt.show()
# Grayscale: 1 channel, Color: 3 channels (RGB). Grayscale shows intensity, color shows hues.
