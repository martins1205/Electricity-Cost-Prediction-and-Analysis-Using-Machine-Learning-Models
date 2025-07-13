
import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('random_forest_best_model.pkl')

# Title of the app
st.title('Electricity Cost Prediction App')

# Input fields for user to enter data
st.header('Enter the details of the site:')

site_area = st.number_input('Site Area (sq ft)', min_value=500, max_value=5000, step=1)
structure_type = st.selectbox('Structure Type', ['Commercial', 'Industrial', 'Mixed-use', 'Residential'])
water_consumption = st.number_input('Water Consumption (liters)', min_value=1000.0, max_value=11000.0, step=0.1)
recycling_rate = st.slider('Recycling Rate (%)', min_value=10, max_value=90, step=1)
utilisation_rate = st.slider('Utilisation Rate (%)', min_value=30, max_value=100, step=1)
air_quality_index = st.slider('Air Quality Index', min_value=0, max_value=200, step=1)
issue_resolution_time = st.slider('Issue Resolution Time (hours)', min_value=1, max_value=72, step=1)
resident_count = st.number_input('Resident Count', min_value=0, max_value=500, step=1)

# Predict button
if st.button('Predict Electricity Cost'):
    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'site area': [site_area],
        'structure type': [structure_type],
        'water consumption': [water_consumption],
        'recycling rate': [recycling_rate],
        'utilisation rate': [utilisation_rate],
        'air qality index': [air_quality_index],
        'issue reolution time': [issue_resolution_time],
        'resident count': [resident_count]
    })

    # Make prediction
    prediction = model.predict(input_data)

    # Display the prediction
    st.success(f'The predicted electricity cost is: ${prediction[0]:.2f}')
