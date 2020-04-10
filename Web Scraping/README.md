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

**Library purpose**
- **numpy:** allows us to create multi-dimensional arrays
- **pandas:** is used for data manipulation and analysis
- **request:** allows HTML request to function smoothly
- **BeautifulSoup:** allows us to extract and parse HTML and XML Doccuments.
