#This is a demo for github co-pilot showing how it can be used to help create a script that will build a chart from an external websource.
#The comments are prewritten to demonstrate how co-pilot can be used to help write code based on them.

#Import Packages for requesting url, handling data frames and creating charts from data frames
import requests
import pandas as pd
import matplotlib.pyplot as plt


#URL http://open.statswales.gov.wales/en-gb/dataset/HLTH0091
#This is the url for the data set that we will be using to build the chart

url = 'http://open.statswales.gov.wales/en-gb/dataset/HLTH0091'

#Request the url and store the response in a variable called response as JSON
response = requests.get(url).json()

#convert to dictionary
data = dict(response)

#process dictionary into a data frame based on the value column
df = pd.DataFrame(data['value'])

#print the data frame first 5 rows
print(df.head())

#convert Data column to numeric value for plotting
df['Data'] = pd.to_numeric(df['Data'])

#plot the the columns Date_ItemName_ENG as x axis and Data as y axis, and filter Indicator_Hierarchy  by Misc_Admissions_All
df[df['Indicator_Hierarchy'] == 'Misc_Admissions_All'].plot(x='Date_ItemName_ENG', y='Data')

#export the result to a png file
plt.savefig('chart.png')