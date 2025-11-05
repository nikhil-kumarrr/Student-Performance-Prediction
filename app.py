import streamlit as st
import pandas as pd
import pickle

# Load model
with open("student_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load model columns
with open("model_columns.pkl", "rb") as f:
    model_cols = pickle.load(f)

# UI Styling
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f8d7e8;
    font-family: 'Segoe UI', sans-serif;
}

[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}

h1 {
    color: #b02a7c;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
}

.stButton > button {
    background-color: #e64997;
    color: white;
    border-radius: 8px;
    padding: 10px 22px;
    font-size: 18px;
    font-weight: 600;
    width: 100%;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #d03885;
    transform: scale(1.03);
}

.input-box {
    background: #ffe8f3;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #ffb6d5;
    margin-bottom: 18px;
}

footer {visibility: hidden;}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# App title
st.title("Student Performance Prediction")

st.markdown("Enter student information to estimate the result.")

# Form Structure
with st.container():
    st.markdown("<div class='input-box'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["male", "female"])
        ethnicity = st.selectbox("Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
        lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
        test_prep = st.selectbox("Test Preparation", ["none", "completed"])

    with col2:
        parent_edu = st.selectbox("Parental Education", [
            "bachelor's degree", "some college", "master's degree",
            "associate's degree", "high school", "some high school"
        ])
        math = st.number_input("Math Score", 0, 100, 50)
        reading = st.number_input("Reading Score", 0, 100, 50)
        writing = st.number_input("Writing Score", 0, 100, 50)

    st.markdown("</div>", unsafe_allow_html=True)

# Prepare input
data = {
    "Gender": gender,
    "Ethnicity": ethnicity,
    "ParentalEducation": parent_edu,
    "LunchType": lunch,
    "TestPrep": test_prep,
    "MathScore": math,
    "ReadingScore": reading,
    "WritingScore": writing
}

df = pd.DataFrame([data])

# Encoding map
label_map = {
    "Gender": {"female": 0, "male": 1},
    "Ethnicity": {"group A": 0, "group B": 1, "group C": 2, "group D": 3, "group E": 4},
    "ParentalEducation": {
        "associate's degree": 0, "bachelor's degree": 1, "high school": 2,
        "master's degree": 3, "some college": 4, "some high school": 5
    },
    "LunchType": {"free/reduced": 0, "standard": 1},
    "TestPrep": {"none": 0, "completed": 1}
}

for col, mapping in label_map.items():
    df[col] = df[col].map(mapping)

df = df.reindex(columns=model_cols, fill_value=0)

# Predict
if st.button("Predict Result"):
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    if prediction == 1:
        st.success(f"✅ Student is likely to Pass\nConfidence: {probability:.2%}")
    else:
        st.error(f"❌ Student may Fail\nConfidence: {(1-probability):.2%}")

st.markdown("<hr style='margin-top:40px;'>", unsafe_allow_html=True)
st.caption("Built with Machine Learning | Student Result Predictor")
