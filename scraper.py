#!/usr/bin/env python
# coding: utf-8

# ## Step 0: Imports
# 
# We aren't even going to use pandas for this one! No pip install of anything required.

# In[1]:


import os
import csv

# We'll use these to store the current date as a column
from datetime import datetime
from datetime import date


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


response = requests.get("https://www.tagesanzeiger.ch/")
doc = BeautifulSoup(response.text)


# ## Step 1: Create the file if it doesn't exist

# In[4]:


# The file we want to save
filename = 'top_stories.csv'


# In[5]:


# If it doesn't exist, create it with the column headers
if not os.path.exists(filename):
    print("Creating new", filename)
    with open(filename, 'w') as f:
        f.write("title,url,date\n")


# In[6]:


website = "https://www.tagesanzeiger.ch/"


# ## Step 2: Add the data to the file

# In[7]:


# The info we want to save
top_title = doc.select('.ArticleTeaser_title__tlltn')[0].text #that gets the headline text out of the website
top_url = website + doc.find(class_ = "article-teaser-list").find('a')['href'] #that gets the url out of the webpage

# This is if you want the time. If just the date, use date.today()
today = datetime.now()

# Open up the file in 'append' mode, which adds to the end
with open('top_stories.csv', 'a') as file:
    writer = csv.writer(file)
    # Write a single row to it with the title, url and date
    print("Adding a new line")
    writer.writerow([top_title, top_url, today])


# ## Testing it out
# 
# Keep running the code above to add more lines

# In[8]:


import pandas as pd

pd.read_csv("top_stories.csv")


# ### it's how you're saving the top headline to the end of your CSV file. Right now in your code you're creating a dataframe with all of the stories, but you only really want one story. So instead, grab the top story and use the code I sent you to write the headline (and url?) to the file.6
