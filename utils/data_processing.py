import pandas as pd
import streamlit as st

def load_data(file):
    if file is not None:
        filename = file.name
        st.write(filename)
        if filename.endswith('csv'):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
    else:
        df = pd.read_excel('data/Sample - Superstore.xls')
        st.write(df.head())

    return df
