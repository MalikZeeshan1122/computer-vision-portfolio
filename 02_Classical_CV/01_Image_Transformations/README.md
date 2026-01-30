# Image Transformations

Transformations are fundamental for data augmentation, geometric correction, and aligning images.

## 1. Geometric Transformations
- **Scaling (Resize)**: Changing image dimensions.
- **Translation**: Shifting image (x, y).
- **Rotation**: Rotating around a point.
- **Affine Transformation**: Preserves parallelism (e.g., rotation, scale, translation, shear).
- **Perspective Transformation**: Changing the viewpoint (homography).

## 2. Interpolation
When resizing, we need to estimate pixel values at new locations.
- **Nearest Neighbor**: Fast, blocky.
- **Bilinear**: Smooth, standard.
- **Bicubic**: Smoother, slower.

## 🛠️ Practical Exercise: Manipulate an Image
Open `basic_transforms.py` to:
1. Load an image.
2. Resize it (upscale and downscale).
3. Rotate it by 45 degrees.
4. Flip it horizontally.
