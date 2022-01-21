import streamlit as st
import pandas as pd
# import plotly.express as px
import pickle

st.write("# Ames Housing Data Exploration")

test_model = pickle.load(open('ames-model.sav', 'rb'))

# Inputs
lot_area = st.number_input(
    label = "What is your total lot area, in square feet?",
    min_value = 1300,
    max_value = 39100,
    step = 100
)

first_floor = st.number_input(
    label = "What is the total area of your first floor, in square feet?",
    min_value = 372,
    max_value = 2223,
    step = 1
)

gr_liv = st.number_input(
    label = "What is the total area of your ground floor, in square feet?",
    min_value = 435,
    max_value = 2975,
    step = 5
)

run = st.button("Click here to get your prediction")

if run:
    input_data = pd.DataFrame(columns=['LotArea', '1stFlrSF', 'GrLivArea'])
    input_data = input_data.append({
        "LotArea":lot_area, 
        "1stFlrSF":first_floor, 
        "GrLivArea":gr_liv}, 
        ignore_index=True)
    st.write(f"Predicted Value: ${test_model.predict(input_data)[0]:,.2f}")