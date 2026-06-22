# 👁️ GLAUCOVISION AI

## AI-Powered Glaucoma Screening System using Deep Learning and ConvNeXt-Tiny

GLAUCOVISION AI is an end-to-end deep learning application developed for automated glaucoma screening using retinal fundus images. The system leverages a fine-tuned ConvNeXt-Tiny architecture to classify retinal images as either **Normal** or **Glaucoma**, while providing confidence scores, risk assessment, clinical interpretation, and downloadable PDF reports through an interactive Streamlit web application.

---

# 📌 Problem Statement

Glaucoma is one of the leading causes of irreversible blindness worldwide. Since optic nerve damage caused by glaucoma cannot be reversed, early detection plays a crucial role in preventing severe vision loss.

Traditional glaucoma diagnosis requires specialist examination and clinical expertise, which may not always be accessible in resource-constrained environments. This project aims to explore how Deep Learning can assist in the early screening process by providing rapid and automated analysis of retinal fundus images.

---

# 🎯 Project Objectives

* Develop an AI-powered glaucoma screening system.
* Classify retinal fundus images into Normal and Glaucoma categories.
* Generate confidence scores and risk assessments.
* Provide clinical interpretation of predictions.
* Generate downloadable PDF reports.
* Deploy an easy-to-use web application for practical usage.

---

# 📂 Dataset

The project utilizes retinal fundus images categorized into:

* Normal
* Glaucoma

### Dataset Distribution

| Split      | Images |
| ---------- | ------ |
| Train      | 8000   |
| Validation | 770    |
| Test       | 770    |

### Image Resolution

* Original Resolution: 512 × 512
* Model Input Resolution: 384 × 384

---

# ⚠️ Challenges Faced

## 1. Medical Image Variability

Retinal fundus images exhibited significant variations in:

* Illumination
* Contrast
* Retinal pigmentation
* Image quality

These variations affected model generalization and prediction consistency.

## 2. Overfitting Risk

Medical imaging datasets are comparatively smaller than large-scale natural image datasets. Initial experiments showed signs of overfitting, requiring careful use of transfer learning and fine-tuning strategies.

## 3. Clinical Reliability

High accuracy alone is insufficient in healthcare applications. False predictions can have serious consequences, making confidence analysis and risk assessment equally important.

## 4. Deployment Challenges

Transforming a trained model into a user-friendly application required:

* Real-time image preprocessing
* Error handling
* PDF report generation
* User experience optimization
* Deployment considerations

---

# 🤖 Why ConvNeXt-Tiny?

Several CNN architectures were evaluated before selecting ConvNeXt-Tiny.

ConvNeXt-Tiny was chosen because it offers:

* Strong feature extraction capability
* Modernized CNN design inspired by Vision Transformers
* Excellent performance on image classification tasks
* Better computational efficiency than larger architectures
* Practical suitability for deployment

### Framework

* TensorFlow
* Keras

---

# 🔬 Methodology

## Step 1: Image Preprocessing

Each retinal image undergoes:

* Resizing to 384 × 384
* RGB conversion
* Tensor preparation
* Model-ready formatting

---

## Step 2: Deep Learning Model

### Architecture

ConvNeXt-Tiny

### Approach

* Transfer Learning
* Fine-Tuning
* Binary Classification

### Classes

* Normal
* Glaucoma

---

## Step 3: Evaluation

The model was evaluated using an independent test dataset.

### Evaluation Metrics

* Accuracy
* ROC-AUC
* Confidence Score Analysis
* Error Analysis

---

#  Unique Project Workflow

Unlike many academic glaucoma classification projects that stop at model training and evaluation, this project implements a complete end-to-end AI workflow.

Retinal Fundus Image

↓ Upload

↓ Preprocessing

↓ ConvNeXt-Tiny Inference

↓ Confidence Score Calculation

↓ Risk Assessment

↓ Clinical Interpretation

↓ PDF Report Generation

↓ Streamlit Deployment

This transforms the project from a research prototype into a practical screening application.

---

# 📊 Results

| Metric            | Score      |
| ----------------- | ---------- |
| Test Accuracy     | 89.35%     |
| ROC-AUC Score     | 0.953      |
| Test Dataset Size | 770 Images |

### Key Observations

* Strong separation between Normal and Glaucoma classes.
* Consistent confidence score generation.
* Practical performance suitable for screening assistance.

---

# 🔍 Error Analysis

Observed failure cases included:

### False Positives

Some normal retinal images displayed optic disc characteristics resembling glaucoma patterns.

### False Negatives

Certain glaucoma cases exhibited subtle visual abnormalities that were difficult for the model to distinguish.

### Additional Factors

* Low-quality retinal scans
* Poor illumination
* Borderline clinical cases

Future improvements can focus on larger datasets and explainable AI techniques.

---

# 💻 Application Features

### AI Features

* Glaucoma Detection
* Confidence Score Calculation
* Risk Level Assessment
* Clinical Interpretation

### User Features

* Retinal Fundus Image Upload
* Real-Time Prediction
* Downloadable PDF Report
* Error Handling
* Responsive Streamlit Interface

### Deployment Features

* Lightweight Architecture
* Browser-Based Access
* Easy Integration

---

#  Technology Stack

## Deep Learning

* TensorFlow
* Keras
* ConvNeXt-Tiny

## Data Processing

* NumPy
* Pillow

## Deployment

* Streamlit

## Reporting

* ReportLab

## Programming Language

* Python

---

# 📈 Future Improvements

Potential future enhancements include:

* Multi-class retinal disease classification
* Larger clinical datasets
* Explainable AI techniques
* Cloud API deployment
* Integration with ophthalmology workflows
* Clinical decision support systems

---

# 🎓 Key Learnings

Through this project, I gained hands-on experience in:

* Deep Learning model development
* Medical image classification
* Transfer Learning
* Model evaluation and error analysis
* Streamlit application development
* PDF report generation
* End-to-end AI deployment workflows

This project strengthened my understanding of how machine learning models can be transformed into complete real-world applications.

---

# ✅ Conclusion

GLAUCOVISION AI demonstrates how deep learning can assist in early glaucoma screening through automated retinal image analysis.

By combining ConvNeXt-Tiny, confidence-based risk assessment, clinical interpretation, PDF reporting, and an interactive Streamlit application, the project delivers a complete end-to-end AI screening workflow rather than a standalone classification model.

The system achieved a **Test Accuracy of 89.35%** and a **ROC-AUC Score of 0.953**, demonstrating strong predictive capability while maintaining practical usability through deployment.

---

# 👨‍💻 Author

**K. Saivardhan Goud**

B.Tech – Electronics & Communication Engineering (9.84 - current CGPA)
KL University Hyderabad

Areas of Interest:

* Artificial Intelligence
* Machine Learning
* Deep Learning
* Computer Vision
* Generative AI

Focused on building end-to-end AI applications that combine research, model development, deployment, and user-centric experiences.

GitHub: GitHub: [K. Saivardhan Goud](https://github.com/saiii-vardhan08)
LinkedIn: LinkedIn: [Connect on LinkedIn](www.linkedin.com/in/saivardhangoudk08)
