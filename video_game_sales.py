import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Video Game Sales')

df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

# 3D scatterplot of sales in 3 regions
st.subheader("Video Game Sales in NA, EU and JP")
st.write(
'''
The 3D scatterplot below visualizes the distribution of video game sales with release date from 1985 to 2016. 
Each dot in the 3D space represents a game, and the x, y and z axis represent its sales in NA, EU and JP.
The color of the dot represents the year of release of the game.
'''
)

fig = px.scatter_3d(
                data_frame=df,
                x="NA_Sales",
                y="EU_Sales",
                z="JP_Sales",
                color= "Year_of_Release",
                title="Game Sales in NA, EU and JP",
            )

st.plotly_chart(fig, use_container_width=True)

# bar chart of sales over years
st.subheader("Video Game Sales from 1980 to 2016")
st.write(
'''
The bar chart below shows the video game sales from 1980 to 2016.
There are 2 options for the visualization: average sales or total sales.
User could see the trend of sales over the years and compare the sales by region.
'''
)

# clean up the dataset
df = df.loc[df['Year_of_Release'] <= 2016]

histo_type = st.selectbox('Histogram Function', ('Average', 'Sum'), key=0)
st.write('Selected Histogram Function: ', histo_type)
func = "avg" if (histo_type == "Average") else "sum"

selected_region = st.selectbox('Sales by Region', ('NA_Sales', 'EU_Sales', 'JP_Sales', 'Global_Sales'), key=1)
st.write('Selected Sale Region: ', selected_region)

fig = px.histogram(
    data_frame=df,
    x="Year_of_Release",
    y=selected_region,
    title=histo_type + " of Sales by Years",
    histfunc=func,
)

st.plotly_chart(fig, use_container_width=True)

# 2D scatterplot of ratings vs. sales
st.subheader("Video Game Sales vs. Ratings")
st.write(
'''
The 2D scatterplot below visualizes video game sales and ratings from 1985 to 2016.
User could select the year of release, rating score type, and sales by region they want to examine.
They can also choose the games of specific platforms.
'''
)
df = df.dropna()

years = df['Year_of_Release'].unique().astype(int)
years = years.tolist()
year = st.slider('Select a Year', min(years), max(years), 2007)
st.write("Sales and ratings in: ", year)

score_type = st.selectbox('Score Type:', ('Critic_Score', 'User_Score'))
st.write('Selected Score Type: ', score_type)

sale_region = st.selectbox('Sales by Region', ('NA_Sales', 'EU_Sales', 'JP_Sales', 'Global_Sales'), key=2)
st.write('Selected Sale Region: ', sale_region)

platforms = df['Platform'].unique().tolist()
platform = st.multiselect('Platform(s): ', platforms, ['PS3', 'X360'], key=0)
st.write('Selected Platform(s): ', platform)

cur_dataset =  df.loc[df['Year_of_Release'] == year]
cur_dataset =  cur_dataset.loc[cur_dataset['Platform'].isin(platform)]
cur_dataset = cur_dataset.astype({"NA_Sales": float, "EU_Sales": float, "JP_Sales": float, 
                                "Global_Sales": float, "User_Score": float})

fig = px.scatter(
    data_frame=cur_dataset,
    x=sale_region,
    y=score_type,
    color="Platform",
    title="Video Game Sales vs. Ratings",
)

st.plotly_chart(fig, use_container_width=True)

# 2D scatterplot of sales vs. year of release (different genres)
st.subheader("Video Game Sales of Different Genres")
st.write(
'''
This 2D scatterplot visualizes video game sales of different genres over years.
User could select the game genres they want to examine and compare the sales between different genres.
'''
)

sale_region = st.selectbox('Sales by Region', ('NA_Sales', 'EU_Sales', 'JP_Sales', 'Global_Sales'), key=3)
st.write('Selected Sale Region: ', sale_region)

genres = df['Genre'].unique().tolist()
genre = st.multiselect('Genre(s): ', genres, ['Action', 'Shooter'], key=1)
st.write('Selected Genre(s): ', genre)

df_genre = df.loc[df['Genre'].isin(genre)]
fig = px.scatter(
    data_frame=df_genre,
    x="Year_of_Release",
    y=sale_region,
    color="Genre",
    title="Sales of Games of Different Genres",
)
st.plotly_chart(fig, use_container_width=True)

