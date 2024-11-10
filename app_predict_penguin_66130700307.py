
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('model_penguin_66130700307.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title('Predict Randomforest Penguin App')

# Input fields for user to enter data
island = st.selectbox('Select island :', ['Torgersen', 'Biscoe', 'Dream'])
culmen_length_mm = st.number_input('Enter Culmen Length (mm):')
culmen_depth_mm = st.number_input('Enter Culmen Depth (mm):')
flipper_length_mm = st.number_input('Enter Flipper length (mm):')
body_mass_g = st.number_input('Enter Body Mass (g):')
sex = st.selectbox('Select sex :', ['Male','Female'])

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'island': [island],
    'culmen_length_mm': [culmen_length_mm],
    'culmen_depth_mm': [culmen_depth_mm],
    'flipper_length_mm': [flipper_length_mm],
    'body_mass_g': [body_mass_g],
    'sex': [sex]
})

# Make prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f'Predicted Specie: {round(prediction[0])}')

