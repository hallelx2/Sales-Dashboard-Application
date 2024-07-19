import streamlit as st
import pandas as pd
import os
import warnings
from components.upload import upload_file
from components.filters import apply_filters
from components.charts import render_charts
from components.tables import render_tables
from utils.data_processing import load_data

warnings.filterwarnings('ignore')

st.set_page_config(page_title='Dashboard', page_icon=':bar_chart:', layout='wide')
st.title(':bar_chart: Sample Dashboard')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

file = upload_file()

df = load_data(file)

start_date, end_date, filtered_df = apply_filters(df)

render_charts(filtered_df, start_date, end_date)

render_tables(filtered_df)
