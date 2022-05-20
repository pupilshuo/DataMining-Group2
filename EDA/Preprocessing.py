#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Import order_products_prior & order_products_train dataset

order_products_prior_df= pd.read_csv("order_products__prior.csv")
order_products_train_df= pd.read_csv("order_products__train.csv")
products_df=pd.read_csv("products.csv")


# In[3]:


# Merge order_products_prior and order_products_train datasets to order_products

frames=[order_products_prior_df,order_products_train_df]
order_products_df=pd.concat(frames)


# In[4]:


# Checking for null value

order_products_df.isnull().sum()


# In[5]:


# Checking for duplicated value

order_products_df[order_products_df.duplicated()].shape


# In[6]:


# Match 'product_id' in the order_products with 'products_name' in the products

order_products_df = pd.merge(order_products_df, 
                      products_df, 
                      on ='product_id', 
                      how ='left')
order_products_df


# In[11]:


order_products_df.to_csv(r'order_products.csv', index = False)

