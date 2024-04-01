import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(page_title='Dashboard', page_icon=':bar_chart', layout='wide')
st.title(':bar_chart: Sample Dashboard')
st.markdown('<style>div.block-container[padding-top:1rem;]</style>', unsafe_allow_html = True)
file = st.file_uploader(':file_folder: Upload a file', type = (['csv','txt', 'xlsx', 'xls']))

if file is not None:
    filename = file.name
    st.write(filename)
    df=pd.read_excel(filename)
else:
    df = pd.read_excel('Sample - Superstore.xls')
    st.write(df.head())
    
col1, col2 = st.columns((2))
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Getting the minimum and maximum date
start_date = pd.to_datetime(df['Order Date']).min()
end_date = pd.to_datetime(df['Order Date']).max()

with col1:
    date1 = pd.to_datetime(st.date_input('Start Date', start_date))

with col2:
    date2 = pd.to_datetime(st.date_input('End Date', end_date))

df = df[(df['Order Date']>=date1) & (df['Order Date']<=date2)].copy()

st.sidebar.header("Choose your filter: ")

# Region Filter
region = st.sidebar.multiselect("Pick your region", df["Region"].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df['Region'].isin(region)]


# State Filter
state = st.sidebar.multiselect("Pick your state", df['State'].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2['State'].isin(state)]


# City Filter
city = st.sidebar.multiselect("Pick your city", df['City'].unique())
if not city:
    df4 = df3.copy()
else:
    df4 = df3[df3['City'].isin(city)]

# Selecting conditions for the filters to run on
if not region and not state and not city:
    filtered_df = df
elif not state and not city:
    filtered_df = df[df["Region"].isin(region)]
elif not region and not city:
    filtered_df = df[df["State"].isin(state)]
elif state and city:
    filtered_df = df3[df["State"].isin(state) & df3["City"].isin(city)]
elif region and city:
    filtered_df = df3[df["Region"].isin(region) & df3["City"].isin(city)]
elif region and state:
    filtered_df = df3[df["Region"].isin(region) & df3["State"].isin(state)]
elif city:
    filtered_df = df3[df3["City"].isin(city)]
else:
    filtered_df = df3[df3["Region"].isin(region) & df3["State"].isin(state) & df3["City"].isin(city)]



