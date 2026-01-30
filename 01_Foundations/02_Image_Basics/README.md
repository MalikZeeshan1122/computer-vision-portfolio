# Image Basics

Before using high-level libraries, you must understand what an image actually *is*.

## 1. Pixels & Channels
An image is just a grid of numbers.
- **Grayscale**: 2D array (Height x Width). Values 0 (black) to 255 (white).
- **Color (RGB)**: 3D array (Height x Width x 3). Channels: Red, Green, Blue.
- **HSV**: Hue, Saturation, Value. Often better for color-based tracking than RGB.

## 2. Convolutions & Kernels
The most important operation in Computer Vision.
- **Kernel**: A small matrix (e.g., 3x3) that slides over the image.
- **Convolution**: The process of multiplying the kernel with the underlying image patch and summing the result.
- **Why?** This is how we detect edges, blur images, and sharpen details. It's the building block of CNNs.

## 3. Filters
- **Gaussian Blur**: Smooths noise.
- **Sobel**: Detects edges (changes in intensity).
- **Median**: Removes "salt and pepper" noise.

---

## 🛠️ Practical Exercise: Pixel Manipulation & Convolution
Open `pixel_playground.py` to:
1. Create an image from scratch using NumPy.
2. Manipulate individual pixels.
3. Implement a simple "Box Blur" convolution manually.
