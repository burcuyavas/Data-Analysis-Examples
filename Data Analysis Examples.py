#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Data Visualization Example


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[6]:


plt.plot(5, 5, 'o')
plt.ylabel('Y')
plt.xlabel('X')
plt.title('Plotting Example')
plt.show()


# In[21]:


import numpy as np  
import pandas as pd 
get_ipython().system('conda install -c anaconda xlrd --yes')


# In[22]:


df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe')


# In[23]:


df_can.head()


# In[24]:


df_can.tail()


# In[25]:


df_can.info()


# In[26]:


df_can.columns.values 


# In[27]:


df_can.index.values


# In[28]:


print(type(df_can.columns))
print(type(df_can.index))


# In[29]:


df_can.columns.tolist()
df_can.index.tolist()

print (type(df_can.columns.tolist()))
print (type(df_can.index.tolist()))


# In[31]:


df_can.shape # size of dataframe (rows, columns) 


# In[32]:


df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)


# In[33]:


df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns


# In[34]:


df_can['Total'] = df_can.sum(axis=1)


# In[35]:


df_can.isnull().sum()


# In[36]:


df_can.describe()


# In[37]:


df_can.Country 


# In[38]:


df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]


# In[44]:


print(df_can.loc['Japan'])
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())


# In[54]:


import numpy as np  
import pandas as pd 
from PIL import Image 


# In[55]:


get_ipython().system('conda install -c anaconda xlrd --yes')


# In[56]:


df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print('Data downloaded and read into a dataframe!')


# In[57]:


df_can.head()


# In[58]:


print(df_can.shape)


# In[59]:


df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis = 1, inplace = True)

df_can.rename (columns = {'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace = True)

df_can.columns = list(map(str, df_can.columns))

df_can.set_index('Country', inplace = True)

df_can['Total'] =  df_can.sum (axis = 1)

years = list(map(str, range(1980, 2014)))
print ('data dimensions:', df_can.shape)


# In[60]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches # needed for waffle Charts

mpl.style.use('ggplot') 

print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0


# In[61]:


df_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden'], :]
df_dsn


# In[62]:


total_values = sum(df_dsn['Total'])
category_proportions = [(float(value) / total_values) for value in df_dsn['Total']]

for i, proportion in enumerate(category_proportions):
    print (df_dsn.index.values[i] + ': ' + str(proportion))


# In[63]:


width = 40 
height = 10 

total_num_tiles = width * height 

print ('Total number of tiles is ', total_num_tiles)


# In[ ]:




