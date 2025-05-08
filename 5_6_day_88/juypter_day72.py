#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df=pd.read_csv('salaries_by_college_major.csv')


# In[2]:


df


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df.isna()


# In[7]:


clean_df=df.dropna()


# In[8]:


clean_df.tail()


# In[9]:


clean_df['Starting Median Salary']


# In[10]:


clean_df['Starting Median Salary'].max()


# In[11]:


clean_df['Starting Median Salary'].idxmax()


# In[12]:


clean_df['Undergraduate Major'].loc[43]


# In[13]:


clean_df['Undergraduate Major'][43]


# In[14]:


clean_df['Mid-Career Median Salary'].max()


# In[15]:


clean_df['Mid-Career Median Salary'].idxmax()


# In[16]:


clean_df['Mid-Career Median Salary'][8]


# In[17]:


clean_df.loc[8]


# In[18]:


clean_df['Starting Median Salary'].min()


# In[19]:


clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]


# In[20]:


clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]


# In[21]:


salary_diff=clean_df['Mid-Career 90th Percentile Salary']-clean_df['Mid-Career 10th Percentile Salary']


# In[22]:


salary_diff


# In[23]:


clean_df.insert(1,'Spread',salary_diff)


# In[31]:


clean_df.head()


# In[32]:


low_risk=clean_df.sort_values('Spread')


# In[33]:


low_risk.head()


# In[34]:


highest_potential=clean_df.sort_values('Mid-Career 90th Percentile Salary',ascending=False)


# In[35]:


highest_potential.head()


# In[36]:


greatest_spread=clean_df.sort_values('Spread',ascending=False)
greatest_spread[['Undergraduate Major','Spread']].head()


# In[37]:


greatest_spread=clean_df.sort_values('Mid-Career Median Salary',ascending=False)
greatest_spread[['Undergraduate Major', 'Mid-Career Median Salary']].head()


# In[38]:


clean_df.groupby('Group').count()


# In[49]:


print(clean_df.dtypes)


# In[50]:


pd.options.display.float_format = '{:,.2f}'.format 
mean_df = clean_df.groupby('Group').mean(numeric_only=True)


# In[51]:


mean_df


# In[ ]:




