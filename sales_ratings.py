import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Video Game Sales and Ratings')

df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

# 3D scatterplot of sales in 3 regions
st.subheader("3D scatterplot of sales in 3 regions")
fig = px.scatter_3d(
                data_frame=df,
                x="NA_Sales",
                y="EU_Sales",
                z="JP_Sales",
                color= "Year_of_Release",
                title="Game Sales in NA, EU and JP",
            )

st.plotly_chart(fig, use_container_width=True)

# scatterplot of ratings vs. sales
st.subheader("scatterplot of ratings vs. sales")
df = df.dropna()

years = df['Year_of_Release'].unique().astype(int)
years = years.tolist()
year = st.slider('Select a Year', min(years), max(years), 2005)
st.write("Sales and ratings in: ", year)

score_type = st.selectbox('Score Type:', ('Critic_Score', 'User_Score'))
st.write('Selected Score Type: ', score_type)

sale_region = st.selectbox('Sales Region', ('NA_Sales', 'EU_Sales', 'JP_Sales', 'Global_Sales'))
st.write('Selected Sale Region: ', sale_region)

platforms = df['Platform'].unique().tolist()
platform = st.multiselect('Platform(s): ', platforms, ['PS4', 'XB'])
st.write('Selected Platform(s): ', platform)

cur_dataset =  df.loc[df['Year_of_Release'] == year]
cur_dataset =  cur_dataset.loc[cur_dataset['Platform'].isin(platform)]
cur_dataset = cur_dataset.astype({"Global_Sales": float, "User_Score": float})

fig = px.scatter(
    data_frame=cur_dataset,
    x=sale_region,
    y=score_type,
    color="Platform",
    title="Game Sales vs. Ratings",
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("sales of over years")

