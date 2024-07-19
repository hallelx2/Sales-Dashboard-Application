import streamlit as st

def create_download_button(dataframe, filename):
    csv = dataframe.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data', data=csv, file_name=filename, mime='text/csv')
