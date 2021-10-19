## Project Goals
The goal of this interactive data science application is to explore the video game sales from 1980 to 2016.
It allows the users to examine the trend of video games sales from different perspectives.
Users will be able to answer the question "How could various factors, such as platform, genre and ratings, impact video game sales?"

The dataset I used for this project is from Kaggle [Link](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings).


## Design Decisions

**3D Scatterplot of Video Game Sales in NA, EU and JP**

This plot gives the users an overall impression of the distribution of video game sales in the 3 major regions - NA, EU and JP - from 1980 to 2016.
Each dot in the 3D space represents a game, and the x, y and z axis represent its sales in NA, EU and JP.
The color of the dot represents the year of release of the game.

Users can understand the impact of region on game sales by examining this plot - rotating, zooming in, looking at specific axes, etc.

**Bar Chart of Video Game Sales from 1980 to 2016**

The bar chart shows the video game sales from 1980 to 2016.
There are 2 options for the visualization: average sales or total sales.
User could see the trend of sales over the years and compare the sales by region.

**2D Scatterplot of Game Sales vs. Ratings**

The 2D scatterplot visualizes video games sales and ratings from 1985 to 2016.
User could select the year of release, rating score type, and sales by region they want to examine.
They can also choose the games of specific platforms.

**2D Scatterplot of Game Sales of Different Genres**

This 2D scatterplot visualizes video games sales of different genres from the 1980s to 2016.
User could select the game genres they want to examine and compare the sales between different genres.

## Development Process
I worked solo on this project. 
I spent about 10 hours on this - about 1 hour choosing a dataset, 1 hour thinking about the question to answer, 
and the rest of the time cleaning up the dataset and implementing the application.

Performing the EDA and deciding between visualization choices took me the most time. 
I needed to think about how to use the graphs and plots to convey meaningful information and answer the questions.
I also spent some time exploring Streamlit and different plotting libraries.
At the beginning I used Matplotlib for visualization, 
but later I switched to Plotly since it includes more interactive features and allows the users to explore the dataset in more interesting ways.
