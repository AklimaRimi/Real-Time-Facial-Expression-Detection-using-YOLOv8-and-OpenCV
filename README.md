# Real-Time Facial Expression Detection using YOLOv8 and OpenCV

![](https://img.shields.io/badge/Status-Completed-brightgreen)

This project uses a custom-built facial expression dataset and YOLOv8 to detect and classify human emotions in real-time from video streams. With over 70,000 labeled images across 9 emotional classes, the model is trained and evaluated to perform with high accuracy and speed using OpenCV.

---

## 📦 Dataset Overview

The **Facial Expression Recognition - 9 Emotions Dataset** was carefully **compiled and annotated** using multiple publicly available datasets from **Roboflow Universe**. It was curated to support emotion recognition tasks in deep learning and human-computer interaction.

### 📊 Key Statistics
- **Total Images**: 70,000+
- **Image Format**: JPG / PNG (source-dependent)
- **Image Size**: Varies
- **Annotations**: Single-label (One of 9 expression classes)

### 😄 Emotion Classes
- Angry  
- Contempt  
- Disgust  
- Fear  
- Happy  
- Natural (Neutral)  
- Sad  
- Sleepy  
- Surprised

---

## 🧹 Dataset Creation & Annotation Process

1. **Source Selection**
   - Merged data from top-quality facial emotion datasets hosted on Roboflow.
   - Included real, synthetic, and video frame data.

2. **Deduplication & Cleaning**
   - Removed duplicate or corrupt images using hash-matching and OpenCV image integrity checks.

3. **Annotation Standardization**
   - Unified inconsistent labels (e.g., “neutral” vs “natural”).
   - Converted all annotations into YOLOv8-compatible `.txt` files (one per image).
   - Ensured each bounding box tightly fits facial features.

4. **Class Balancing**
   - Balanced minority class samples using:
     - Image augmentation (flip, crop, contrast).
     - Oversampling to reduce class imbalance bias.

5. **Validation Split**
   - Stratified dataset into:
     - **Train** (80%)
     - **Validation** (10%)
     - **Test** (10%)

---

## 🧠 Model Training: YOLOv8

### 🔧 Parameters Used
```bash
epochs = 25
imgsz = 224
batch = 32
lr0 = 0.01
conf = 0.40
```
