<div align="center">
   <h1>🖼️ Image Processing with OpenCV Python</h1>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
    <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  </p>

  <p>
    <strong>Implementation of fundamental digital image processing techniques using OpenCV</strong><br />
  </p>

  <p>
    <img src="https://img.shields.io/badge/Status-Active-success" />
    <img src="https://img.shields.io/badge/Version-1.0.0-blue" />
  </p>
</div>

---

## 🌟 Overview

> A collection of Python scripts for digital image processing, focusing on **background subtraction**, **image denoising**, and **histogram equalization**

This project implements three fundamental image processing techniques using the **OpenCV** and **NumPy** libraries. Each task covers one processing technique in a chained pipeline — the output of one task serves as the input for the next.

---

## ✨ Key Features

### 🔹 Core Functionality
- 🔍 **Background Subtraction** (Task 1) — Separates objects from the background
- 🔇 **Image Denoising via Averaging** (Task 2) — Reduces noise by averaging multiple frames
- 🌗 **Histogram Equalization** (Task 3) — Enhances contrast on dark images

### 🔹 Technical Highlights
- 🎯 **Pixel-wise Arithmetic** using NumPy arrays
- 🔒 **Safe Clipping** to prevent pixel value overflow
- 🖼️ **Multi-image Accumulation** for noise averaging
- 📊 **Histogram Redistribution** for contrast enhancement
- 🔄 **Chained Processing Pipeline** — output of one task feeds into the next

---

