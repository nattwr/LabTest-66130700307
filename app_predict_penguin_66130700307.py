
# import streamlit as st
# import pandas as pd
# import pickle
# from sklearn.preprocessing import LabelEncoder

# # Load the trained model
# with open('model_penguin_66130700307.pkl', 'rb') as file:
#     model = pickle.load(file)

# # Title of the app
# st.title('Predict Randomforest Penguin App')

# # Input fields for user to enter data
# island = st.selectbox('Select island :', ['Torgersen', 'Biscoe', 'Dream'])
# culmen_length_mm = st.number_input('Enter Culmen Length (mm):')
# culmen_depth_mm = st.number_input('Enter Culmen Depth (mm):')
# flipper_length_mm = st.number_input('Enter Flipper length (mm):')
# body_mass_g = st.number_input('Enter Body Mass (g):')
# sex = st.selectbox('Select sex :', ['Male','Female'])

# island_encode = island_encoder.transform(island)
# sex_encode = sex_encoder.transform(sex)

# # Create a DataFrame for the input
# input_data = pd.DataFrame({
#     'island': [island_encode],
#     'culmen_length_mm': [culmen_length_mm],
#     'culmen_depth_mm': [culmen_depth_mm],
#     'flipper_length_mm': [flipper_length_mm],
#     'body_mass_g': [body_mass_g],
#     'sex': [sex_encode]
# })

# # Make prediction
# if st.button('Predict'):
#     prediction = model.predict(input_data)
#     result = species_encoder.inverse_transform(prediction) 
#     st.write(f'Predicted Specie: {round(result)}')
import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# Load the trained model
with open('model_penguin_66130700307.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the encoders
species_encoder = LabelEncoder().fit(['Adelie', 'Chinstrap', 'Gentoo'])
island_encoder = LabelEncoder().fit(['Torgersen', 'Biscoe', 'Dream'])
sex_encoder = LabelEncoder().fit(['MALE', 'FEMALE'])

# Title of the app
st.title('Predict Randomforest Penguin App')

# Input fields for user to enter data
island = st.selectbox('Select island:', ['Torgersen', 'Biscoe', 'Dream'])
culmen_length_mm = st.number_input('Enter Culmen Length (mm):')
culmen_depth_mm = st.number_input('Enter Culmen Depth (mm):')
flipper_length_mm = st.number_input('Enter Flipper Length (mm):')
body_mass_g = st.number_input('Enter Body Mass (g):')
sex = st.selectbox('Select sex:', ['MALE', 'FEMALE'])

# Encode the input values
island_encode = island_encoder.transform([island])[0]
sex_encode = sex_encoder.transform([sex])[0]

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'island': [island_encode],
    'culmen_length_mm': [culmen_length_mm],
    'culmen_depth_mm': [culmen_depth_mm],
    'flipper_length_mm': [flipper_length_mm],
    'body_mass_g': [body_mass_g],
    'sex': [sex_encode]
})

# Make prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    result = species_encoder.inverse_transform(prediction)
    st.write(f'Predicted Species: {result[0]}')

