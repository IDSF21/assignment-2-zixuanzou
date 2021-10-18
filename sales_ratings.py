import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Video Game Sales with Ratings')

df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

fig = px.scatter_3d(
                data_frame=df,
                x="NA_Sales",
                y="EU_Sales",
                z="JP_Sales",
                color= "Year_of_Release",
                title="Game Sales in NA, EU and JP",
            )

st.plotly_chart(fig, use_container_width=True)

df = df.dropna()
print(df.shape)

years = df['Year_of_Release'].unique().astype(int)
years = years.tolist()
print(len(years))

year = st.slider('Select a Year', min(years), max(years), 2005)
st.write("Sales and ratings in: ", year)
cur_year =  df.loc[df['Year_of_Release'] == year]
cur_year = cur_year.astype({"Global_Sales": float, "User_Score": float})

fig = px.scatter(
    data_frame=cur_year,
    x="Global_Sales",
    y="User_Score",
    color="Platform",
    title="Game Sales vs. Ratings",
)

st.plotly_chart(fig, use_container_width=True)

# a = cur_year.sort_values('User_Score')
# a


