
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


get_ipython().run_cell_magic('bash', '', 'wget http://api.bitcoincharts.com/v1/csv/coinbaseUSD.csv.gz')


# In[3]:


get_ipython().run_cell_magic('bash', '', 'gunzip coinbaseUSD.csv.gz')


# In[4]:


get_ipython().run_cell_magic('bash', '', 'ls')


# In[5]:


get_ipython().run_cell_magic('bash', '', 'tail -n 10000 coinbaseUSD.csv >> coinbaseUSD-last10k.csv')


# In[6]:


with open('coinbaseUSD-last10k.csv', 'r') as f:
    rows = csv.reader(f)
    unix_times    = []
    last_prices    = []
    trade_volumes = []
    for row in rows:
        unix_time    = int(row[0])
        last_price   = float(row[1])
        trade_volume = float(row[2])    
        unix_times.append(unix_time)
        last_prices.append(last_price)
        trade_volumes.append(trade_volume)


# In[7]:


df = pd.DataFrame({'T': unix_times,
                   'P':last_prices,
                   'V':trade_volumes})


# In[8]:


df


# In[9]:


df.describe()


# In[10]:


df['T']


# In[11]:


df.loc[7:12]


# In[12]:


#Compute the VWAP(Volume Weighted Average Price) of last 10k trades
# VWAP = sum((price)(volume)/sum(volume))
PV = df['P']*df['V']
df2 = pd.DataFrame({'T': unix_times,
                   'P':last_prices,
                   'V':trade_volumes,
                   'PV': df['P']*df['V'] })


# In[13]:


df3 = df2.groupby(['T']).sum() 


# In[14]:


df3.head()


# In[15]:


df4 = df3['PV']/df3['V']


# In[16]:


df4.head()


# In[17]:


df4.tail(100)


# In[18]:


df4.plot()

