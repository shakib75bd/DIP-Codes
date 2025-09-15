#4-neighbours and 8-neighbours in image
import cv2
img=cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

x = img.shape[0]//2
y = img.shape[1]//2

val = img[x,y]

#four neighbour
four = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
eight = four + [(x-1,y-1), (x+1,y+1),(x+1,y-1),(x-1,y+1)]

print('4 neighbours: ', four)
print('8 neighbours: ', eight)
