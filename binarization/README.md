# Image Binarization Techniques - MO443 Assignment 2

This repository contains the implementation and analysis for the second assignment of the course *Introduction to Digital Image Processing (MO443)* at the University of Campinas (UNICAMP), under Professor Hélio Pedrini.

**Author**: Maurício Pereira Lopes  
**RA**: 225242  
**Date**: May 5th, 2023

## 📄 Overview

[Code](trabalho_2.ipynb)

The goal of this assignment was to explore and implement both global and local thresholding methods for binarization of grayscale images. Each pixel is classified as either foreground (black) or background (white) depending on whether its value is above or below a computed threshold.

## 🧪 Techniques Implemented

Nine binarization methods were implemented and analyzed using Python, mostly from scratch, with vectorized alternatives tested when applicable:

1. **Global Thresholding**
2. **Otsu’s Method** (using OpenCV)
3. **Bernsen Method**
4. **Niblack Method**
5. **Sauvola and Pietaksinen Method**
6. **Phansalskar, More and Sabale Method**
7. **Local Contrast Method**
8. **Local Mean Method**
9. **Local Median Method**

## 📂 Repository Contents

```plaintext
📁 data/
    Grayscale image files used in the experiments.
📄 codigo-trabalho2-1S2023-RA225242.ipynb
    Jupyter Notebook containing all implementations, charts, and results.
📄 relatorio-trabalho2-1S2023-RA225242.pdf
    The original report with detailed explanations and experiment results.
```

## ⚙️ Dependencies

To run the code, you’ll need the following Python libraries:

- `numpy >= 1.20` (for `sliding_window_view`)
- `opencv-python`
- `matplotlib`
- `os`
- `time`

All images used are grayscale and located in the `data/` subdirectory.

## 💡 Highlights

- Most methods were implemented manually for educational purposes.
- Vectorized implementations using `numpy.lib.stride_tricks.sliding_window_view` greatly improved performance in some cases.
- A wide variety of images were tested, including high contrast photos and noisy fingerprint images.
- Detailed analysis of parameter sensitivity (kernel size `n`, constant `k`, etc.) was performed for each method.

## 🧠 Results Summary

- **Global methods** worked well for high-contrast images (e.g., `plutao.jpg`, `saturn.jpg`) but struggled with shadowed or low-contrast regions.
- **Local methods** offered better segmentation overall, though performance depended heavily on parameter tuning.
- **Phansalskar’s method** provided the most robust results across different image types.
- **Local mean thresholding** provided a good balance between speed and accuracy.

## 🚀 Future Improvements

- Enhance vectorized implementations to reduce execution time.
- Perform a broader grid search for parameter optimization.
- Investigate discrepancies observed when using vectorized Bernsen thresholding.

---

Feel free to explore the Jupyter Notebook for visual results, code logic, and further insights into each method.
