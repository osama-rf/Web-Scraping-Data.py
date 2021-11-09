#!/usr/bin/env python
# coding: utf-8

# ### Importing Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()


# In[ ]:





# ==========

# ##### Importing Libraries & Methods

# In[ ]:


# BeautifulSoup is a Python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup as bs

# urllib.request for opening and reading URLs
from urllib.request import urlopen


# In[ ]:





# ##### Inputting the URL

# In[ ]:


# Getting the website page address
url = 'https://wuzzuf.net/search/jobs/?a=navbl%7Cspbl&q=illustrator'


# In[ ]:





# ##### Create a Client-based Request to Get the URL

# In[ ]:


client = urlopen(url)


# In[ ]:





# ##### Getting the HTML Code of the Full Page

# In[ ]:


html = client.read()
print(html)


# In[ ]:





# ##### Closing the Request

# In[ ]:


client.close()


# In[ ]:





# ##### Creating an HTML Parser Using BeautifulSoup

# In[ ]:


soup = bs(html, "html.parser")


# In[ ]:


# Now we have a well-prepared html code
soup


# In[ ]:





# ##### Creating a Container for the Needed Data

# In[ ]:


containers = soup.find_all("div", {"class" : "css-qa8nz1-Card e1v1l3u10"})


# In[ ]:


len(containers)


# In[ ]:


print(bs.prettify(containers[0]))


# In[ ]:





# ##### Accessing Page Elements

# In[ ]:


# Let's check how to access a specific element in the page (i.e. the job title)
containers[0].div.h2.text


# In[ ]:


# Here is the best practice (better way) for accessing the job title
job_title = containers[0].findAll("h2", {"class": "css-m604qf"})
job_title[0].text


# In[ ]:


company_name = containers[0].findAll("a", {"class": "css-17s97q8"})
company_name[0].text


# In[ ]:


job_type = containers[0].findAll("a", {"class": "css-n2jc4m"})
job_type[0].text


# In[ ]:





# ##### Bringing it All Together

# In[ ]:


# We need to create a file to save our new data to it
f = open('data/wuzzuf.csv','w')
headers = "Job_Ttile, Company_Name, Job_Type\n"
f.write(headers)

# Now we will get ALL the needed data from the web page
for container in containers:
    jtitle = container.findAll("h2", {"class": "css-m604qf"})
    job_title = jtitle[0].text.strip()
    
    cname = container.findAll("a", {"class": "css-17s97q8"})
    company_name = cname[0].text.strip()
    
    jtype = container.findAll("a", {"class": "css-n2jc4m"})
    job_type = jtype[0].text.strip()
    
#     print(job_title)
#     print(company_name)
#     print(job_type)
#     print()
    
    print(job_title + ", " + company_name + ", " + job_type)
    f.write(job_title + ", " + company_name + ", " + job_type + "\n")

f.close()


# In[ ]:




