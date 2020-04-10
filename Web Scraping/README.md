# Web Scraping with Python

In this repository we will look at the essientials and fundamentals of web scraping. This web scraper will be created within the Python Jupyter Notebook IDE and use **numpy**, **pandas**, **request**, and **BeautifulSoup** libraries. It is possible to use a standard Python IDE with proper preperations, but For this repository it is advised to use the online Colab provided below for it includes the essiential libraries. 

## Colab Setup

This Colab is an online Jupyter Notebook that allows the uses google drive to run or create code without having to install the full Jupyter's Full IDE. 

**Note:** *you must be logged into google*

[Colab](https://colab.research.google.com/drive/1KGh5r59YJuNRCR3JRhJCJojgt9vR8IUW#scrollTo=7RyOhSZaiM7R): Link to the Colab we will be using throughout the Web Scraping.


![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/Colab%20demo.JPG)

Your colab should look like this. This colab document will be used as a guide to ensure all code is typed and formatted correctly. It will also track and provide essential links. 

## Colab Web Scraping from scratch

we will need to open up a new Jupyter Notebook. Expand **File** and select **New Notebook**.

![image](https://github.com/jordanadrianoo/Hack-Quarantine-2020/blob/master/Repository%20Images/Web%20Scraper%20Images/Colab%20New%20Notebook%20demo.JPG?raw=true)

Once a blank document is opened in a new tab we can begin to populate it with code!

## Importing Libraries

in the first cell we will begin to import the essential librarys needed.
```
import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup
```
once finished typing, ***Press*** <**shift + enter**> to run current cell and create a new cell. If no errors are shown the partition code is running perfectly.

<img src="https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/Import%20Libraries%20Demo.JPG">

**Libraries purposes-**
- **numpy:** allows us to create multi-dimensional arrays
- **pandas:** is used for data manipulation and analysis
- **request:** allows HTML request to function smoothly
- **BeautifulSoup:** allows us to extract and parse HTML and XML Doccuments.

## Requesting from website 

Next, we must tell our python what web page we will be using. In our example, we will be using [World-O-Meter](https://www.worldometers.info/coronavirus/) as a source of information.

```
req = requests.get('https://www.worldometers.info/coronavirus/')
```

we set a variable named **req** that will use request and store the HTML source returned from the website we provided.

In a new cell, type

```
soup = BeautifulSoup(req.content)
```

this will also set a varible named **soup** that will parase the content within **req**.

## Extractin Data from Website

When developing a Web Scraper it is important to understand how HTML is containing its data. When visiting a variety of websites it is crucial to see the patterns that data is stored within HTML. For this web crawler we will extracting all the data from [World-O-Meter's](https://www.worldometers.info/coronavirus/) data table. A clear pattern can be seen within the rows and columns.

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/data%20table.JPG)

***note:*** *data will be different from the time this repository was made. 

Next, we will inspect how the table is being used in HTML. We can do this by selecting a country in the first column and **right click** on the mouse and selecting **Inspect Element**



