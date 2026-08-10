# GLAUCOVISION AI

## AI-Powered Glaucoma Screening System using ConvNeXt-Tiny

GLAUCOVISION AI is an end-to-end deep learning application for automated glaucoma screening from retinal fundus images. The system uses a fine-tuned **ConvNeXt-Tiny** model to classify images as **Normal** or **Glaucoma**, generate confidence and risk assessments, and produce downloadable screening reports through a Streamlit web application.

**Live Demo:** https://glaucovisionai-2gmtotw5bz5epjwxdpygry.streamlit.app/

---

## Problem Statement

Glaucoma can cause irreversible vision loss, making early screening important. This project explores how deep learning can assist retinal image screening by providing fast and accessible automated predictions.

The objective was to build a complete AI system rather than stopping at model training, covering **data preparation, model development, evaluation, inference, application development, reporting, and deployment**.

---

## Solution

```text
Retinal Fundus Image
        ↓
Image Preprocessing
        ↓
384 × 384 RGB Input
        ↓
ConvNeXt-Tiny
        ↓
Normal / Glaucoma
        ↓
Confidence Score
        ↓
Risk Assessment
        ↓
Prediction Explanation
        ↓
PDF Report
        ↓
Streamlit Web Application
```

---

## Dataset

The dataset contains retinal fundus images belonging to two classes:

- Normal
- Glaucoma

| Split | Images |
|---|---:|
| Training | 8,000 |
| Validation | 770 |
| Test | 770 |
| Total | 9,540 |

| Property | Value |
|---|---|
| Classification | Binary |
| Original Resolution | 512 × 512 |
| Model Input | 384 × 384 |
| Classes | Normal, Glaucoma |

The dataset was separated into training, validation, and test sets so that model training, validation, and final performance evaluation were performed on independent data.

---

## Why ConvNeXt-Tiny?

ConvNeXt-Tiny was selected because it provides a practical balance between **feature extraction capability, classification performance, computational requirements, and deployment feasibility**.

The model was adapted to the retinal image classification task using **transfer learning and fine-tuning**, allowing pretrained visual representations to be specialized for the target dataset.

---

## Methodology

### 1. Image Preprocessing

Uploaded retinal images are:

- Resized to `384 × 384`
- Converted to RGB
- Converted into model-ready numerical input
- Batched before inference

### 2. Model Development

- Architecture: **ConvNeXt-Tiny**
- Approach: **Transfer Learning + Fine-Tuning**
- Task: **Binary Classification**
- Classes: **Normal / Glaucoma**

### 3. Evaluation

The model was evaluated on an independent test set using:

- Accuracy
- ROC-AUC
- Precision
- Recall
- F1-Score
- Error analysis

---

## Model Performance

| Metric | Result |
|---|---:|
| Test Accuracy | **89.35%** |
| ROC-AUC | **0.953** |
| Test Samples | **770** |

The model achieved **89.35% test accuracy** with a **0.953 ROC-AUC**, indicating strong discrimination between the evaluated Normal and Glaucoma classes.

---

## Prediction Pipeline

```text
User Upload
     ↓
Image Validation
     ↓
Image Resize
     ↓
RGB Conversion
     ↓
Model Input Preparation
     ↓
ConvNeXt-Tiny Inference
     ↓
Probability
     ↓
Confidence Score
     ↓
Risk Assessment
     ↓
Prediction Explanation
     ↓
PDF Report
```

---

## Application Features

### AI Features

- Glaucoma classification
- Confidence score
- Probability estimation
- Risk-level assessment
- Prediction explanation

### Application Features

- Retinal image upload
- Image preview
- Real-time inference
- Automated PDF report
- Error handling
- Light and dark theme support
- Browser-based interface

### Deployment

- GitHub-based version control
- Streamlit Community Cloud deployment
- Cloud-based model retrieval
- End-to-end deployed inference

---

## Engineering Highlights

- Built an end-to-end computer vision inference pipeline.
- Applied transfer learning and fine-tuning with ConvNeXt-Tiny.
- Evaluated performance using multiple classification metrics.
- Integrated the trained model with Streamlit.
- Implemented automated PDF report generation.
- Added confidence and risk assessment logic.
- Separated prediction and reporting functionality into modular utilities.
- Resolved deployment issues involving Python/TensorFlow compatibility, dependency installation, memory constraints, and cloud runtime configuration.

---

## System Architecture

```text
                    GLAUCOVISION AI
                           |
             +-------------+-------------+
             |                           |
        Streamlit UI                ML Pipeline
             |                           |
       Image Upload               ConvNeXt-Tiny
             |                           |
       Image Preview               Prediction
             |                           |
             +-------------+-------------+
                           |
                  Confidence / Risk
                           |
                    PDF Generation
                           |
                    User Download
```

---

## Current Limitation

The current model assumes that the uploaded image is a retinal fundus image.

Since the classifier is trained for only two classes, arbitrary non-retinal images may still be assigned to either **Normal** or **Glaucoma**.

A stronger production-oriented pipeline would first validate whether the uploaded image is actually a retinal fundus image.

```text
Uploaded Image
      ↓
Fundus Image Validation
      ↓
   Valid Image?
    /       \
   No       Yes
   ↓         ↓
Reject    ConvNeXt-Tiny
             ↓
       Normal / Glaucoma
```

This is a planned improvement using **fundus-image validation or out-of-distribution detection**.

---

## Future Improvements

- Fundus-image validation
- Out-of-distribution detection
- Grad-CAM explainability
- Larger and more diverse datasets
- External validation
- Probability calibration
- Multi-disease retinal screening
- Model optimization for lower-latency inference

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Deep Learning | TensorFlow, Keras |
| Model | ConvNeXt-Tiny |
| Image Processing | Pillow, NumPy |
| Web Application | Streamlit |
| PDF Generation | ReportLab |
| Model Retrieval | gdown |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

---

## Project Structure

```text
GLAUCOVISION_AI_DEPLOY/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   ├── doctor_bg.jpg
│   ├── glaucoma_eye.jpg
│   └── healthy_eye.jpg
│
├── utils/
│   ├── __init__.py
│   ├── predict.py
│   ├── gradcam.py
│   └── pdf_report.py
│
└── notebooks/
    └── Glaucoma_detection.ipynb
```

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/saiii-vardhan08/GLAUCOVISION_AI_DEPLOY.git
cd GLAUCOVISION_AI_DEPLOY
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Medical Disclaimer

GLAUCOVISION AI is an **educational and research-oriented screening system**, not a medical diagnostic device.

Model predictions may contain false positives and false negatives. The system should not replace professional ophthalmological examination, diagnosis, or treatment.

---

## Author

### K. Saivardhan Goud

**B.Tech — Electronics & Communication Engineering**  
**KL University, Hyderabad**

**Current CGPA: 9.84**
### Specialization

**Generative AI**

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Computer Vision
- Generative AI
- End-to-End AI Engineering

Focused on building practical AI systems that combine **problem identification, data analysis, model development, evaluation, optimization, software engineering, and deployment**.

### Links

- **GitHub:** https://github.com/saiii-vardhan08
- **LinkedIn:** https://www.linkedin.com/in/saivardhangoudk08
- **Live Demo:** https://glaucovisionai-2gmtotw5bz5epjwxdpygry.streamlit.app/
