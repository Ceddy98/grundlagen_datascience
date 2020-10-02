#!/usr/bin/env python
# coding: utf-8

# In[8]:


eingabe = input("Text: ")


# In[2]:


from hashlib import sha256


# In[9]:


hashCode = sha256(eingabe.encode('utf-8'))


# In[10]:


hashCode


# In[11]:


hashCode.hexdigest()


# In[ ]:




