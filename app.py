# 🌟 Streamlit App for Employee Salary Prediction
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image

# Mapping dictionaries for label-encoded values
workclass_map = {
    "Private": 4, "Self-emp-not-inc": 6, "Self-emp-inc": 5,
    "Federal-gov": 1, "Local-gov": 2, "State-gov": 3,
    "Without-pay": 7, "Never-worked": 0, "Other": 8
}

marital_map = {
    "Married-civ-spouse": 2, "Never-married": 4,
    "Divorced": 0, "Separated": 3, "Widowed": 5, "Married-spouse-absent": 1
}

occupation_map = {
    "Tech-support": 11, "Craft-repair": 1, "Other-service": 6, "Sales": 9,
    "Exec-managerial": 3, "Prof-specialty": 8, "Handlers-cleaners": 4,
    "Machine-op-inspct": 5, "Adm-clerical": 0, "Farming-fishing": 2,
    "Transport-moving": 13, "Priv-house-serv": 10, "Protective-serv": 7,
    "Armed-Forces": 14, "Other": 12
}

relationship_map = {
    "Husband": 0, "Own-child": 1, "Not-in-family": 2,
    "Unmarried": 3, "Other-relative": 4, "Wife": 5
}

race_map = {
    "Black": 0, "Asian-Pac-Islander": 1, "Amer-Indian-Eskimo": 2,
    "Other": 3, "White": 4
}

gender_map = {"Female": 0, "Male": 1}

country_map = {
    "United-States": 38, "Mexico": 22, "Philippines": 28, "Germany": 10,
    "Canada": 4, "India": 15, "Other": 0
}

# Load model
model = joblib.load("best_model.pkl")

# Page Config
st.set_page_config(page_title="Salary Predictor", page_icon="💼", layout="centered")

# Header with custom gradient background
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #6a11cb, #2575fc);
        color: white;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
    }
    .stButton > button {
        background-color: #e91e63;
        color: white;
        border-radius: 10px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>💼 Employee Salary Predictor</h1>", unsafe_allow_html=True)

st.write("Enter employee details below to predict whether the income is more than 50K 💰 or not.")

with st.form("salary_form"):
    st.markdown("### 📋 Employee Information")

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("🎂 Age (years)", 18, 90, 30)
        fnlwgt = st.number_input("📊 Final Weight (fnlwgt)", 10000, 1000000, 50000)
        edu_num = st.slider("🎓 Educational Number", 1, 16, 10)
        capital_gain = st.number_input("💸 Capital Gain", 0, 100000, 0)
        capital_loss = st.number_input("💸 Capital Loss", 0, 5000, 0)
        hours_per_week = st.slider("⏰ Hours per Week", 1, 100, 40)

    with col2:
        workclass_label = st.selectbox("🏢 Workclass", list(workclass_map.keys()))
        workclass = workclass_map[workclass_label]

        marital_label = st.selectbox("❤️ Marital Status", list(marital_map.keys()))
        marital_status = marital_map[marital_label]

        occupation_label = st.selectbox("🔧 Occupation", list(occupation_map.keys()))
        occupation = occupation_map[occupation_label]

        relationship_label = st.selectbox("👪 Relationship", list(relationship_map.keys()))
        relationship = relationship_map[relationship_label]

        race_label = st.selectbox("🌍 Race", list(race_map.keys()))
        race = race_map[race_label]

        gender_label = st.selectbox("⚧️ Gender", list(gender_map.keys()))
        gender = gender_map[gender_label]

        country_label = st.selectbox("🌐 Native Country", list(country_map.keys()))
        native_country = country_map[country_label]

    submit = st.form_submit_button("🔍 Predict Salary Group")

    if submit:
        input_df = pd.DataFrame({
            'age': [age], 'workclass': [workclass], 'fnlwgt': [fnlwgt],
            'educational-num': [edu_num], 'marital-status': [marital_status],
            'occupation': [occupation], 'relationship': [relationship],
            'race': [race], 'gender': [gender], 'capital-gain': [capital_gain],
            'capital-loss': [capital_loss], 'hours-per-week': [hours_per_week],
            'native-country': [native_country]
        })

        prediction = model.predict(input_df)
        result = '>50K' if prediction[0] == 1 else '<=50K'

        st.markdown("<h3 style='text-align: center; color: white;'>🎯 Prediction Result</h3>", unsafe_allow_html=True)
        st.success(f"✅ The predicted income group is: **{result}**")
