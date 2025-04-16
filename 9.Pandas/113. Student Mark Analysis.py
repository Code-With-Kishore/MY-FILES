# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 18:05:57 2025

@author: Admin
"""
import numpy as np
import pandas as pd
df = pd.read_csv('D:\STUDENT MARKS2.csv')

df['TAMIL']=df['TAMIL'].fillna(value=df['TAMIL'].mean())
df['ENGLISH']=df['ENGLISH'].fillna(value=df['ENGLISH'].mean())
df['MATHS']=df['MATHS'].fillna(value=df['MATHS'].mean())
df['SCIENCE']=df['SCIENCE'].fillna(value=df['SCIENCE'].mean())
df['SOCIAL']=df['SOCIAL'].fillna(value=df['SOCIAL'].mean())

df['TAMIL']=df['TAMIL'].astype(int)
df['ENGLISH']=df['ENGLISH'].astype(int)
df['MATHS']=df['MATHS'].astype(int)
df['SCIENCE']=df['SCIENCE'].astype(int)
df['SOCIAL']=df['SOCIAL'].astype(int)

df.index=[225214201+i for i in range(len(df))]

total_mark=df['TAMIL']+df['ENGLISH']+df['MATHS']+df['SCIENCE']+df['SOCIAL']

df['MARKS']=total_mark

Avg=df['MARKS']/5

df['AVERAGE']=Avg

df.loc[df['AVERAGE'] >= 90, 'GRADE'] = 'A'
df.loc[(df['AVERAGE'] >= 80) & (df['AVERAGE'] < 90), 'GRADE'] = 'B'
df.loc[(df['AVERAGE'] >= 70) & (df['AVERAGE'] < 80), 'GRADE'] = 'C'
df.loc[(df['AVERAGE'] >= 60) & (df['AVERAGE'] < 70), 'GRADE'] = 'D'
df.loc[df['AVERAGE'] < 60, 'GRADE'] = 'F'

max_val = np.argmax(df['MARKS'])  
max_index = df.index[max_val]       
first_mark = df.loc[max_index]          

min_val=np.argmin(df['MARKS'])
min_index=df.index[min_val]
last_mark=df.loc[min_index]

nlar=df.nlargest(3, 'MARKS')
nsmall=df.nsmallest(3, 'MARKS')


high_score1=df['TAMIL'].max()
Tamil_high=df[df['TAMIL']==high_score1]

high_score2=df['ENGLISH'].max()
English_high=df[df['ENGLISH']==high_score2]

high_score3=df['MATHS'].max()
Maths_high=df[df['MATHS']==high_score3] 

high_score4=df['SCIENCE'].max()
Science_high=df[df['SCIENCE']==high_score4] 

high_score5=df['SOCIAL'].max()
Social_high=df[df['SOCIAL']==high_score5]  

T=Tamil_high.head(1)
E=English_high.head(1)
M=Maths_high.head(1)
S=Science_high.head(1)
H=Social_high.head(1)

print(df)

print('\nMax-index value:\n', max_index)
print('\nFirst Rank Student Mark:\n', first_mark)

print('\nMin-index value:\n', min_index)
print('\nLast Rank Student Mark:\n', last_mark)

print('\nTop Student Mark List:\n',nlar)
print('\nLowest Mark Student List:\n',nsmall)

print('\nHighest Score of Tamil Subject:\n',T)
print('\nHighest Score of English Subject:\n',E)
print('\nHighest Score of Maths Subject:\n',M)
print('\nHighest Score of Science Subject:\n',S)
print('\nHighest Score of Social Subject:\n',H)




