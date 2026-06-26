import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("patient_wait_time_model.pkl")

st.set_page_config(page_title="Patient Wait Time Predictor", layout="wide")

st.title("🏥 Patient Queue Wait Time Prediction System")

st.write("Enter patient and queue details to predict waiting time.")

st.sidebar.header("Patient Details")

queue_length = st.sidebar.number_input(
    "Queue Length",
    min_value=0,
    max_value=100,
    value=5
)

arrival_hour = st.sidebar.slider(
    "Arrival Hour",
    0,
    23,
    10
)

arrival_minute = st.sidebar.slider(
    "Arrival Minute",
    0,
    59,
    30
)

arrival_day = st.sidebar.slider(
    "Arrival Day",
    1,
    31,
    30
)

arrival_month = st.sidebar.slider(
    "Arrival Month",
    1,
    12,
    3
)

is_weekend = st.sidebar.selectbox(
    "Weekend",
    [0,1]
)

service_time = st.sidebar.number_input(
    "Expected Service Time (Minutes)",
    value=15
)

total_time = st.sidebar.number_input(
    "Expected Total Time",
    value=30
)

input_data = pd.DataFrame({

    "queue_length":[queue_length],
    "arrival_hour":[arrival_hour],
    "arrival_minute":[arrival_minute],
    "arrival_day":[arrival_day],
    "arrival_month":[arrival_month],
    "is_weekend":[is_weekend],
    "service_time":[service_time],
    "total_time":[total_time]

})

if st.button("Predict Waiting Time"):

    prediction = model.predict(input_data)

    st.success(f"Estimated Waiting Time : {prediction[0]:.2f} Minutes")

st.divider()

st.subheader("Patient Information")

st.dataframe(input_data)