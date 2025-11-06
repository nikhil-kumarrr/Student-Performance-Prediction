# Student Performance Prediction

## Introduction

This project predicts whether a student will pass or fail based on their academic and lifestyle features. The goal is to help identify students who might need extra support.

---

### Features Used
* Gender
* Ethnicity
* Parental education
* Lunch type
* Test preparation course
* Math score
* Reading score
* Writing score
* Weekly study hours
* Absences
* Extra activities
---
### Project Workflow
1. Data Cleaning
* Missing values handled (categorical → most frequent).
* Numerical and categorical columns separated.
* Outliers treated using the IQR method.
* Count of outliers removed printed for verification.
---
### 2. Encoding & Scaling
* Categorical features label-encoded.
* Numerical features scaled for model training.
---
### 3. Exploratory Data Analysis
* Distribution charts
* Correlation heatmap
* Performance comparison based on study hours and absences
* Relationship between parental education & scores
---
### Models Trained
You trained two supervised learning models:
1. Logistic Regression
Accuracy: 100%
2. Random Forest Classifier
Accuracy: 99.6%
Best Model: Logistic Regression (based on accuracy and clean confusion matrix)
---
### Evaluation Metrics
For both models:
* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Classification Report
---

### Dataset
Available on
Kaggle : https://www.kaggle.com/datasets/desalegngeb/students-exam-scores

---
### How the Prediction Works
After training, the model predicts whether a student will:
* Pass (1)
* Fail (0)
---
### Tech Stack
* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
---
### Project Highlights
* Clean data preprocessing workflow
* High-accuracy models
* Clear EDA visuals
* Encoded + scaled training pipeline
* Realistic student performance prediction logic
