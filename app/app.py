import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""
            # This is a header
            ## This is a sub header
            This is text
            """)


df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 5)


def get_data():
    return pd.DataFrame(
            np.random.randn(3, 3),
            columns=['a', 'b', 'c'])

@st.cache
def get_cached_data():
    return get_data()

columns = st.columns(2)


columns[0].write("Uncached dataframe")
columns[0].write(get_data())

columns[1].write("Cached dataframe")
columns[1].write(get_cached_data())