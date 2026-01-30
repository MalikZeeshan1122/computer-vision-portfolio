# Feature Detection

To understand images, we need to find "features"—points of interest that are distinct and trackable.

## Key Concepts
1.  **Corners (Harris Corner Detection)**:
    - Points where intensity changes in all directions. Good for simple structures.
2.  **SIFT (Scale-Invariant Feature Transform)**:
    - **Pros**: Very accurate, scale & rotation invariant.
    - **Cons**: Patented (historically), slower.
3.  **SURF (Speeded-Up Robust Features)**:
    - Faster than SIFT, but also patented (historically).
4.  **ORB (Oriented FAST and Rotated BRIEF)**:
    - **Pros**: Fast, free (open source), good for real-time.
    - **Cons**: Less robust to scale precision than SIFT.

In this module, we will focus on **ORB** because it is efficient and free to use in OpenCV.

## 🛠️ Practical Exercise: Finding Keypoints
Open `feature_detection.py` to:
1. Load the `original.jpg` image.
2. Initialize the ORB detector.
3. "Detect" keypoints and "Compute" descriptors.
4. Visualize the keypoints on the image.
