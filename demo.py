import streamlit as st
import pandas as pd
import numpy as np

# Titling
st.title('Sample title')

# Streamlit writing
st.write("This is a test!")

# Streamlit magic
"Help"

# Sliders + widget updating
x = st.slider("Slider", 10, 200, 15)
x

# pandas integration
df = pd.DataFrame({"Name": ['Darren'], "Age": ["21"]})
# st.write(df)
df

# charts
df = pd.DataFrame({"Age": np.random.randn(5)})

st.line_chart(df)


# checkbox
test = st.checkbox('Checkbox')

if test:
    "HI"

# sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("Hi")
