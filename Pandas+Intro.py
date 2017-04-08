
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[3]:

s


# In[4]:

s.index

pd.Series(np.random.randn(5))
# In[5]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[6]:

pd.Series(d)


# In[7]:

d


# In[8]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[9]:

pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])


# In[10]:

s


# In[11]:

s[0]


# In[12]:

s[:3]


# In[13]:

s[s > s.median()]


# In[14]:

s[[4, 3, 1]]


# In[15]:

np.exp(s)


# In[16]:

s['a']


# In[17]:

s['e'] = 12.


# In[18]:

s


# In[19]:

'e' in s


# In[20]:

'f' in s


# In[21]:

s.get('f')


# In[22]:

s.get('e')


# In[23]:

s.get('f', np.nan)


# In[24]:

s + s


# In[25]:

s * 2


# In[26]:

np.exp(s)


# In[27]:

s[1:] + s[:-1]


# In[28]:

s = pd.Series(np.random.randn(5), name='something')


# In[29]:

s


# In[30]:

s2 = s.rename("different")


# In[31]:

s2.name


# In[32]:

s['f'] = 0


# In[33]:

s


# In[34]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
   'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
  


# In[35]:

d


# In[36]:

df = pd.DataFrame(d)


# In[37]:

df


# In[38]:

pd.DataFrame(d, index=['d', 'b', 'a'])


# In[39]:

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])


# In[40]:

df.Index


# In[41]:

df.index


# In[42]:

df.columns


# In[43]:

d = {'one' : [1., 2., 3., 4.],
   'two' : [4., 3., 2., 1.]}


# In[44]:

d


# In[45]:

pd.DataFrame(d)


# In[46]:

pd.DataFrame(d, index=['a', 'b', 'c', 'd'])


# In[47]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[48]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[49]:

pd.DataFrame(data)


# In[50]:

pd.DataFrame(data, index=['first', 'second'])


# In[51]:

pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[52]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[53]:

data


# In[54]:

pd.DataFrame(data2)


# In[55]:

pd.DataFrame(data2, index=['first', 'second'])


# In[56]:

pd.DataFrame(data2, columns=['a', 'b'])


# In[57]:

df['one']


# In[58]:

df['three'] = df['one'] * df['two']


# In[59]:

df['flag'] = df['one'] > 2


# In[60]:

df


# In[61]:

del df['two']


# In[62]:

three = df.pop('three')


# In[63]:

df


# In[ ]:




# In[64]:

df['foo'] = 'bar'


# In[65]:

df


# In[66]:

df['one_trunc'] = df['one'][:2]


# In[ ]:




# In[67]:

df


# In[68]:

df.insert(1, 'bar', df['one'])


# In[69]:

df


# In[70]:

three


# In[ ]:



