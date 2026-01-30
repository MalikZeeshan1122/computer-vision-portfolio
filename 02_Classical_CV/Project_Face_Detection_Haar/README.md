# Project: Face Detection 😃

Before deep learning, Viola-Jones (Haar Cascades) was the standard for face detection. It's fast, light, and still used in digital cameras.

## How it works
1.  **Haar Features**: Simple rectangular features (black and white boxes) that act like filters.
2.  **Integral Image**: A trick to make calculating those features incredibly fast.
3.  **AdaBoost**: Selects the best features (e.g., eyes are darker than cheeks, bridge of nose is lighter than eyes).
4.  **Cascading**: A series of classifiers. If the first one says "no face", it discards the window immediately.

## 🛠️ The Project
Open `face_detection.py`.
1.  We will use Python's built-in webcam access (or a static image if you prefer).
2.  We load a pre-trained XML model included in OpenCV.
3.  We detect faces and draw rectangles around them.

**Note**: This requires a webcam. If you don't have one, you can change the input to `original.jpg`.
