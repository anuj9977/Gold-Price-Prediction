import streamlit as st
import pickle
import numpy as np
import pandas as pd


model = pickle.load(open("model.pkl", "rb")) 


st.set_page_config(page_title="Gold Price Predictor", layout="centered")

st.title("Gold Price Prediction App")
st.markdown("This app predicts **Gold Price (GLD)** based on financial indicators like SPX, USO, SLV, and EUR/USD.")

st.divider()


col1, col2 = st.columns(2)

with col1:
    spx = st.number_input("S&P 500 Index (SPX)", min_value=0.0, step=0.1)
    uso = st.number_input("Crude Oil ETF (USO)", min_value=0.0, step=0.1)

with col2:
    slv = st.number_input("Silver ETF (SLV)", min_value=0.0, step=0.1)
    eurusd = st.number_input("EUR/USD Exchange Rate", min_value=0.0, step=0.001, format="%.3f")


if st.button("🔮 Predict Gold Price"):
    try:
        
        input_data = np.array([[spx, uso, slv, eurusd]])
        prediction = model.predict(input_data)

        st.success(f"Predicted Gold Price (GLD): **${prediction[0]:,.2f}**")
    except Exception as e:
        st.error(f" Error making prediction: {e}")

st.divider()

