#!/usr/bin/env python
# coding: utf-8

# In[1]:


def mean_value(*n):
    sum=0
    counter=0
    for x in n:
        counter = counter+1
        sum += x 
    mean = sum/counter
    return mean 
mean_value(1,2,3,4,5)


# In[17]:


def product(*n):
    res=1
    for i in range(len(n)):
        res *= n[i]
    return res
product(1,2,3,4,5)


# In[ ]:




