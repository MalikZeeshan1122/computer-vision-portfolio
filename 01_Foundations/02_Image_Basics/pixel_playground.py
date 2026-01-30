import numpy as np
import matplotlib.pyplot as plt

def show_images(original, processed, title="Processed Image"):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(original, cmap='gray')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.title(title)
    plt.imshow(processed, cmap='gray')
    plt.axis('off')
    plt.show()

def create_synthetic_image():
    """
    Creates a simple 10x10 grayscale image with a white square in the middle.
    Returns: a numpy array of shape (10, 10)
    """
    # Create a 10x10 black image (zeros)
    img = np.zeros((10, 10), dtype=np.uint8)
    
    # Create a 4x4 white square in the center (rows 3-7, cols 3-7)
    img[3:7, 3:7] = 255
    
    return img

def apply_box_blur(image):
    """
    Applies a 3x3 box blur kernel to the image manually.
    """
    height, width = image.shape
    output = np.zeros((height, width), dtype=np.float32)
    
    # Simple 3x3 averaging kernel
    # [[1/9, 1/9, 1/9],
    #  [1/9, 1/9, 1/9],
    #  [1/9, 1/9, 1/9]]
    
    # TODO: Iterate over every pixel (excluding borders) and apply the filter
    # For each pixel (i, j), look at its neighbors, average them, and assign to output[i, j]
    
    for i in range(1, height - 1):
        for j in range(1, width - 1):
             # Extract the 3x3 region centered at (i, j)
             region = image[i-1:i+2, j-1:j+2]
             # Calculate the average
             average = np.mean(region)
             output[i, j] = average
             
    return output.astype(np.uint8)

if __name__ == "__main__":
    # 1. Create Image
    img = create_synthetic_image()
    print("Image Created:\n", img)
    
    # 2. Apply Blur
    blurred = apply_box_blur(img)
    print("\nBlurred Image:\n", blurred)
    
    # Visualization (will simplify logging if in non-GUI env)
    # show_images(img, blurred, "Box Blur")
