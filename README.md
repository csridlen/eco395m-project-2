# Airbnb Price Prediction

Final Python Project 

Team: Violet-2

Team Members: 

[Fjollë Gjonbalaj](https://github.com/Fjolle)

[Brendan Ok](https://github.com/brendanok)

[Abby Johnson](https://github.com/johnsonabigail)

[Victor Besse](https://github.com/Victor-Besse)

[Christina Ridlen](https://github.com/csridlen)

[Steven Kim](https://github.com/su1214)

## Introduction

We use a combination of explanatory data analysis, model prediction and machine learning to predict Airbnb rental prices based on 17 key variables including room type and neighbourhood group. We build trained models, including a linear regression and a lasso regression. We compare the performance of models based on the RMSE (the standard deviation of the residuals/prediction errors). 

## Data Collection

The main source of data contains Airbnb data for the city of New York for the year 2021. The data was made available by [Inside Airbnb](http://insideairbnb.com/get-the-data/) and can be found on our [data folder of our repo](https://raw.githubusercontent.com/csridlen/eco395m-project-2/main/data/airbnb_listings_2021.csv).

We also used data published by New York City's various institutions including locations of [subway stations](https://data.cityofnewyork.us/Transportation/Subway-Stations/arq3-7z49) and [parks](https://data.cityofnewyork.us/City-Government/ARCHIVED-Parks-Zones/rjaj-zgq7) as well as neighboorhood areas.

### Data Summary
We did some preliminary analysis and visualizations in order to better understand our data. Below you can see some of those results:

We created a violin plot to showcase density and distribtuion of prices in different New York City neighbourhoods. We remove extreme values from the price variable by limiting this analysis on prices less than $250. It is clear from the plot that Manhattan has the highest average airbnb price among neighbourhood groups. 

![Plot 1](artifacts/violinplot.png)

We also show top 5 neighbourhoods by room type based on calculated host listings. It is possible that hosts with more listings charge higher prices. This might be an indicator that more experienced hosts know the market better. This plot shows that Bedford-Stuyvesant has the highest calculated host listings, so we would expect to see higher prices in this neighbourhood group compared to other neighbourhood groups. Further, private rooms have more host listings than entire home/apt in all instances except for Hell's Kitchen. 

![Plot 2](artifacts/barplot.png)

We also created a boxplot showing airbnb prices for each neighborhood group based on room type. We can see from the boxplot that Manhattan has the highest airbnb prices among neighbourhood, followed by Brooklyn and Queens. In all instances, entire home/apartments are more expensive than private rooms and shared rooms. 

![Plot 3](artifacts/boxplot.png)

The heatmap below shows airbnb prices in New York City based on latitute and longitude. 

![Plot 4](artifacts/heatmap1.png)

The second heatmap shows each major neighbourhood group in New York City based on latitute and longitude. 

![Plot 5](artifacts/heatmap2.png)
 
### Data Limitations

### Data Extensions

## Preliminary Analysis: Summary Statistics

## Average prices by neighborhood
An issue that we found initially is that the neighborhoods as defined in the Inside Airbnb dataset isn't consistent with the neighborhoods as reported to the Decennial Census and American Community Survey. So we recoded the neighborhoods to the [updated neighborhoods](https://data.cityofnewyork.us/City-Government/2020-Neighborhood-Tabulation-Areas-NTAs-Tabular/9nt8-h7nd) found through the NYC OpenData portal. 

The updated neighborhoods divide up the city into smaller and more groups. Below is a map of average Airbnb Prices grouped by neighborhoods.

![Plot 1](artifacts/neighbourhood_price_2021_1.png) ![Plot 2](artifacts/neighbourhood_price_2021_2.png)

Refer to [here](https://htmlpreview.github.io/?https://github.com/csridlen/eco395m-project-2/blob/main/artifacts/neighbourhood_price_2021_2.html) to see an interative plot with actual prices per neighborhood.

### Subway station and park zones
We decided to use proximity to subway stations and parks as a predictor in Airbnb prices. For each Airbnb listing, we calculated the distance to the nearest subway and park. We calculated distance using the Manhattan distance formula (Also known as taxicab geomery and named after the borough of course). This distance calculation is different from a traditional distance formula as it's the distance that would be used to for an individual that might drive or walk to a destination rather than distance that would cut through lots and buildings.

Plots below show the distance to the nearest [park](https://htmlpreview.github.io/?https://github.com/csridlen/eco395m-project-2/blob/main/artifacts/nearest_park2.html) and [station](https://htmlpreview.github.io/?https://github.com/csridlen/eco395m-project-2/blob/main/artifacts/nearest_station_2.html). 

![Plot 3](artifacts/nearest_park2.png) ![Plot 4](artifacts/nearest_station_2.png)

## #Data Dictionary 

[airbnb_listings_2021](https://raw.githubusercontent.com/csridlen/eco395m-project-2/main/data/airbnb_listings_2021.csv)


## Database

## Dashboard Creation

## Methodology


### Data Cleaning Process

## Analysis/Findings

## Conclusions

## Reproducability Instructions

## Extensions and Limitations

## Appendix





http://insideairbnb.com/get-the-data/
https://www.kaggle.com/datasets/kritikseth/us-airbnb-open-data
- https://github.com/kytola/CleanAirbnb
- https://github.com/edkrueger/eco395m/blob/final-project/projects/final-project.md
- https://wherebnb.herokuapp.com/
- https://github.com/kritikseth/wherebnb

housing data set: https://data.cityofnewyork.us/City-Government/NYC-Citywide-Annualized-Calendar-Sales-Update/w2pb-icbu
