#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
car = pd.read_csv(r"C:\Users\91630\Downloads\car dataset.csv")
car.head()


# In[33]:


car.shape


# ( For Data Cleaning ) Find all Null Values in the dataset. If there is any null value in any column, then fill it with the mean of that column.

# In[31]:


car.isnull().sum()


# In[15]:


#Dropping All the null values
car = car.dropna(subset=['EngineSize' ,'Cylinders','Horsepower','MPG_City',
                         'MPG_Highway','Weight','Wheelbase','Length'])
car = car.dropna(subset=['Make', 'Model', 'Type', 'DriveTrain', 'MSRP', 'Invoice'])


# Check what are the different types of Make are there in our dataset. And, what is the count (occurrence) of each Make in the data

# In[16]:


# Count occurrences of each Make
make_counts = car['Make'].value_counts()


# Show all the records where Origin is Asia or Europe ( Filtering )

# In[32]:


# Filter data for cars from Asia or Europe
asia_europe_cars = car[car['Origin'].isin(['Asia', 'Europe'])]
asia_europe_cars.shape


# CALCULATE THE AVERAGE MSRP OF EACH MAKER

# In[18]:


# Calculate average MSRP of each Make
# Remove , and $ symbols from MSRP column
car['MSRP'] = car['MSRP'].str.replace(',', '').str.replace('$', '').astype(float)
make_avg_msrp = car.groupby('Make')['MSRP'].mean().sort_values(ascending=False)


# In[29]:


# Display results using charts
fig, axs = plt.subplots(1, 3, figsize=(12, 5))


# In[30]:


# Bar chart for Make counts
plt.bar(make_counts.index, make_counts.values)
plt.xticks(rotation=90)
plt.title('Make Counts')
plt.xlabel('Makers')
plt.ylabel('Count')
plt.show()

# Pie chart for Asia/Europe cars
asia_europe_counts = asia_europe_cars['Origin'].value_counts()
plt.pie(asia_europe_counts.values, labels=asia_europe_counts.index, autopct='%1.1f%%')
plt.title('Asia/Europe Cars')
plt.legend(title='Origin', loc='upper right')
plt.show()

# Horizontal bar chart for Make average MSRP
fig = plt.figure(figsize=(10,8))
plt.barh(make_avg_msrp.index, make_avg_msrp.values)
plt.title('Make Average MSRP')
plt.xlabel('MSRP')
plt.ylabel('Make')
plt.show()


# In[ ]:




