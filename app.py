import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('depression_model.pkl')

# Page config
st.set_page_config(
    page_title="Depression Prediction",
    page_icon="🧠",
    layout="centered"
)

# Title
st.title("🧠 Depression Prediction App")
st.markdown("Fill in the details below to predict the likelihood of depression.")
st.divider()

# Input fields
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", min_value=18, max_value=59, value=25)
    academic_pressure = st.slider("Academic Pressure", min_value=0, max_value=5, value=3)
    study_satisfaction = st.slider("Study Satisfaction", min_value=0, max_value=5, value=3)
    work_study_hours = st.slider("Work/Study Hours", min_value=0, max_value=12, value=6)
    financial_stress = st.slider("Financial Stress", min_value=1, max_value=5, value=3)

with col2:
    sleep_duration = st.selectbox(
        "Sleep Duration",
        ['Less than 5 hours', '5-6 hours', '7-8 hours', 'More than 8 hours']
    )
    dietary_habits = st.selectbox(
        "Dietary Habits",
        ['Unhealthy', 'Moderate', 'Healthy']
    )
    suicidal_thoughts = st.selectbox(
        "Have you ever had suicidal thoughts?",
        ['Yes', 'No']
    )
    family_history = st.selectbox(
        "Family History of Mental Illness",
        ['Yes', 'No']
    )

st.divider()

# Predict button
if st.button("Predict", use_container_width=True):

    # Prepare input data
    input_data = pd.DataFrame({
        'Age': [age],
        'Academic Pressure': [academic_pressure],
        'Study Satisfaction': [study_satisfaction],
        'Work/Study Hours': [work_study_hours],
        'Financial Stress': [financial_stress],
        'Sleep Duration': [sleep_duration],
        'Dietary Habits': [dietary_habits],
        'Have you ever had suicidal thoughts ?': [1 if suicidal_thoughts == 'Yes' else 0],
        'Family History of Mental Illness': [1 if family_history == 'Yes' else 0]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    st.divider()

    # Show result
    if prediction == 1:
        st.error("⚠️ The model predicts signs of **Depression**")
        st.metric("Confidence", f"{probability[1]*100:.1f}%")
        st.warning("Please consider consulting a mental health professional.")
    else:
        st.success("✅ The model predicts **No Depression**")
        st.metric("Confidence", f"{probability[0]*100:.1f}%")
        st.info("Keep maintaining healthy habits!")