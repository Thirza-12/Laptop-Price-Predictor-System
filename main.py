import streamlit as st
import joblib
import numpy as np
brand = ['Acer', 'Alienware', 'Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'Microsoft']
pro_model = ['i3', 'i5', 'i7', 'other']
graphic_brand = ['amd', 'intel', 'nvidia']
os_name = ['linux', 'mac', 'windows']

# Load the model
price = joblib.load("model.pkl")

def predict_price(comp, ram, stype, storage, screen, pro, speed, graphic, gsize, os, mass):
    # Predict price using the loaded model
    prediction = price.predict([[comp, ram, stype, storage, screen, pro, speed, graphic, gsize, os, mass]])
    rounded_prediction = round(float(prediction[0]) / 1.8, 2)  # Round off prediction to 2 decimal places
    return rounded_prediction  # Return the rounded prediction # Convert the prediction to INR

# Streamlit UI
st.title("Laptop Price Predictor")

comp = st.selectbox("Company Name", brand)
ram = st.number_input("RAM Amount", min_value=1, value=4)
stype = st.radio("Does it have SSD?", ("No", "Yes"))
stype = 1 if stype == "Yes" else 0
storage = st.number_input("Storage Amount (GB)", min_value=1, value=256)
screen = st.number_input("Screen Size (inches)", min_value=10.0, value=15.6)
pro = st.selectbox("Processor model", pro_model)
speed = st.number_input("Clock Speed", min_value=1.0, value=2.0)
graphic = st.selectbox("Graphic Card Brand", graphic_brand)
gsize = st.number_input("Graphic Card Size", min_value=1, value=4)
os = st.selectbox("Operating System", os_name)
mass = st.number_input("Mass of the Laptop (kg)", min_value=0.1, value=2.0)

if st.button("Predict Price"):
    prediction = predict_price(brand.index(comp), ram, stype, storage, screen, pro_model.index(pro), speed,
                               graphic_brand.index(graphic), gsize, os_name.index(os), mass)
    st.success(f"The Price of this particular laptop is: {prediction} INR")
