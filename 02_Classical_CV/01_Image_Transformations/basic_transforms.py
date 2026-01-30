import cv2
import numpy as np

def show_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # 1. Create a dummy image (black background with a white rectangle)
    # We use a dummy image so you don't need to download one.
    image = np.zeros((300, 300, 3), dtype=np.uint8)
    cv2.rectangle(image, (50, 50), (250, 250), (255, 255, 255), -1) # White filled square
    cv2.rectangle(image, (100, 100), (200, 200), (0, 0, 255), -1)   # Red filled square
    
    # Save the original for reference
    cv2.imwrite("original.jpg", image)
    print("Original image created.")

    # 2. Resize
    # Resize to half size
    height, width = image.shape[:2]
    new_dim = (width // 2, height // 2)
    resized = cv2.resize(image, new_dim, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite("resized.jpg", resized)
    print(f"Resized image saved. New shape: {resized.shape}")
    
    # 3. Rotate
    # Rotate 45 degrees around center
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(image, rotation_matrix, (width, height))
    cv2.imwrite("rotated.jpg", rotated)
    print("Rotated image saved.")

    # 4. Flip
    # Flip horizontally (1 for horizontal, 0 for vertical, -1 for both)
    flipped = cv2.flip(image, 1)
    cv2.imwrite("flipped.jpg", flipped)
    print("Flipped image saved.")
    
    print("Implement the transformations in the script!")

if __name__ == "__main__":
    main()
