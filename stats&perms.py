#!/usr/bin/env python
# coding: utf-8

# #Write a user defined function that will take a list of values and return mean values

# In[21]:


def calculate_mean(values):
    if len(values) == 0:
        return None  
    return sum(values)/len(values)


# In[25]:


values = [10, 20, 30, 40, 50]
mean_value = calculate_mean(values)
print(mean_value)


# #Write a user defined function that will take a list of values and return mode values

# In[43]:


def find_mode(values):
    a = [values.count(x) for x in set(values)]  
    b = max(a)
    return [x for x in set(values) if values.count(x) == b]


# In[47]:


values = [1, 2, 2, 3, 3, 3, 4, 5]
mode = find_mode(values)
print(mode) 


# In[ ]:





# In[53]:


def mode_value(L):
    s=set(L)
    d={}
    for x in s:
        d[x]=L.count(x)
    return(max(d.values()))


# In[55]:


L=["M","M","F","M","F","M"]
mode_value(L)


# In[ ]:




