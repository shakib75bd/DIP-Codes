"""Task: Pixel Neighborhood Analysis"""
import cv2
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
x, y = img.shape[0]//2, img.shape[1]//2
val = img[x, y]
four = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
eight = four + [(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]
print(f"Pixel ({x},{y}) value: {val}")
print("4-neighbors:", four)
print("8-neighbors:", eight)
# Neighborhoods are key for filtering and edge detection.
