
# coding: utf-8

# In[42]:


import math

import pandas as pd
import numpy as np


# In[32]:


df = pd.read_csv('./example.csv', header=None)


# In[33]:


df


# In[34]:


# 19文字/行
# LINEの吹き出しは13文字
# 5文字くらい重なる
# →12文字で切ろう（ここは可変が望ましいけど）

# 発言/発言者のcsvを作る
# 1/0で相手/自分


# In[36]:


line_len = 19
dialog_len = 12


# In[80]:


text_output = []

for i in range(df.shape[0]):
    text = df.iloc[i, 1]
    text_list = []
    if len(text) >= dialog_len:
        lines = math.ceil(len(text)/dialog_len)
        for l in range(lines):
            l_text = text[l*dialog_len:(l+1)*dialog_len]
            text_list.append(l_text)
    else:
        text_list.append(text)
    
    # 自分側
    if df.iloc[i, 0] == 0:
        for t in range(len(text_list)):
            text = text_list[t]
            if t != 0:
                while len(text) <= dialog_len-1:
                    text = text + '　'
            while len(text) <= line_len-1:
                text = '　' + text
            text_output.append(text)
    
    # 相手側
    elif df.iloc[i, 0] == 1:
        for t in range(len(text_list)):
            text = text_list[t]
            while len(text) <= line_len-1:
                text = text + '　'
            text_output.append(text)
    else:
        print('error')
    
    text_output.append('')

for l in text_output:
    print(l)

