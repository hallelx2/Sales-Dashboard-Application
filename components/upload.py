import streamlit as st

def upload_file():
    file = st.file_uploader(':file_folder: Upload a file', type=['csv', 'txt', 'xlsx', 'xls'])
    return file
