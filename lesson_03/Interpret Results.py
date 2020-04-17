#!/usr/bin/env python
# coding: utf-8

# ### Interpreting Results of Logistic Regression
# 
# In this notebook (and quizzes), you will be getting some practice with interpreting the coefficients in logistic regression.  Using what you saw in the previous video should be helpful in assisting with this notebook.
# 
# The dataset contains four variables: `admit`, `gre`, `gpa`, and `prestige`:
# 
# * `admit` is a binary variable. It indicates whether or not a candidate was admitted into UCLA (admit = 1) our not (admit = 0).
# * `gre` is the GRE score. GRE stands for Graduate Record Examination.
# * `gpa` stands for Grade Point Average.
# * `prestige` is the prestige of an applicant alta mater (the school attended before applying), with 1 being the highest (highest prestige) and 4 as the lowest (not prestigious).
# 
# To start, let's read in the necessary libraries and data.

# In[2]:


import numpy as np
import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("./admissions.csv")
df.head()


# There are a few different ways you might choose to work with the `prestige` column in this dataset.  For this dataset, we will want to allow for the change from prestige 1 to prestige 2 to allow a different acceptance rate than changing from prestige 3 to prestige 4.
# 
# 1. With the above idea in place, create the dummy variables needed to change prestige to a categorical variable, rather than quantitative, then answer quiz 1 below.

# In[8]:


df[['highest_prestige', 'high_prestige', 'some_prestige', 'no_prestige']] = pd.get_dummies(df['prestige'])
df['Intercept'] = 1
df.head()


# In[17]:


df.describe()


# In[ ]:





# `2.` Now, fit a logistic regression model to predict if an individual is admitted using `gre`, `gpa`, and `prestige` with a baseline of the prestige value of `1`.  Use the results to answer quiz 2 and 3 below.  Don't forget an intercept.

# In[10]:


lm = sm.Logit(df['admit'], df[['Intercept', 'gre', 'gpa', 'high_prestige', 'some_prestige', 'no_prestige']])
res = lm.fit()


# In[11]:


from scipy import stats
stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)
res.summary()


# In[16]:


# Decrease
np.exp(-res.params)


# In[15]:


# Increase
np.exp(res.params)


# In[ ]:




