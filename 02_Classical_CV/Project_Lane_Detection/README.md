# Project: Lane Detection System 🛣️

This is a classic "Hello World" project for self-driving cars. The goal is to identify lane lines on the road.

## The Pipeline
1.  **Color Selection**: Filter the image to keep only yellow and white pixels (the color of lane lines).
2.  **Grayscale**: Convert to grayscale for edge detection.
3.  **Gaussian Blur**: Smooth the image to reduce noise and spurious edges.
4.  **Canny Edge Detection**: Find the edges in the image.
5.  **Region of Interest (ROI)**: Mask out everything except the road (we don't care about the sky).
6.  **Hough Transform**: Find lines (series of points) from the edge pixels.

## 🛠️ The Project
Open `lane_detection.py`. It includes a helper to generate a **synthetic road image** so you don't need to download a dataset yet.

### Your Goal
Implement the pipeline steps in the `detect_lanes` function.
