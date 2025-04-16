# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 11:24:20 2025

@author: Admin
"""


import pandas as pd
df = pd.read_csv('D:\STUDENT MARKS2.csv')

df=df.dropna()

df['TAMIL']=df['TAMIL'].astype(int)
df['ENGLISH']=df['ENGLISH'].astype(int)
df['MATHS']=df['MATHS'].astype(int)
df['SCIENCE']=df['SCIENCE'].astype(int)
df['SOCIAL']=df['SOCIAL'].astype(int)

print(df)