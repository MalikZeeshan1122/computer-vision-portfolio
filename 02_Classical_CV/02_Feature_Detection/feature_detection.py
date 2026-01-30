import cv2
import numpy as np

def main():
    # 1. Load Image
    # We will use the 'original.jpg' created in the previous step.
    # Ensure you are running this from the root directory.
    image_path = '02_Classical_CV/01_Image_Transformations/original.jpg'
    
    # Try to load the image
    img = cv2.imread(image_path)
    
    # If image is not found, let's create a dummy one on the fly so the script doesn't crash
    if img is None:
        print(f"Could not load {image_path}. Creating a dummy image.")
        img = np.zeros((300, 300, 3), dtype=np.uint8)
        cv2.rectangle(img, (50, 50), (250, 250), (255, 255, 255), -1)
        cv2.rectangle(img, (100, 100), (200, 200), (0, 0, 255), -1)

    # Convert to grayscale (features are typically found in grayscale)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. Initialize Detector
    orb = cv2.ORB_create()

    # 3. Detect and Compute
    # find the keypoints with ORB
    kp = orb.detect(gray, None)
    
    # compute the descriptors with ORB
    kp, des = orb.compute(gray, kp)
    
    # 4. Draw Keypoints
    # draw only keypoints location,not size and orientation
    img_with_kp = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
    
    # Save/Show result
    cv2.imwrite('orb_features.jpg', img_with_kp)
    print(f"Saved orb_features.jpg. Detected {len(kp)} keypoints.")
    
    print("Implement ORB detection in the script!")

if __name__ == "__main__":
    main()
