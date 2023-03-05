# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 03:19:52 2023

@author: AAA
"""

import pandas as pd
import matplotlib.pyplot as plt

# Create the data frame
data = {'year': [2017, 2018, 2019, 2020, 2021],
        'Belgium': [44198, 47549, 46599, 45189, 51768],
        'France': [38781, 41593, 40579, 39037, 43519],
        'Germany': [44653, 47974, 46795, 46253, 50802],
        'Italy': [32407, 34622, 33673, 31835, 35551],
        'Poland': [13865, 15468, 15732, 15742, 17841],
        'Spain': [28170, 30365, 29554, 27056, 30116]}

df = pd.DataFrame(data)

# read files into dataframe and print
df_countries = pd.read_csv('GDP_per_capita_table.csv')
print(df_countries)

# set the title, x-label, and y-label
plt.figure(figsize=(10,6))
plt.plot(df_countries['year'], df_countries['Belgium'], label='Belgium')
plt.plot(df_countries['year'], df_countries['France'], label='France')
plt.plot(df_countries['year'], df_countries['Germany'], label='Germany')
plt.plot(df_countries['year'], df_countries['Italy'], label='Italy')
plt.plot(df_countries['year'], df_countries['Poland'], label='Poland')
plt.plot(df_countries['year'], df_countries['Spain'], label='Spain')
# set the title, x-label, and y-label
plt.title('GDP of European Countries')
plt.xlabel('Year')
plt.ylabel('GDP (in millions)')

# set the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# display the plot
plt.show()


# produce bar chat
ax = df_countries.plot(x='year', kind='bar', stacked=True)

# Set the x label and y label
ax.set_xlabel('Year')
ax.set_ylabel('GDP')

# Set the title
ax.set_title('GDP by country and year')

# Set the legend outside the plot
ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

# Show the plot
plt.show()




# data for the table
data = {
    'Belgium': [44198, 47549, 46599, 45189, 51768],
    'France': [38781, 41593, 40579, 39037, 43519],
    'Germany': [44653, 47974, 46795, 46253, 50802],
    'Italy': [32407, 34622, 33673, 31835, 35551],
    'Poland': [13865, 15468, 15732, 15742, 17841],
    'Spain': [28170, 30365, 29554, 27056, 30116]
}

# calculate the total GDP for each country
gdp_totals = {}
for country, gdp_data in data.items():
    gdp_totals[country] = sum(gdp_data)

# find the country with the highest GDP
highest_gdp_country = max(gdp_totals, key=gdp_totals.get)

# plot a pie chart of the GDP of each country
labels = gdp_totals.keys()
sizes = gdp_totals.values()
explode = [0.1 if country == highest_gdp_country else 0 for country in labels]

plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True)
plt.axis('equal')
plt.title('GDP by Country')
plt.show()






