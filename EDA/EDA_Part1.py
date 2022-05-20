#!/usr/bin/env python
# coding: utf-8

# import lib


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load the product file
prducts_df = pd.read_csv("products.csv")
aisles_df = pd.read_csv("aisles.csv")
departments = pd.read_csv("departments.csv")
order_products_prior_df = pd.read_csv("order_products__prior.csv")
order_products_train_df = pd.read_csv("order_products__train.csv")
orders_df = pd.read_csv("orders.csv")


# In[7]:



# merge the product dataframe and the


order_products_prior_df = pd.merge(order_products_prior_df
                                   , prducts_df
                                   , on="product_id", how="left")
order_products_prior_df = pd.merge(order_products_prior_df
                              , aisles_df
                              , on="aisle_id"
                              , how="left")
order_products_prior_df = pd.merge(order_products_prior_df
                                   , departments
                                   , on="department_id"
                                   , how = "left"
                                  )





cnt_srs = order_products_prior_df.groupby(by="product_name").count()["add_to_cart_order_mod"].reset_index()
cnt_srs.sort_values(by="add_to_cart_order_mod", ascending=False).head(10)


# In[32]:


#plot the the values of the product with different aisles
cnt_srs = order_products_prior_df.aisle.value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(cnt_srs.head(20).index, cnt_srs.head(20).values
            , alpha=0.5
            , color="blue"
           )

plt.xticks(rotation="90")
plt.ylabel("Count")
plt.xlabel("Aisle name")
plt.show()




temp = order_products_prior_df.department.value_counts()




plt.figure(figsize=(7, 7))
plt.pie(temp
        , labels=temp.index
        , autopct="%1.1f%%"
        , startangle=200
       )
plt.show()


# In[17]:


group_df = order_products_prior_df.groupby("department")["reordered"].mean()
group_df = group_df.reset_index()
group_df.head()


# plot the values of reorder with different department


plt.figure(figsize=(12, 5))
sns.barplot(group_df.department
            , group_df.reordered
            , alpha=0.8
            , color="blue")

plt.ylabel("reordered ratio", fontsize=12)
plt.title("The reordered ratio in differfent departments", fontsize=13)
plt.xlabel("department", fontsize=12)
plt.xticks(rotation=90)
plt.show()




group_df = order_products_prior_df.groupby(["department_id", "aisle"])["reordered"].mean()
group_df = group_df.reset_index()


# plot the values of reorder with different department id


fig, ax = plt.subplots(figsize=(14, 14))
ax.scatter(group_df.reordered, group_df.department_id, alpha=0.8, color="red")
plt.plot([0.6]*23, np.arange(0, 23), color="red", linestyle="--")

for i, txt in enumerate(group_df.aisle.values):
    ax.annotate(txt, (group_df.reordered[i], group_df.department_id[i])
                , rotation=45
                , color="green"
               )
    plt.xlabel("reordered ratio", fontsize=14)

plt.ylabel("department", fontsize=14)
plt.title("Reorder ration of different aisles", fontsize=20)
plt.yticks(np.arange(1, 22), departments.department)
plt.ylim([0, 22])
plt.xlim([0, 0.9])
plt.grid()
plt.show()

