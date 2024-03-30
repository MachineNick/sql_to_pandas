#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install mysql.connector


# In[5]:


#connecting pandas to sql server here host will have the value of ip ,localhost if running on your own pc or server other ip for aws
import pandas as pd
import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='',database='demo_')


# In[6]:


#getting values from sql sever
pd.read_sql_query("SELECT * FROM `user_details`",conn)


# In[ ]:




