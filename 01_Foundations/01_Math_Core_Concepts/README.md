# Math & Core Concepts for Computer Vision

## 1. Linear Algebra
Linear algebra is the language of computer vision. Images are matrices, and operations on them (like rotation, scaling, and filtering) are linear transformations.

### Key Concepts
- **Vectors**: Direction and magnitude (e.g., motion vectors, gradients).
- **Matrices**: 2D arrays (images), transformations (homography).
- **Eigenvalues/Eigenvectors**: Principal Component Analysis (PCA), face recognition (Eigenfaces).

### Resources
- [3Blue1Brown - Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) (Highly Recommended for intuition)
- [Immersive Linear Algebra](http://immersivemath.com/ila/index.html)

## 2. Probability & Statistics
Understanding uncertainty is crucial. Sensors are noisy, and models are probabilistic.

### Key Concepts
- **Probability Distributions**: Gaussian (Normal) distribution is used everywhere (e.g., Kalman Filters).
- **Maximum Likelihood Estimation (MLE)**: How we fit models to data.
- **Bayes' Theorem**: Updating beliefs with new evidence (e.g., tracking).

## 3. Optimization
How do we train models? By minimizing error.

### Key Concepts
- **Gradient Descent**: The engine of deep learning.
- **Loss Functions**: MSE (Mean Squared Error), Cross-Entropy.

---

## 🛠️ Practical Exercise: Linear Algebra from Scratch
To truly understand, build it yourself.

**Goal**: Implement basic matrix operations without `numpy` first, then verify with `numpy`.

Open `linear_algebra_basics.py` and implement the TODOs.
