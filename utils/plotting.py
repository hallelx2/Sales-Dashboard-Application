import plotly.express as px
import pandas as pd

def create_line_chart(filtered_df):
    filtered_df["month_year"] = filtered_df["Order Date"].dt.to_period("M")
    linechart = pd.DataFrame(filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
    fig = px.line(linechart, x="month_year", y="Sales", labels={"Sales": "Amount"}, height=500, width=1000, template="gridon")
    return fig

def create_treemap(filtered_df):
    fig = px.treemap(filtered_df, path=["Region", "Category", "Sub-Category"], values="Sales", hover_data=["Sales"],
                     color="Sub-Category")
    fig.update_layout(width=800, height=650)
    return fig

def create_pie_chart(filtered_df, column):
    fig = px.pie(filtered_df, values="Sales", names=column, template="plotly_dark")
    fig.update_traces(text=filtered_df[column], textposition="inside")
    return fig
