# This is the sorce code in python
# Proper libraries must be installed

# Import necessary libraries

import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

# Make a HTTP request for the webpage

req = requests.get('https://www.worldometers.info/coronavirus/')

# Parse the raw HTML into a soup

soup = BeautifulSoup(req.content)

# Map the HTML table for "cases by country" into an array of arrays
#
# Map(function, array) -> Essentially applies a function to each element in an array. We use lambda expressions to create functions.

data = list(map(lambda x: list(map(lambda y: y.text, x.select('td, th'))), soup.select('table#main_table_countries_today tr')))

# Turn array of arrays into a Pandas Dataframe
df = pd.DataFrame(data)

# Set the column names to the first row
df.columns = df.iloc[0]

# Delete first row to avoid confusing it as a country
df = df.drop(0, axis=0)

# Lets have a look at the first ten rows, it should match the website table.

df.head(10)

# Finaly, save as a spreadsheet or other file format. It will be in a folder located on the left sidebar.

df.to_csv('covid19.csv')
