# Student Performance Prediction
A machine learning–powered web app that predicts whether a student will pass or fail based on demographic, educational, and test-related factors.
The app uses a trained classifier model and applies proper feature encoding to deliver accurate predictions with confidence scores.

## 🚀 Features
* ✔️ Predicts Pass / Fail
* ✔️ Shows confidence percentage
* ✔️ Uses trained ML model (student_model.pkl)
* ✔️ Encodes categorical features using mapping + saved columns
* ✔️ Smooth, modern UI with a soft pink academic theme
* ✔️ Fast predictions using Streamlit 

## How It Works
### 1. Dataset
#### Uses the expanded student performance dataset including features such as:
* Gender
* Ethnicity 
* Parental education
* Lunch type
* Test preparation course
* Math, Reading, Writing scores

### 2. Preprocessing
* Categorical encoding using label maps
* Ensuring training and inference columns match (model_columns.pkl)
* Handling feature order
* No missing data during prediction because missing fields are filled with default zeroes

### 3. ML Model
* Model type: Binary Classification (Pass / Fail)
* Preprocessing & training done inside the Jupyter Notebook
* Saved as student_model.pkl

### 4. Prediction Output
* 🔍 Pass/Fail prediction
* 📊 Confidence score (probability)
* Clean success/error messages

## Tech Stack
* Python
* Streamlit
* Pandas
* Scikit-Learn
* Pickle
* NumPy

## 📦 Installation & Setup
### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
```

### 3️⃣ Activate environment

#### Windows:
```bash
venv\Scripts\activate
```

#### Mac/Linux:
```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Streamlit app
```bash
streamlit run app.py
```

## 📁 Project Structure
```bash
│── app.py                               # Streamlit web app
│── Student Performance Prediction.ipynb # Model training notebook
│── Expanded_data_with_more_features.csv # Dataset
│── student_model.pkl                    # Trained ML model
│── model_columns.pkl                    # Correct column order for inference
│── requirements.txt
└── README.md
```

## Dataset 
Available on
Kaggle : https://www.kaggle.com/datasets/desalegngeb/students-exam-scores

## 🌐 Live Demo
https://studentperformancebot.streamlit.app/

## 📸 Screenshots
![img alt](https://github.com/nikhil-kumarrr/images/blob/main/Screenshot%202025-12-14%20193357.png?raw=true)
