# pylint: skip-file

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Title of the web app 
st.title('Hello World!') 
# Input text box 
user_input = st.text_input('Enter your name') 
# Display the input 
st.write(f'Hello, {user_input}!')

@st.cache_data
def load_data(file):
    data = pd.read_csv(file)
    return data

st.title('Simple Data Application')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.write(data.head(20))

if uploaded_file is not None:
    if st.checkbox('Show histogram'): 
        column = st.selectbox('Select the column to create a histogram', data.columns) 
        plt.hist(data[column].dropna()) 
        st.pyplot(plt)