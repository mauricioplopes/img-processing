
# Digital Image Processing - MO443 - Assignment 01

This repository contains the implementation of Assignment 01 for the course **MO443 – Introduction to Digital Image Processing** at the **Institute of Computing, University of Campinas (Unicamp)**.

[Code](trabalho1.ipynb)

Author: **Maurício Pereira Lopes**  
RA: 225242  
Semester: 1st Semester of 2023  
Instructor: Prof. Hélio Pedrini

## 📌 Project Overview

The purpose of this assignment was to implement basic operations in digital image processing using Python. The project consists of **eight independent tasks**, each addressing different image processing concepts. The solutions were implemented without using specialized image processing libraries, relying solely on **NumPy**, **ImageIO**, **Matplotlib**, and basic Python operations.

## 📁 Project Structure

The repository contains:
- Eight Python scripts, one for each question (`trabalho01-questaoX.py`, where X = 1.1 to 1.8).
- A Jupyter Notebook file (`trabalho01.ipynb`) that includes all the implementations for easier experimentation and visualization.
- Output images in `.png` format for each question, automatically generated upon running the scripts.

## ⚙️ Requirements

Before running the scripts, ensure you have the following Python packages installed:

```bash
pip install numpy imageio matplotlib
```

Also, an **internet connection is required** to download the input images via URLs embedded in the scripts.

## 🚀 How to Run

Each script can be executed individually from the command line:

```bash
python trabalho01-questaoX.py
```

- The script will display the result in a window and also save the output as a `.png` image file.
- The Jupyter Notebook can be opened and run with `jupyter notebook trabalho01.ipynb`.

## 📷 Tasks Summary

### 1. Mosaics
Reorders 16 image blocks randomly to create a shuffled mosaic of a grayscale image.

### 2. Image Combination
Performs weighted averaging between two grayscale images using different weight pairs.

### 3. Intensity Transformations
Applies various operations on a grayscale image:
- Negative transformation
- Contrast reduction
- Line-based and symmetric transformations

### 4. RGB to Grayscale and Sepia
- Converts an RGB image into sepia tones using channel transformations.
- Converts to grayscale using weighted channel averages.

### 5. Gamma Correction
Applies gamma correction with different gamma values to adjust brightness.

### 6. Quantization
Reduces the number of grayscale levels to simulate lower bit-depth representations.

### 7. Bit Planes
Extracts and visualizes all 8 bit planes from a grayscale image.

### 8. Image Filtering
Applies various 2D filters (high-pass, low-pass, Sobel, identity, etc.) via manually implemented convolution without specialized libraries.

## 🔍 Notes and Observations

- All image transformations are manually implemented using array slicing and operations in NumPy.
- For filtering (Task 8), a custom convolution function (`filtrar`) was implemented, including image padding using reflection to preserve border characteristics.
- Most filters provided acceptable results, but high-pass filters showed lower contrast—potential area for future improvement.

## 📘 Conclusion

This project reinforced core concepts of digital image processing and provided practical experience with image manipulation techniques. Avoiding high-level libraries challenged the understanding and manual implementation of core algorithms such as reshaping, slicing, and filtering through convolution.

---

Feel free to explore the code, run the notebooks, and test your own modifications or enhancements to the algorithms!
