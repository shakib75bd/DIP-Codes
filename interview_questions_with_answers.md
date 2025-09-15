# Digital Image Processing Interview Questions & Answers

This document contains common interview questions and concise answers based on the fundamental image processing tasks covered in this repository.

## 0. Libraries and Functions

**Q:** What is OpenCV (`cv2`)?
**A:** OpenCV is an open-source computer vision and image processing library. The `cv2` module is its Python interface, used for reading, manipulating, and analyzing images and videos.

**Q:** What is matplotlib and why is it used here?
**A:** Matplotlib is a Python plotting library. It is used to visualize images and data (e.g., histograms) in these scripts.

**Q:** What does `cv2.imread()` do?
**A:** It reads an image from a file. The second argument specifies the mode: `cv2.IMREAD_GRAYSCALE` loads as grayscale, default loads as color (BGR).

**Q:** What does `cv2.equalizeHist()` do?
**A:** It applies histogram equalization to a grayscale image, enhancing its contrast.

**Q:** What does `cv2.blur()` do?
**A:** It applies an averaging (mean) filter to smooth or blur an image.

**Q:** What does `cv2.Laplacian()` do?
**A:** It applies the Laplacian operator to an image, highlighting edges by calculating the second derivative.

**Q:** What does `cv2.add()` do?
**A:** It adds two images or arrays element-wise, handling overflow safely for image data.

**Q:** What does `plt.imshow()` do?
**A:** It displays an image in a matplotlib plot window.

**Q:** What does `plt.hist()` do?
**A:** It plots a histogram of pixel intensities from an image.

**Q:** What does `np.fft.fft2()` do?
**A:** It computes the 2D Fast Fourier Transform of an image, converting it to the frequency domain.

**Q:** What does `np.fft.fftshift()` do?
**A:** It shifts the zero-frequency component to the center of the spectrum for visualization.

**Q:** What does `np.tile()` do?
**A:** It repeats an array to create a new array of a specified shape, useful for creating patterns like synthetic noise.

**Q:** What does slicing like `img[::2, ::2]` do?
**A:** It subsamples the image by taking every 2nd pixel in both dimensions, reducing resolution.

**Q:** What does the function `bit_p(img, x)` do in bit-plane slicing?
**A:** It extracts the x-th bit-plane from the image using bitwise operations.

**Q:** What does the function `img_gr_q(img, x)` do in quantization?
**A:** It quantizes the image to x gray levels by scaling and rounding pixel values.

## 1. Image Types and Display

**Q:** What is the difference between a grayscale and a color image?
**A:** Grayscale images have one channel representing intensity; color images have three channels (typically RGB) representing color information.

**Q:** How many channels does a grayscale image have? What about a color image?
**A:** Grayscale: 1 channel; Color: 3 channels (Red, Green, Blue).

**Q:** How do you load and display images using OpenCV and matplotlib?
**A:** Use `cv2.imread()` to load, and `matplotlib.pyplot.imshow()` to display. Convert BGR to RGB for color images before displaying.

## 2. Negative of an Image

**Q:** How do you generate the negative of a grayscale image?
**A:** Subtract each pixel value from 255: `negative = 255 - image`.

**Q:** What effect does a negative image have on visual perception?
**A:** It inverts brightness, making dark areas light and vice versa, revealing hidden details.

**Q:** Why is 255 used in the formula for image negation?
**A:** 255 is the maximum intensity for 8-bit images; subtracting from 255 inverts the pixel value.

## 3. Image Subsampling

**Q:** What is image subsampling and why is it used?
**A:** Subsampling reduces image resolution by selecting every Nth pixel, used for compression or analysis at lower detail.

**Q:** How does subsampling affect image resolution and details?
**A:** It decreases resolution and removes fine details, making the image blockier.

**Q:** How can you downsample an image by a factor of N in Python?
**A:** Use slicing: `downsampled = image[::N, ::N]`.

## 4. Gray-Level Quantization

**Q:** What is gray-level quantization?
**A:** Reducing the number of possible intensity values in an image.

**Q:** How does reducing the number of gray levels affect image quality?
**A:** Fewer levels cause visible banding and loss of detail.

**Q:** How do you implement quantization in code?
**A:** Divide pixel values by a factor, then multiply to scale: `(image // (256//levels)) * (255//(levels-1))`.

## 5. Bit-Plane Slicing

