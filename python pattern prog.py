#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("enter the no.of rows to be print"))

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()


# In[3]:


n=int(input("enter the no.of rows to be print"))

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()


# In[ ]:




