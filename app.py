import streamlit as st
import pandas as pd
import numpy as np
import joblib 

import streamlit as st

try:
    import joblib
    st.write("✅ joblib imported successfully")
except ModuleNotFoundError:
    st.write("❌ joblib NOT found")

#load the data
model=joblib.load('Linear_Regression_model.pkl')

#title of app
st.title('AirCraft Fuel Consuption Predictor')

#Input Fields

flight_distance=st.number_input('Flight_Distance')
number_of_passanger=st.number_input('Number_Of_Passanger')
flight_duration=st.number_input('Flight_Duration(Hours)')
aircraft_type=st.selectbox('Aircraft_Type',['Type1','Type2','Type3'])

#Creating a dataframe

input_data=pd.DataFrame(
    {
        'Flight_Distance': [flight_distance],
        'Number_of_Passengers' :[number_of_passanger],
        'Flight_Duration':[flight_duration],
        'Aircraft_Type_Type1':[1 if aircraft_type == 'Type1' else 0],
        'Aircraft_Type_Type2':[1 if aircraft_type == 'Type2' else 0],
        'Aircraft_Type_Type3':[1 if aircraft_type == 'Type3' else 0]
    }
)

if st.button('Predict'):
    Fuel_Consumption =model.predict(input_data)
    st.write(Fuel_Consumption)
