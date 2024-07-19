import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd
from utils.download import create_download_button

def render_tables(filtered_df):
    cl1, cl2 = st.columns((2))
    with cl1:
        with st.expander("Category_ViewData"):
            category_df = filtered_df.groupby(by=["Category"], as_index=False)["Sales"].sum()
            st.write(category_df.style.background_gradient(cmap="Blues"))
            create_download_button(category_df, "Category.csv")

    with cl2:
        with st.expander("Region_ViewData"):
            region = filtered_df.groupby(by="Region", as_index=False)["Sales"].sum()
            st.write(region.style.background_gradient(cmap="Oranges"))
            create_download_button(region, "Region.csv")

    st.subheader(':point_right: Month wise Sub-Category Sales Summary')
    with st.expander("Summary_Table"):
        df_sample = filtered_df[0:5][["Region", "State", "City", "Category", "Sales", "Profit", "Quantity"]]
        fig = ff.create_table(df_sample, colorscale="Cividis")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("Month wise sub-Category Table")
        filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
        sub_category_Year = pd.pivot_table(data=filtered_df, values="Sales", index=["Sub-Category"], columns="month")
        st.write(sub_category_Year.style.background_gradient(cmap="Blues"))

    data1 = px.scatter(filtered_df, x="Sales", y="Profit", size="Quantity")
    data1['layout'].update(title="Relationship between Sales and Profits using Scatter Plot.",
                           titlefont=dict(size=20), xaxis=dict(title="Sales", titlefont=dict(size=19)),
                           yaxis=dict(title="Profit", titlefont=dict(size=19)))
    st.plotly_chart(data1, use_container_width=True)

    with st.expander("View Data"):
        st.write(filtered_df.iloc[:500, 1:20:2].style.background_gradient(cmap="Oranges"))

    create_download_button(filtered_df, "Data.csv")
