# Computer Vision Portfolio 👁️

Reference implementations and projects tracking my journey from Computer Vision foundations to Advanced Deep Learning.

## 📂 Repository Structure

### [01_Foundations](./01_Foundations)
Core mathematical and image processing concepts.
- **Math & Core Concepts**: Linear Algebra (Vectors, Matrices) from scratch.
- **Image Basics**: Pixel manipulation, Convolutions, and building filters manually.

### [02_Classical_CV](./02_Classical_CV)
Traditional Computer Vision techniques using OpenCV.
- **Image Transformations**: Resizing, Rotation, Affine transforms.
- **Feature Detection**: Detecting keypoints using ORB (Oriented FAST and Rotated BRIEF).
- **Projects**:
    - 🛣️ **[Lane Detection](./02_Classical_CV/Project_Lane_Detection)**: Detecting road lanes using Canny Edge Detection and Hough Transforms.
    - 😃 **[Face Detection](./02_Classical_CV/Project_Face_Detection_Haar)**: Real-time face detection using Haar Cascades.

### [03_Deep_Learning_CV](./03_Deep_Learning_CV) *(Coming Soon)*
Modern Deep Learning approaches.
- CNNs (ResNet, VGG)
- Object Detection (YOLO)
- Segmentation (U-Net)

### 04 - 07 *(Planned)*
- **Advanced CV**: 3D Vision, SLAM.
- **Deployment**: ONNX, Edge devices.
- **Projects & Research**: End-to-end applications.

---

## 🚀 Getting Started

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/MalikZeeshan1122/computer-vision-portfolio.git
    cd computer-vision-portfolio
    ```

2.  **Install Dependencies**:
    ```bash
    pip install opencv-python numpy matplotlib
    ```

3.  **Run a Project**:
    *Lane Detection*:
    ```bash
    python 02_Classical_CV/Project_Lane_Detection/lane_detection.py
    ```
    *Face Detection*:
    ```bash
    python 02_Classical_CV/Project_Face_Detection_Haar/face_detection.py
    ```

## 🛠️ Tech Stack
- **Languages**: Python
- **Libraries**: OpenCV, NumPy, Matplotlib
- **Planned**: PyTorch, Ultralytics (YOLO)

---
*Created as part of a 90-day Computer Vision Learning Path.*
