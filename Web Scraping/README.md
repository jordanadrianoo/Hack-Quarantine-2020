# Web Scraping with Python

In this repository we will look at the essentials and fundamentals of web scraping. This web scraper will be created within the Python Jupyter Notebook IDE and use **numpy**, **pandas**, **request**, and **BeautifulSoup** libraries. It is possible to use a standard Python IDE with proper preparations, but for this repository it is advised to use the online Colab provided below for it includes the essential libraries. Credit and video belongs to Wyatt Phillips. Here is a video link to the [full tutorial](https://www.youtube.com/watch?v=Ssi1A8FAAFI) on youtube!

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

in the first cell we will begin to import the essential libraries needed.
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
- **BeautifulSoup:** allows us to extract and parse HTML and XML Documents.

## Requesting from website 

Next, we must tell our python what web page we will be using. In our example, we will be using [World-O-Meter](https://www.worldometers.info/coronavirus/) as a source of information.

```
req = requests.get('https://www.worldometers.info/coronavirus/')
```

we set a variable named **req** that will use request and store the HTML source returned from the website we provided.

In a new cell, ***type***

```
soup = BeautifulSoup(req.content)
```

this will also set a variable named **soup** that will parase the content within **req**.

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/parsing%20HTML.JPG)

## Extracting Data from Website

When developing a Web Scraper it is important to understand how HTML is containing its data. When visiting a variety of websites it is crucial to see the patterns that data is stored within HTML. For this web crawler we will extracting all the data from [World-O-Meter's](https://www.worldometers.info/coronavirus/) data table. A clear pattern can be seen within the rows and columns.

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/data%20table.JPG)

***note:*** *data will be different from the time this repository was made.* 

Next, we will inspect how the table is being used in HTML. We can do this by selecting a country in the first column and **right click** on the mouse and selecting **Inspect Element**

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/data%20table%20Inspect%20Element.JPG)

The Inspect Element is is an important developer’s tool that can provide live feedback. We are currently trying to find the data tables ID. If we scroll up slowly we should be able to find where the tables ID is called.

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/data%20table%20ID.JPG)

As you can see, the tables ID is called **"main_table_countries_today"**. Now that we know the tables ID we can ***press*** <**Ctrl+F**> to search through the HTML document. In the search box we will ***type***

```
table# main_table_countries_today
```

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/data%20table%20find%20ID.JPG)

We are searching the entire HTML document for the table ID but we will add **tr** to return each element within the table. 

 ```
table# main_table_countries_today tr
```

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/Table%20Elements.JPG)

now that we can confirm that these are the elements within the table we can tell python what to extract from the HTML document.

Back in your Notebook we will use this information to create a new cell to parse the information. ***Disclaimer:*** *This section can be very challenging to read at first*. 

```
data = list(map(lambda x: list(map(lambda y: y.text, x.select('td, th'))), soup.select('table#main_table_countries_today tr')))
```

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/Parsing%20the%20table.JPG)

This extremely difficult part can be fully explained using this [video source](http://www.youtube.com/watch?v=Ssi1A8FAAFI&t=16m25s). This video will start in the middle explaining how to find pattern recognition and how this parsing line of code works. 

# Formatting with Panda's dataframe

It is important to make sure that all the information we extract is displayed in a clean easy to read format.

Thus, in a new cell we will ***type***

```
df = pd.DataFrame(data)
```

This will transfer the content from data and parse it into the panda dataframe.

in the same cell ***type***

```
df.columns = df.iloc[0]
```
This second part of code will set the first list of arrays as the title. 

again, in the same cell ***type***

```
df = df.drop(0, axis=0)
```

This third line will delete the first list to avoid duplications

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/formating.JPG)

when this cell is run without errors we have formatted all of the data into pandas dataframe and is ready to be displayed by simply calling it into a new cell.

```
df
```
![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/Our%20Data%20Table.JPG)

**congratulations!** You have successfully extracted and displayed the information from the website provided.

## Exporting as CVS file

What can we do with this information though? Thank you for asking! we can export this information into a **CVS** file. CVS files can be used for a wide arrangement of data structures or statistics. ***type***

```
df.to_csv('covid19.csv')
```

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/Export%20to%20CSV.JPG)

This will export the data table as a CVS and save within the google drive. Location to download locally is found under the table of content.

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/CSV%20location.JPG)

Once downloaded locally, you can **open** the file in **Microsoft Excel**. 

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Web%20Scraper%20Images/Excel%20Spread%20Sheet.JPG)

With the foundation of web scraping there is a lot of information you can extract and conclude. Try using different websites and see what you can scrape together!

# sources

- [Wyatt Phillips full tutorial](https://www.youtube.com/watch?v=Ssi1A8FAAFI)
- [Wyatt Phillips powerpoint](https://docs.google.com/presentation/d/1zHwfvTlk9vXFhiDdJSeFzasBZgwor1xM1wTiQH_qRDY/edit#slide=id.g720c73f8d4_0_136)
- [Colab](https://colab.research.google.com/drive/1KGh5r59YJuNRCR3JRhJCJojgt9vR8IUW#scrollTo=7RyOhSZaiM7R)
- [Worldometer](https://www.worldometers.info/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Xpath Cheatsheet](https://devhints.io/xpath)
- [Panda's Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)
