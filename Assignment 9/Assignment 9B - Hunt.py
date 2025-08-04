##################################
### Created: August 3, 2025
### Author: Devin Hunt
### DS510 Assignment 9 Part B
### Description: Manipulate CSV file like prior assingment but us pandas instead
### Inputs: User input of a string
### Packages: string
### Output: console output
### References: 
##################################

import pandas as pd
from pandas import Series, DataFrame

weather = pd.read_csv("weather.csv")

#delete first column
del weather["Unnamed: 0"]

#low_wind should be renamed in the output as gust_wind
weather.rename(columns={'low_wind': 'gust_wind'}, inplace=True)

# replace gust_wind NaN with high_wind
weather["gust_wind"][weather.gust_wind != weather.gust_wind] = weather["high_wind"]

# replace precip values of T with 0.001
weather["precip"][weather.precip == "T"] = "0.001"

#write file to output csv file
weather.to_csv("out.csv")

