import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('fraud_model.pkl')

st.title("🔍 Real-Time Fraud Detection")
st.write("Enter transaction details below to check for potential fraud.")

amount = st.number_input("Transaction Amount")
time = st.number_input("Time (in seconds since first transaction)")

if st.button("Predict"):
    input_data = np.array([[amount, time] + [0]*28])  # dummy V1-V28s
    prediction = model.predict(input_data)
    result = "Fraud" if prediction[0] == 1 else "Not Fraud"
    st.write(f"Prediction: {result}")
