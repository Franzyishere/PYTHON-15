#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("data bank.csv")

# histogram of total_bills 
plt.hist(data['education'])

plt.title("Histogram")

# Adding the Legends 
plt.show()


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data bank.csv")
job = ['admin', 'uknown', 'housemaid', 'unemployed']
duration = [1042, 323, 4242, 424]
plt.pie(duration, labels=job)
plt.title("pie chart")
plt.show()


# In[3]:


import pandas as pd 
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("data bank.csv")

# Scatter plot with day against tip 
plt.plot(data['balance']) 
plt.plot(data['day'])

# Adding Title to the Plot 
plt.title("Scatter Plot")

# Setting the X and Y Labels 
plt.xlabel('balance')
plt.ylabel('day')

plt.show()


# In[4]:


import pandas as pd 
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("data bank.csv")

# Scatter plot with day against tip 
plt.scatter(data['marital'], data['balance'], c=data['day'], 
            s=data['campaign'])

# Adding Title to the Plot 
plt.title("Scatter Plot")

# Setting the X and Y Labels
plt.xlabel('marital')
plt.ylabel('age')

plt.colorbar()

plt.show()


# In[5]:


import pandas as pd

# reading the database
data=pd.read_csv("data bank.csv")

# printing the top 10 rows
display(data.head(10))


# In[ ]:




