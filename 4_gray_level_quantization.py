import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

def img_gr_q(img,x):
	return img//(256//x)*(255//(x-1))

plt.figure(figsize=(20,5))
plt.title('Gray-Level Quantization (2,4,8,16,256)')
plt.subplot(1,5,1); plt.imshow(img_gr_q(img,2), cmap='gray');plt.title('2')
plt.subplot(1,5,2); plt.imshow(img_gr_q(img,4), cmap='gray');plt.title('4')
plt.subplot(1,5,3); plt.imshow(img_gr_q(img,8), cmap='gray');plt.title('8')
plt.subplot(1,5,4); plt.imshow(img_gr_q(img,16), cmap='gray');plt.title('16')
plt.subplot(1,5,5); plt.imshow(img_gr_q(img,256), cmap='gray');plt.title('256')

plt.tight_layout()
plt.show()