## 📋 Table of Contents
1. [Prerequisites](#-1-prerequisites)
2. [Installation](#-2-installation)
3. [Project Structure](#-3-project-structure)
4. [Script Breakdown](#-4-script-breakdown)
5. [Running the Scripts](#-5-running-the-scripts)
6. [Processing Flow](#-6-processing-flow)
7. [Output Results](#-7-output-results)
8. [Troubleshooting](#️-8-troubleshooting)
9. [Closing](#-9-closing)

---

## 🔧 1. Prerequisites

Make sure your development environment meets the following requirements:
- **Python** >= 3.8
- **pip** (Python package manager)
- **OpenCV** (`cv2`)
- **NumPy**

---

## 📦 2. Installation

Clone the repository and install all dependencies:

```bash
git clone <repository-url>
cd <folder-name>
pip install opencv-python numpy
```

---

## 📁 3. Project Structure

```
project/
├── src/
│   ├── background_subtraction.py    # Task 1 - Background subtraction
│   ├── denoising_averaging.py       # Task 2 - Image denoising via averaging
│   └── histogram_equalization.py    # Task 3 - Histogram equalization
├── img/
│   ├── image_soal1/
│   │   ├── no_object.jpeg           # Background image without object
│   │   └── with_object.jpeg         # Image containing the object
│   ├── image_soal2/
│   │   └── *.jpg                    # Multiple noisy photos for averaging
│   ├── hasil_soal1/                 # Task 1 output
│   ├── hasil_soal2/                 # Task 2 output
│   └── hasil_soal3/                 # Task 3 output
└── README.md
```

### Architecture Layer Explanation

1. **src/** → Processing scripts per task
2. **img/image_soalX/** → Input images per task
3. **img/hasil_soalX/** → Output images per task

---

## 🔬 4. Script Breakdown

### Task 1 — Background Subtraction (`background_subtraction.py`)

Separates an object from its background by subtracting the background image from the image containing the object.

**Techniques used:**
- Convert both images to **grayscale**
- **Pixel subtraction**: `with_object - no_object`
- `np.clip(0, 255)` to prevent negative wrap-around
- Resize images to the same dimensions before processing

```python
diff = np.clip(obj_gray.astype(np.int16) - bg_gray.astype(np.int16), 0, 255).astype(np.uint8)
```

**Output files:**

| File | Description |
|------|-------------|
| `soal1_before.jpg` | Background image in grayscale |
| `soal1_after.jpg` | Object image in grayscale |
| `soal1_diff.jpg` | Subtraction result (object = white, background = black) |

---

### Task 2 — Denoising via Averaging (`denoising_averaging.py`)

Reduces image noise by averaging pixel values across multiple photos taken under the same conditions.

**Techniques used:**
- Collect all image paths using `glob`
- Pixel accumulation using **float64** to avoid overflow
- Divide accumulated sum by number of images to get the average
- Resize each photo to match the reference size before summing

```python
acc = np.zeros((height, width, 3), dtype=np.float64)
for p in paths:
    acc += cv2.resize(cv2.imread(p), (width, height)).astype(np.float64)
averaged = (acc / len(paths)).astype(np.uint8)
```

**Output files:**

| File | Description |
|------|-------------|
| `soal2_before.jpg` | One raw noisy photo |
| `soal2_averaged.jpg` | Result after averaging (reduced noise) |

---

### Task 3 — Histogram Equalization (`histogram_equalization.py`)

Enhances contrast on a dark image by redistributing the intensity histogram evenly across the full range.

**Techniques used:**
- Uses the averaged output from Task 2 as input
- Convert to **grayscale** (histogram equalization works on a single intensity channel)
- Apply `cv2.equalizeHist()` for histogram redistribution

```python
gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hasil = cv2.equalizeHist(gray)
```

**Output files:**

| File | Description |
|------|-------------|
| `soal3_before.jpg` | Grayscale image before equalization (dark) |
| `soal3_after.jpg` | Image after equalization (contrast enhanced) |

---

## 🚀 5. Running the Scripts

Run each script in order from the project root folder:

```bash
# Task 1 - Background Subtraction
python src/background_subtraction.py

# Task 2 - Denoising Averaging
python src/denoising_averaging.py

# Task 3 - Histogram Equalization
python src/histogram_equalization.py
```

> ⚠️ **Important**: Run the scripts in order! Task 3 depends on the output of Task 2.

---

## 🔄 6. Processing Flow

```
[no_object.jpeg]   ─┐
                     ├─→ Background Subtraction ──→ [soal1_diff.jpg]
[with_object.jpeg] ─┘

[noisy_photos/*.jpg] ──→ Averaging ──→ [soal2_averaged.jpg]
                                                │
                                                ↓
                                 Histogram Equalization
                                                │
                                                ↓
                                      [soal3_after.jpg]
```

**Key notes:**
- Task 1 and Task 2 run **independently** (different inputs)
- Task 3 **depends** on Task 2's output (`soal2_averaged.jpg`)
- Make sure all `hasil_soalX/` folders exist before running the scripts

---

## 📊 7. Output Results

### Expected Results

**Task 1 (Background Subtraction):**
- `soal1_diff.jpg` → Image where the object area appears white/bright and the background is black

**Task 2 (Denoising):**
- `soal2_averaged.jpg` → Smoother, cleaner image compared to `soal2_before.jpg`

**Task 3 (Histogram Equalization):**
- `soal3_after.jpg` → Brighter image with improved contrast compared to `soal3_before.jpg`

---

## 🛠️ 8. Troubleshooting

### Problem: `ModuleNotFoundError: No module named 'cv2'`

**Solution:**
```bash
pip install opencv-python
```

---

### Problem: `error: (-215:Assertion failed) !_src.empty()`

Image could not be read — path is wrong or the file does not exist.

**Solution:**
```bash
# Verify the folder structure is correct
ls img/image_soal1/
ls img/image_soal2/

# Confirm that filenames match what is referenced in the script
```

---

### Problem: `FileNotFoundError` when saving results

Output folders have not been created yet.

**Solution:**
```bash
# Create output folders manually
mkdir -p img/hasil_soal1
mkdir -p img/hasil_soal2
mkdir -p img/hasil_soal3
```

---

### Problem: `soal2_averaged.jpg` not found when running Task 3

Task 2 script has not been run yet.

**Solution:**
```bash
# Run Task 2 first
python src/denoising_averaging.py

# Then run Task 3
python src/histogram_equalization.py
```

---

### Problem: `Found 0 photos` in Task 2

No `.jpg` files found in the `img/image_soal2/` folder.

**Solution:**
```bash
# Verify that photos exist in the correct folder
ls img/image_soal2/*.jpg
```

---

## 📧 9. Closing

This project implements three interconnected image processing techniques — from object extraction and noise reduction to contrast enhancement. The pipeline reflects a common preprocessing workflow used in computer vision and digital image analysis.

---
