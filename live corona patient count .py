#!/usr/bin/env python
# coding: utf-8

# In[1]:


#SOUP

import requests
from bs4 import BeautifulSoup

url= "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
data = s.find_all("div",class_ = "maincounter-number")

print("Total Cases :",data[0].text.strip())
print("Total Deaths:",data[1].text.strip())
print("Total Recoverd:",data[2].text.strip())


# In[ ]:




