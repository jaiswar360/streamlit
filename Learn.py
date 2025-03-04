import streamlit as st
import pandas as pd
import numpy as np

st.write(""" 
         # Learning Streamlit 
         *with Python*
         """)


st.write(""" ### Input Fields """)

name = st.text_input('Enter your Name:')
age = st.text_input('Enter your Age:')
fav_mov = st.text_input('Enter your Favourite Movie:')

st.write(f'Hello {name}, you are {age} years old and your favourite movie is {fav_mov}.')

st.write(""" ### TV Show Watchtime Data (2024) """)

data = pd.read_csv("TV Show Watchtime Dataset for 2024.csv")
st.write(data)

st.write(""" ### Random Charts """)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data) 
st.bar_chart(chart_data)