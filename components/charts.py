import streamlit as st
import plotly.express as px
from utils.plotting import create_line_chart, create_treemap, create_pie_chart

def render_charts(filtered_df, start_date, end_date):
    col1, col2 = st.columns((2))
    with col1:
        st.subheader("Category wise Sales")
        category_df = filtered_df.groupby(by=["Category"], as_index=False)["Sales"].sum()
        fig = px.bar(category_df, x="Category", y="Sales", text=['${:,.2f}'.format(x) for x in category_df["Sales"]],
                     template="seaborn")
        st.plotly_chart(fig, use_container_width=True, height=200)

    with col2:
        st.subheader("Region wise Sales")
        fig = px.pie(filtered_df, values="Sales", names="Region", hole=0.5)
        fig.update_traces(text=filtered_df["Region"], textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader('Time Series Analysis')
    linechart = create_line_chart(filtered_df)
    st.plotly_chart(linechart, use_container_width=True)

    st.subheader("Hierarchical view of Sales using TreeMap")
    treemap = create_treemap(filtered_df)
    st.plotly_chart(treemap, use_container_width=True)

    chart1, chart2 = st.columns((2))
    with chart1:
        st.subheader('Segment wise Sales')
        pie_chart = create_pie_chart(filtered_df, "Segment")
        st.plotly_chart(pie_chart, use_container_width=True)

    with chart2:
        st.subheader('Category wise Sales')
        pie_chart = create_pie_chart(filtered_df, "Category")
        st.plotly_chart(pie_chart, use_container_width=True)