**Q:** What is bit-plane slicing in image processing?
**A:** Separating an image into its binary bit layers to analyze information at each bit position.

**Q:** Which bit-planes contain most of the image information?
**A:** The most significant bit-planes (higher bits) contain most structural information; lower bits contain fine details/noise.

**Q:** How do you extract and visualize bit-planes in Python?
**A:** Use bitwise operations: `(image >> n) & 1` for bit-plane n; display with `imshow()`.

## 6. Pixel Neighborhood Analysis

**Q:** What are 4-neighbors and 8-neighbors of a pixel?
**A:** 4-neighbors: top, bottom, left, right; 8-neighbors: 4-neighbors plus diagonals.

**Q:** Why are pixel neighborhoods important in filtering and edge detection?
**A:** They define local regions for operations like smoothing, sharpening, and edge detection.

**Q:** How do you find the neighbors of a pixel in code?
**A:** For pixel (x, y): 4-neighbors are (x±1, y), (x, y±1); 8-neighbors add (x±1, y±1).

## 7. Histogram and Histogram Equalization

**Q:** What is a histogram in the context of images?
**A:** A plot showing the frequency of each intensity value in an image.

**Q:** How does histogram equalization improve image contrast?
**A:** It redistributes pixel intensities to span the full range, enhancing contrast.

**Q:** How do you plot and equalize a histogram using OpenCV?
**A:** Use `plt.hist(image.ravel(), 256)` to plot; `cv2.equalizeHist(image)` to equalize.

## 8. Contrast Stretching

**Q:** What is contrast stretching?
**A:** Expanding the range of pixel intensities to improve image contrast.

**Q:** How does it affect pixel intensities and image appearance?
**A:** It spreads out intensities, making features more visible.

**Q:** How do you perform linear contrast stretching in Python?
**A:** `stretched = ((image - minV) * 255 / (maxV - minV)).astype('uint8')`.

## 9. Smoothing with Spatial Filters

**Q:** What is the purpose of smoothing (blurring) an image?
**A:** To reduce noise and minor details, making the image smoother.

**Q:** How does kernel size affect the amount of blurring?
**A:** Larger kernels produce more blurring.

**Q:** How do you apply an averaging filter in OpenCV?
**A:** Use `cv2.blur(image, (k, k))` where k is kernel size.

## 10. Sharpening with Laplacian Filter

**Q:** What is the Laplacian filter and how does it work?
**A:** It highlights regions of rapid intensity change (edges) by computing the second derivative.

**Q:** How does sharpening affect image features?
**A:** It enhances edges and fine details, making features more distinct.

**Q:** How do you apply a Laplacian filter in code?
**A:** Use `cv2.Laplacian(image, cv2.CV_64F)`.

## 11. Fourier Transform and Spectrum Visualization

**Q:** What is the 2D Fourier Transform of an image?
**A:** It converts the image from spatial to frequency domain, representing frequency components.

**Q:** What do low and high-frequency components represent?
**A:** Low-frequency: smooth regions; high-frequency: edges and fine details.

**Q:** How do you visualize the magnitude spectrum in Python?
**A:** Use `np.fft.fft2()`, `np.fft.fftshift()`, and plot `20*np.log(np.abs(fshift)+1)`.

## 12. Frequency Domain Filtering

**Q:** What is the difference between low-pass and high-pass filtering?
**A:** Low-pass removes high frequencies (blurs image); high-pass removes low frequencies (enhances edges).

**Q:** How do these filters affect image appearance?
**A:** Low-pass: smoother, less detail; high-pass: sharper, more detail.

**Q:** How do you design and apply ideal filters in the frequency domain?
**A:** Create a mask (circle for low-pass, ring for high-pass), multiply with shifted FFT, then inverse FFT.

## 13. Notch Filtering for Periodic Noise Removal

**Q:** What is periodic noise in images?
**A:** Repetitive patterns caused by interference, often appearing as stripes or waves.

**Q:** How does a notch filter work to remove specific frequencies?
**A:** It zeros out specific frequency components in the spectrum to remove unwanted patterns.

**Q:** How do you add synthetic noise and apply a notch filter in code?
**A:** Add a sinusoidal pattern to the image, create a mask to block noise frequencies, and apply in frequency domain.

---

These answers cover both conceptual and practical aspects of digital image processing, suitable for interviews or exam preparation.
