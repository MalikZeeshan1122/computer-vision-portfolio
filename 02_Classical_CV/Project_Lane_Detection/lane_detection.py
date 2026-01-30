import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_synthetic_road_image():
    """Created a dummy road image with white lane lines."""
    height, width = 540, 960
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Gray road
    cv2.rectangle(img, (0, height//2), (width, height), (100, 100, 100), -1)
    
    # Left Lane (White line)
    cv2.line(img, (width//2 - 100, height//2), (100, height), (255, 255, 255), 10)
    
    # Right Lane (White line)
    cv2.line(img, (width//2 + 100, height//2), (width - 100, height), (255, 255, 255), 10)
    
    return img

def region_of_interest(img):
    """
    Applies an image mask.
    Only keeps the region of the image defined by the polygon
    formed by `vertices`. The rest of the image is set to black.
    """
    height, width = img.shape
    mask = np.zeros_like(img)
    
    # Define a triangular polygon for the road area
    # Bottom-left, Bottom-right, Top-center
    triangle = np.array([
        [(0, height), (width, height), (width // 2, height // 2)]
    ])
    
    cv2.fillPoly(mask, triangle, 255)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def detect_lanes(image):
    # 1. Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 2. Gaussian Blur (kernel size 5)
    # TODO: Apply Gaussian Blur
    # blur = ...
    blur = cv2.GaussianBlur(gray, (5, 5), 0) # Placeholder
    
    # 3. Canny Edge Detection (low_threshold=50, high_threshold=150)
    # TODO: Apply Canny Edge Detection
    # edges = ...
    edges = cv2.Canny(blur, 50, 150) # Placeholder
    
    # 4. Region of Interest
    roi_edges = region_of_interest(edges)
    
    # 5. Hough Transform
    # Lines will be a list of [[x1, y1, x2, y2]]
    # TODO: specific parameters for HoughLinesP
    lines = cv2.HoughLinesP(roi_edges, 1, np.pi/180, 50, minLineLength=50, maxLineGap=100)
    
    # 6. Draw lines on a copy of the original image
    line_image = np.copy(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
            
    return line_image, edges

def main():
    # 1. Generate Image
    image = create_synthetic_road_image()
    
    # 2. Detect Lanes
    result, edges = detect_lanes(image)
    
    # 3. Save Results
    cv2.imwrite('road_original.jpg', image)
    cv2.imwrite('road_edges.jpg', edges)
    cv2.imwrite('road_lanes.jpg', result)
    
    print("Lane Detection verification complete!")
    print("Files saved: road_original.jpg, road_edges.jpg, road_lanes.jpg")

if __name__ == "__main__":
    main()
