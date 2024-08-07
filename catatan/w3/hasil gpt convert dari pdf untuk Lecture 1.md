# Feature Representation in Computer Vision

## What Are Image Features?

- **Definition**
  - Image features are vectors representing images in a compact form.
  - They capture important information present in an image.

- **Examples of Image Features**
  - Blobs, edges, corners, ridges, circles, ellipses, lines.

## Why Do We Need Image Features?

- Represent images as feature vectors for efficient and robust processing.
- Applications of image features include:
  - Object detection
  - Image segmentation
  - Image classification
  - Image retrieval
  - Image stitching
  - Object tracking

- **Limitations of Using Pixel Values Directly**
  - Pixel values vary with lighting, color, angle, and camera orientation.
  - They are often redundant.

## Desirable Properties of Features

- **Reproducibility (Robustness)**
  - Should be detectable at the same locations in different images despite changes in illumination and viewpoint.

- **Saliency (Descriptiveness)**
  - Similar salient points in different images should have similar features.

- **Compactness (Efficiency)**
  - Features should be few and small.

## Types of Image Features

- **Colour Features**
  - **Colour Histogram**
    - Represents the global distribution of pixel colors.
    - Construct histograms for each color channel (R, G, B) and concatenate.

  - **Colour Moments**
    - Represents color distributions using moments (mean, standard deviation, skewness).
    - Feature vector with fewer elements than color histograms.

- **Texture Features**
  - **Haralick Texture Features**
    - Statistical descriptors capturing spatial relationships between neighboring pixels.
    - Constructed using gray-level co-occurrence matrices (GLCMs).

  - **Local Binary Patterns (LBP)**
    - Describe local image texture structure.
    - Divide the image into cells and compare each pixel with neighbors to generate a binary pattern.
    - Can be multiresolution and rotation-invariant.

- **Shape Features**
  - **Basic Shape Features**
  - **Shape Context**
  - **Histogram of Oriented Gradients (HOG)**

## Prominent Feature Descriptors

- **Haralick Features**
  - Construct gray-level co-occurrence matrices.
  - Compute statistical descriptors such as contrast, correlation, energy, and homogeneity.

- **Local Binary Patterns (LBP)**
  - Capture spatial structure through binary patterns.
  - Histograms are constructed from binary patterns of image regions.

- **Scale-Invariant Feature Transform (SIFT)**
  - Describes texture in localized regions around keypoints.
  - Invariant to scale, rotation, affine distortion, and illumination changes.
  - SIFT Algorithm Steps:
    - Scale-Space Extrema Detection
    - Keypoint Localization
    - Orientation Assignment
    - Keypoint Descriptor

## Example Applications

- **Object Detection**
- **Image Segmentation**
- **Image Classification**
- **Image Retrieval**
- **Image Stitching**
- **Object Tracking**

## Descriptor Matching

- Using nearest neighbor distance ratio (NNDR).
- Reject matches with a ratio greater than 0.8.

## Fitting and Alignment

- **Least-Squares Fitting**
  - Estimate transformation parameters by minimizing squared errors.

- **RANdom SAmple Consensus (RANSAC)**
  - Iteratively fits models using random samples and evaluates inlier support.
  - Robust to outliers in data.

## Types of Spatial Transformation

- **Translation**
- **Rotation**
- **Scaling**
- **Affine Transformation**
- **Perspective Transformation**