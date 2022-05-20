#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


orders_df = pd.read_csv("orders.csv")
orders_df


# In[4]:


orders_df = orders_df[~ orders_df['eval_set'].str.contains('test')]
orders_df


# In[5]:


department_df = pd.read_csv("departments.csv")
product_df = pd.read_csv("products.csv")
aisle_df = pd.read_csv("aisles.csv")


# In[6]:


order_product_df = pd.read_csv("order_products.csv")


# In[7]:


#Filter out Saturday morning afternoon and evening orders data

orders_sat_df = orders_df[orders_df['order_dow'] == 0]
orders_satA_df = orders_sat_df.loc[orders_sat_df['order_hour_of_day']  <=5]
orders_satB_df = orders_sat_df.loc[(orders_sat_df.order_hour_of_day <=11) & (orders_sat_df.order_hour_of_day >=6)]
orders_satC_df = orders_sat_df.loc[(orders_sat_df.order_hour_of_day <=17) & (orders_sat_df.order_hour_of_day >=12)]
orders_satD_df = orders_sat_df.loc[(orders_sat_df.order_hour_of_day <=23) & (orders_sat_df.order_hour_of_day >=18)]


# In[8]:


#Saturday afternoon: match order_product department aisle
orders_satC_df = pd.merge(orders_satC_df, 
                      order_product_df, 
                      on ='order_id', 
                      how ='left')


# In[9]:


orders_satC_df = pd.merge(orders_satC_df, 
                      department_df, 
                      on ='department_id', 
                      how ='left')


# In[10]:


orders_satC_df = pd.merge(orders_satC_df, 
                      aisle_df, 
                      on ='aisle_id', 
                      how ='left')


# In[11]:


orders_satC_df


# In[12]:


orders_satC_df.to_csv(r'orders_satC.csv', index = False)


# In[13]:


#Saturday night: match order_product department aisle
orders_satD_df = pd.merge(orders_satD_df, 
                      order_product_df, 
                      on ='order_id', 
                      how ='left')


# In[14]:


orders_satD_df = pd.merge(orders_satD_df, 
                      department_df, 
                      on ='department_id', 
                      how ='left')


# In[15]:


orders_satD_df = pd.merge(orders_satD_df, 
                      aisle_df, 
                      on ='aisle_id', 
                      how ='left')
orders_satD_df


# In[16]:


orders_satD_df.to_csv(r'orders_satD.csv', index = False)


# In[17]:


orders_sun_df = orders_df[orders_df['order_dow'] == 1]
orders_sunA_df = orders_sun_df.loc[orders_sun_df['order_hour_of_day']  <=5]
orders_sunB_df = orders_sun_df.loc[(orders_sun_df.order_hour_of_day <=11) & (orders_sun_df.order_hour_of_day >=6)]
orders_sunC_df = orders_sun_df.loc[(orders_sun_df.order_hour_of_day <=17) & (orders_sun_df.order_hour_of_day >=12)]
orders_sunD_df = orders_sun_df.loc[(orders_sun_df.order_hour_of_day <=23) & (orders_sun_df.order_hour_of_day >=18)]


# In[18]:


orders_sun_df 


# In[19]:


#Sunday morning: match order_product department aisle
orders_sunA_df = pd.merge(orders_sunA_df, 
                      order_product_df, 
                      on ='order_id', 
                      how ='left')


# In[20]:


orders_sunA_df = pd.merge(orders_sunA_df, 
                      department_df, 
                      on ='department_id', 
                      how ='left')


# In[21]:


orders_sunA_df = pd.merge(orders_sunA_df, 
                      aisle_df, 
                      on ='aisle_id', 
                      how ='left')


# In[22]:


orders_sunA_df


# In[23]:


orders_sunA_df.to_csv(r'orders_sunA.csv', index = False)


# In[24]:


#Sunday morning: match order_product department aisle
orders_sunB_df = pd.merge(orders_sunB_df, 
                      order_product_df, 
                      on ='order_id', 
                      how ='left')


# In[25]:


orders_sunB_df = pd.merge(orders_sunB_df, 
                      department_df, 
                      on ='department_id', 
                      how ='left')


# In[26]:


orders_sunB_df = pd.merge(orders_sunB_df, 
                      aisle_df, 
                      on ='aisle_id', 
                      how ='left')


# In[27]:


orders_sunB_df.to_csv(r'orders_sunB.csv', index = False)


# In[28]:


#Sunday afternoon: match order_product department aisle
orders_sunC_df = pd.merge(orders_sunC_df, 
                      order_product_df, 
                      on ='order_id', 
                      how ='left')


# In[29]:


orders_sunC_df = pd.merge(orders_sunC_df, 
                      department_df, 
                      on ='department_id', 
                      how ='left')


# In[30]:


orders_sunC_df = pd.merge(orders_sunC_df, 
                      aisle_df, 
                      on ='aisle_id', 
                      how ='left')


# In[31]:


orders_sunC_df.to_csv(r'orders_sunC.csv', index = False)


# In[32]:


#Sunday night: match order_product department aisle
orders_sunD_df = pd.merge(orders_sunD_df, 
                      order_product_df, 
                      on ='order_id', 
                      how ='left')


# In[33]:


orders_sunD_df = pd.merge(orders_sunD_df, 
                      department_df, 
                      on ='department_id', 
                      how ='left')


# In[34]:


orders_sunD_df = pd.merge(orders_sunD_df, 
                      aisle_df, 
                      on ='aisle_id', 
                      how ='left')


# In[35]:


orders_sunD_df


# In[36]:


orders_sunD_df.to_csv(r'orders_sunD.csv', index = False)


# In[ ]:




