# Introduction
The whole code files have been compiled in Python 3.
the following is a short description of these python files.In the Algorithm folder,the codes in this folder mainly contribute to processing the
whole datasets,but we also split the data into Saturday and Sunday dataset to analyze more information about the dataset.
# The structure of  folder of file
The following is the structure of our data \
-Algorithm \
&emsp;&emsp;-- FP_Growth\
&emsp;&emsp;--Apriori-Fast\
&emsp;&emsp;--Apriori-Slow\
&emsp;&emsp;--Eclat\
&emsp;&emsp;--Tree-projection\
-EDA\
&emsp;&emsp;--EDA\
&emsp;&emsp;--merge_data\
&emsp;&emsp;--preprocessing \
-Dataset \
&emsp;&emsp;--weekends 

# Code Description
The folder of EDA --- This folder is the main part of the EDA code part.It plots the figures of the relationship 
between the reorder product, aisles and department.The ExtractWeekendData.py extract the weekend data information to explore the relationship between departments, aisles and products at different times of the weekend.   \
The folder of Algorithm ----This folder includes four different algorithms
(Eclat,Apriori,FP_Growth,Tree_projection),each sub folder includes the main python file and util python file 
.Moreover,it contains the code computing the rules like the support,confidence and lift.With different supports 
,we can yield the different results. \
The folder of Results ----This folder includes four different algorithms
(Eclat,Apriori,FP_Growth,Tree_projection),each sub folder includes the main python file and util python file 
.Moreover,it contains the code computing the rules like the support,confidence and lift.With different supports 
,we can yield the different results.

