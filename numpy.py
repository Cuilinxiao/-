#!/usr/bin/env python
# coding: utf-8

# # Numpy简介

# numpy提供数据结构：向量、数组的各种操作

# In[1]:


import numpy as np


# # 数组的向量 arange  、linspace、logspace等

# In[2]:


v=np.arange(10)#等价于range
v


# In[3]:


v.ndim


# In[4]:


v.shape


# In[5]:


v.dtype


# In[6]:


v1=np.arange(3,11,2)
v1


# arange([start,] stop[, step,], dtype=None)

# In[7]:


v1.dtype


# In[8]:


v2=np.arange(3,11,2,dtype="float")


# In[9]:


v2.dtype


# np.linspace是生成等差数列的一种方法
# 
# linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# 
#     Return evenly spaced numbers over a specified interval

# In[10]:


v3=np.linspace(2,14,7)
v3


# In[11]:


np.linspace(2.0, 3.0, num=5, retstep=True)


# In[12]:


v3.shape


# np.logspace是生成等比数列的一种方法。
# 
# logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
# 
#     Return numbers spaced evenly on a log scale

# In[13]:


v4=np.logspace(start=3,stop=9,num=7,base=2)
v4


# np.zeros(n,dtype)生成全为0的向量

# In[14]:


np.zeros(10,dtype="float")


# In[15]:


np.random.randn(10)


# In[16]:


help(np.random)


# # 数组

# In[17]:


v5=np.array([np.arange(4),np.arange(4)])
v5


# In[18]:


v5.shape


# In[19]:


v5.ndim


# In[20]:


v5.dtype


# In[21]:


dir(v5)


# In[22]:


v5.reshape(4,2)


# In[23]:


v5.shape=(2,4)
v5


# In[24]:


set(np.typeDict.values())#numpy中的数据类型


# In[25]:


v6=np.zeros((4,3),dtype="float")
v6


# In[26]:


v7=np.ones((3,4))
v7


# In[27]:


v8=np.eye(4)
v8


# # 数组的索引与切片

# In[28]:


a_1=np.linspace(1,10,10,dtype="int")
a_1


# In[29]:


a_1[0]


# In[30]:


a_1[len(a_1)-1]


# In[31]:


a_1[-1]


# In[32]:


a_1[2:5]


# In[33]:


a_1[[2,5,7]]


# In[34]:


a_1[:5]


# In[35]:


a_1[5:]


# In[36]:


a_1[::-1]


# In[37]:


a_2=np.arange(16).reshape(4,4)
a_2


# In[38]:


a_2.shape


# In[39]:


a_2[0,:]


# In[40]:


a_2[[2,3],:]


# In[41]:


a_2[:,0]


# In[42]:


a_2[:,[1,3]]


# In[43]:


a_2[2,3]


# In[44]:


a_2[1:3:2,1:3:2]


# In[45]:


a_2[0,1:3]


# In[46]:


a_2[1:3,1:3]


# In[47]:


a_2


# In[49]:


a_3=np.arange(24).reshape(2,3,4)
a_3


# In[50]:


a_3[0]


# In[51]:


a_3[0,:,:]


# In[53]:


a_3[0,1,:]


# In[54]:


a_3[:,:,1]


# 逻辑索引

# In[55]:


a_3[a_3>15]


# In[58]:


a_3[(a_3>5)&(a_3<20)]


# In[59]:


a_3[~(a_3>15)]


# 数组的操作

# In[60]:


a_3


# In[62]:


b=a_3.ravel()
b


# In[65]:


b.shape


# In[66]:


id(a_3)


# In[67]:


id(b)


# In[69]:


b_1=a_3.flatten()
b_1


# In[70]:


id(b_1)


# In[71]:


b[0]=90


# In[72]:


b


# In[73]:


a_3


# In[76]:


b_1[0]=89
b_1


# In[77]:


a_3


# ravel只是返回数组的一个视图，而flatten会重新分配地址。

# 数组的组合：水平组合（hstack）、垂直组合（vstack）、深度组合（dstack）、列组合（colume_stack）、行组合（row_stack）等

# 1   水平组合:要求行数相同

# In[78]:


a=np.arange(9).reshape(3,3)
a


# In[80]:


b=np.arange(9,18).reshape(3,3)
b


# In[82]:


c1=np.hstack((a,b))
c1


# In[83]:


c2=np.concatenate((a,b),axis=1)
c2


# 2 垂直组合：列数相同

# In[84]:


c3=np.vstack((a,b))
c3


# In[85]:


c4=np.concatenate((a,b),axis=0)
c4


# 深度组合：要求行数与列数都相同.是对于位置元素组合在一起

# In[86]:


c5=np.dstack((a,b))


# In[87]:


c5


# 数组分拆：水平分拆、垂直分拆、深度分拆

# 水平分拆：hsplit

# In[90]:


c1


# In[91]:


c11=np.hsplit(c1,2)
c11


# In[93]:


c12=np.hsplit(c1,3)
c12


# In[94]:


type(c11)


# In[96]:


c13=np.split(c1,2,axis=1)
c13


# 垂直分拆：vsplit

# In[97]:


c1


# In[ ]:


c14

