#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
color = sns.color_palette()

# get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as plt 
import matplotlib.pyplot as plt


# In[ ]:


# Import dataset
order_products_df = pd.read_csv("order_products.csv")
orders_df = pd.read_csv("orders.csv")


# In[ ]:


# Combine Hour of a Day and Day of a Week
group_df= orders_df.groupby(["order_dow", "order_hour_of_day"])["order_number"].count().reset_index()
group_df= group_df.pivot("order_dow", "order_hour_of_day", "order_number")

plt.figure(figsize=(15, 8))
sns.heatmap(group_df, cmap= "gist_heat_r")
plt.yticks([i for i in range(7)], ["Sat.", "Sun.", "Mon.", "Tue.", "Wed.", "Thur.", "Fri."],fontsize= 20)
plt.xlabel ("Hour of a Day", fontsize=20)
plt.ylabel ("Day of a Week", fontsize=20)
plt.xticks(rotation= 90,fontsize=20)
plt.yticks(fontsize=20)
plt.show


# In[ ]:


# How long does next order after prior order?
plt.figure(figsize= (15, 8))
sns.countplot(data= orders_df, x="days_since_prior_order",color= color[0])
plt.ylabel("Count of Order", fontsize= 20)
plt.xlabel("Days", fontsize= 20)
plt.xticks(rotation= 90,fontsize=20)
plt.yticks(fontsize=20)
plt.show()


# In[ ]:


# Days_since_prior_order：
plt.figure(figsize=(15, 8))
sns.countplot(x="days_since_prior_order", data=orders_df, color=color[0])
plt.ylabel("Count", fontsize=12)
plt.xlabel("Days since prior order", fontsize=12)
plt.xticks(rotation= 90,fontsize=20)
plt.yticks(fontsize=20)
plt.show()


# In[ ]:


# Number of orders from one custumor
order_count = orders_df.groupby("user_id")["order_number"].aggregate(np.max).reset_index()
order_count = order_count.order_number.value_counts()
plt.figure(figsize=(15, 8))
sns.barplot(order_count.index, order_count.values, alpha=0.8, color=color[0])
plt.ylabel("Frequency", fontsize=12)
plt.xlabel("Number of Orders", fontsize=12)
plt.xticks(rotation= 90,fontsize=20)
plt.yticks(fontsize=20)
plt.show()


# In[ ]:


# Number of products in one order
grouped_df = order_products_df.groupby("order_id")["add_to_cart_order"].aggregate("max").reset_index()
cnt_srs = grouped_df.add_to_cart_order.value_counts()

plt.figure(figsize=(15,8))
sns.barplot(cnt_srs.index, cnt_srs.values, color=color[0], alpha=0.8)
plt.ylabel('Frequency', fontsize=20)
plt.xlabel('Number of Products in One Order', fontsize=20)
plt.xticks(rotation= 90,fontsize=20)
plt.yticks(fontsize=20)
plt.show()


# In[ ]:


# Redor ratio vs add to cart

reorder_cart_order = order_products_df[['add_to_cart_order','reordered']].groupby('add_to_cart_order').mean().reset_index().rename(columns={'reordered':'reorder_ratio'})
reorder_cart_order = reorder_cart_order[reorder_cart_order['add_to_cart_order']<70]

plt.figure(figsize=(15,8))
sns.lineplot(reorder_cart_order['add_to_cart_order'], reorder_cart_order['reorder_ratio'], alpha=0.8, color=color[0])
plt.ylabel('Reorder Ratio', fontsize=20)
plt.xlabel('Add to Cart Order', fontsize=20)
plt.xticks(rotation=90,fontsize=20)
plt.yticks(fontsize=20)
plt.show()

