import streamlit as st
import pandas as pd

def apply_filters(df):
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    start_date = pd.to_datetime(df['Order Date']).min()
    end_date = pd.to_datetime(df['Order Date']).max()

    col1, col2 = st.columns((2))
    with col1:
        date1 = pd.to_datetime(st.date_input('Start Date', start_date))

    with col2:
        date2 = pd.to_datetime(st.date_input('End Date', end_date))

    df = df[(df['Order Date'] >= date1) & (df['Order Date'] <= date2)].copy()

    st.sidebar.header("Choose your filter: ")

    region = st.sidebar.multiselect("Pick your region", df["Region"].unique())
    state = st.sidebar.multiselect("Pick your state", df['State'].unique())
    city = st.sidebar.multiselect("Pick your city", df['City'].unique())

    filtered_df = df
    if region:
        filtered_df = filtered_df[filtered_df["Region"].isin(region)]
    if state:
        filtered_df = filtered_df[filtered_df["State"].isin(state)]
    if city:
        filtered_df = filtered_df[filtered_df["City"].isin(city)]

    return date1, date2, filtered_df
