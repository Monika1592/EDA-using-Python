#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import create_engine


# In[2]:


engine = create_engine('mysql://username:password@localhost/sakila')


# In[3]:


df=pd.read_sql_table('category_look_up',engine)
df


# In[4]:



get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'mysql://username:password@localhost/sakila')


# In[5]:



get_ipython().run_cell_magic('sql', '', 'show tables')


# In[6]:


get_ipython().run_cell_magic('sql', '', 'select * from category_look_up limit 5')


# In[7]:


get_ipython().run_cell_magic('sql', '', 'select *   from merchant_prices limit 5')


# In[89]:


query = get_ipython().run_line_magic('sql', "SELECT m.Merchant as Merchant,(m.Price) AS Price,m.ID as ID,c.category as cat  from merchant_prices as mleft join category_look_up c on m.Jet_SKU_ID=c.Jet_SKU_IDleft join sales_data as s on s.Jet_SKU_ID=c.Jet_SKU_IDwhere c.Jet_SKU_ID in('J0104','J0014','J0176','J0284','J0336','J0126','J0127','J0209','J0267','','','','')group by Merchant,ID,Price,catorder by c.Jet_SKU_ID asc ;")
check=query.DataFrame()
print(check)


# In[10]:


#q1:overall, how are merchants priced relative to each other


# In[30]:


query = get_ipython().run_line_magic('sql', "SELECT m.Merchant as Merchant,(m.Price) AS Price,m.ID as ID from merchant_prices as mleft join category_look_up c on m.Jet_SKU_ID=c.Jet_SKU_IDwhere Category='Electronics'group by Merchant,ID,Priceorder by m.Merchant")
("")
df=query.DataFrame()
print(df)



# In[44]:


df['Merchant '] = df['Merchant'].astype('object')
df['ID'] = df['ID'].astype('int64')
df['Price'] = df['Price'].astype('float')


# In[45]:


##plt.figure(figsize = (20,10))
sns.relplot(x ='ID', y = 'Price',data = df ,kind='line',hue="Merchant",col="Merchant")
plt.show()


# In[83]:


plt.figure(figsize = (20,10))
Trend = sns.relplot(x ='ID', y = 'Price',kind='scatter', hue="Merchant", data = df ,col='Merchant')


# In[88]:


#Consumables
plt.figure(figsize = (20,10))
Trend = sns.relplot(x ='ID', y = 'Price',kind='scatter', hue="Merchant", data = df1 ,col='Merchant')


# In[85]:


#Home
plt.figure(figsize = (20,10))
Trend = sns.relplot(x ='ID', y = 'Price',kind='scatter', hue="Merchant", data = df2 ,col='Merchant')


# In[41]:


query = get_ipython().run_line_magic('sql', "SELECT m.Merchant,(avg(m.Price)/STDDEV(m.Price)) AS Price from merchant_data as mleft join category_look_up c on m.Jet_SKU_ID=c.Jet_SKU_IDleft join sales_data as s on s.Jet_SKU_ID=c.Jet_SKU_IDwhere Category='Electronics'group by m.Merchantorder by m.Merchant")
("")
query.bar() 


# In[34]:


query = get_ipython().run_line_magic('sql', "SELECT m.Merchant as Merchant,(m.Price) AS Price,m.ID as ID from merchant_prices as mleft join category_look_up c on m.Jet_SKU_ID=c.Jet_SKU_IDleft join sales_data as s on s.Jet_SKU_ID=c.Jet_SKU_IDwhere Category='Consumables'group by Merchant,ID,Priceorder by m.Merchant")
("")
df1=query.DataFrame()
print(df1)


# In[35]:


##plt.figure(figsize = (20,10))
sns.relplot(x ='ID', y = 'Price',data = df1 ,kind='line',hue="Merchant",col="Merchant",ci='sd')
plt.show()


# In[42]:


query = get_ipython().run_line_magic('sql', "SELECT m.Merchant,(avg(m.Price)/STDDEV(m.Price)) AS Price from merchant_data as mleft join category_look_up c on m.Jet_SKU_ID=c.Jet_SKU_IDleft join sales_data as s on s.Jet_SKU_ID=c.Jet_SKU_IDwhere Category='Consumables'group by m.Merchantorder by m.Merchant")
("")
query.bar() 


# In[36]:


query = get_ipython().run_line_magic('sql', "SELECT m.Merchant as Merchant,(m.Price) AS Price,m.ID as ID from merchant_prices as mleft join category_look_up c on m.Jet_SKU_ID=c.Jet_SKU_IDleft join sales_data as s on s.Jet_SKU_ID=c.Jet_SKU_IDwhere Category='Home'group by Merchant,ID,Priceorder by m.Merchant")
("")
df2=query.DataFrame()
print(df2)


# In[37]:


##plt.figure(figsize = (20,10))
sns.relplot(x ='ID', y = 'Price',data = df2 ,kind='line',hue="Merchant",col="Merchant",ci='sd')
plt.show()


# In[43]:


query = get_ipython().run_line_magic('sql', "SELECT m.Merchant,(avg(m.Price)/STDDEV(m.Price)) AS Price from merchant_data as mleft join category_look_up c on m.Jet_SKU_ID=c.Jet_SKU_IDleft join sales_data as s on s.Jet_SKU_ID=c.Jet_SKU_IDwhere Category='Home'group by m.Merchantorder by m.Merchant")
("")
query.bar() 


# In[78]:


query = get_ipython().run_line_magic('sql', "SELECT SUM(A.RANK),A.CATEGORY,A.MERCHANT FROM(SELECT m.Merchant as Merchant,(m.Price) AS Price,m.ID as ID,c.category,DENSE_RANK() OVER (PARTITION BY ID ORDER BY Price DESC) as 'rank' from merchant_prices as mleft join category_look_up c on m.Jet_SKU_ID=c.Jet_SKU_ID)A GROUP BY A.CATEGORY,A.MERCHANT  ")
ana=query.DataFrame()
print(ana)


# In[79]:


query = get_ipython().run_line_magic('sql', "SELECT m.Merchant as Merchant,(m.Price) AS Price,m.ID as ID,c.category,DENSE_RANK() OVER (PARTITION BY ID ORDER BY Price DESC) as 'rank' from merchant_prices as mleft join category_look_up c on m.Jet_SKU_ID=c.Jet_SKU_ID  ")
CHK=query.DataFrame()
print(CHK)


# In[116]:


#Find most competitive and least competitive pricing

query = get_ipython().run_line_magic('sql', 'SELECT A.jet_sku_id FROM(SELECT category, m.jet_sku_id, (max(m.price)-min(m.price))as diff  FROM merchant_prices mleft join category_look_up c on m.jet_sku_id=c.jet_sku_id group by category,m.jet_sku_idorder by diff desc limit 5)A')

abc=query.DataFrame()
print(abc)


# In[115]:


#Questions:
    #1Overall, how are the three merchants prices relative to each other?
    #1 IN Electronics category,Analysis shows that prices of Alexs Store> Leos Bodega> jasmine’s shop
    #  In home category, Alexs Store> Leos Bodega> jasmine’s shop
    #  In Consumables category, Alexs Store> Leos Bodega> jasmine’s shop


# In[ ]:


#Question2:
#Products with most competitive pricing
#0      J0149
1      J0412
2      J0283
3      J0116
4      J0048

#Products with most competitive pricing
#  0      J0284
1      J0336
2      J0104
3      J0176
4      J0014

