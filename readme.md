## Project Goals
The goal of this interactive data science application is to explore the video game sales from 1980 to 2016.
It allows the users to examine the trend of video games sales from different perspectives.

Users will be able to answer the question "How are video game sales affected by various factors?"
This question could be divided to several sub-questions: 
Do newer games have higher sales? 
What genre of games have highest sales?
How are the sales and ratings related?
Are the trends of sales similar across different regions?


## Design Decisions

**Dataset Selection**

The dataset I used for this project is from Kaggle [Link](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings).

It contains the data of about 17k games released from 1980 to 2016.
I chose this dataset because it includes data from many different aspects: realease year, ratings, genre, platform, etc.
We need all these factors to analyze the trend of game sales.

For this dataset, I did not perform data deduplication on game names, because there are games that have been released on multiple platforms.
For example, The Last of Us has been released on both PS3 and PS4.

**3D Scatterplot of Video Game Sales in NA, EU and JP**

This plot gives the users an overall impression of the distribution of video game sales in the 3 major regions - NA, EU and JP - from 1980 to 2016.
Each dot in the 3D space represents a game, and the x, y and z axis represent its sales in NA, EU and JP.
The color of the dot represents the year of release of the game.

Users can understand the impact of region on game sales by examining this plot - rotating, zooming in, looking at specific axes, etc. 
By looking at distribution and color of the points, we can have some high level information of how region and release year impact the game sales. 
For example, games that released in the 1980s tend to have higher sales in NA and JP, compared to EU.
I thought about limiting the number of data points on the scatterplot or getting rid of the outliers, 
but I decided to include all the points because I want to show the user the actual full representation of game sales in these regions.

**Bar Chart of Video Game Sales from 1980 to 2016**

The bar chart shows the video game sales from 1980 to 2016.
There are 2 options for the visualization: average sales or total sales.
User could see the trend of sales over the years and compare the trend of sales between different regions.

I decided to include this bar chart because it clearly shows the trend of game sales (both average and sum) over ~30 years.
From the bar chart we can see that the total sale of games have increased a lot, especially at the beginning of the 21st century. 
However, the average sale of each game was much higher in the 1980s and the 1990s.
This poses some interesting research questions for the users to explore.

**2D Scatterplot of Game Sales vs. Ratings**

The 2D scatterplot visualizes video games sales and ratings from 1985 to 2016.
User could select the year of release, rating score type, and sales by region they want to examine.
They can also choose the games of specific platforms.

I added this plot becuase users could get a lot of insights on the game sales by utilizing the interactive features.
Users can select the subset of data they want to examine by chooing the year, score type, platform and region, 
which allows them to analysis and compare the data more easily.
Initially I did not add the platform selection to the plot, but later I realized that platform also played an essential part in game sales.
By adding that to the plot, users could also see and compare the game sales on consoles of different generations.

**2D Scatterplot of Game Sales of Different Genres**

This 2D scatterplot visualizes video games sales of different genres from the 1980s to 2016.
User could select the game genres they want to examine and compare the sales between different genres.

Initially I chose to do a histogram or a bar chart showing the average game sales per year of the different genres.
However, I later decided to do a scatterplot because there are several outliers in the dataset, 
which could heavily influence the average sales and lead to misrepresentation of the data.


## Development Process
I worked solo on this project. 
I spent about 12 hours on this - about 1 hour choosing a dataset, 1 hour thinking about the question to answer, 
2 hours for the writeup and deploymeny, and the rest of the time cleaning up the dataset and implementing the application.

Performing the EDA and deciding between visualization choices took me the most time. 
I needed to think about how to use the graphs and plots to convey meaningful information and answer the questions.
I also spent some time exploring Streamlit and different plotting libraries.
At the beginning I used Matplotlib for visualization, 
but later I switched to Plotly since it includes more interactive features and allows the users to explore the dataset in more interesting ways.
