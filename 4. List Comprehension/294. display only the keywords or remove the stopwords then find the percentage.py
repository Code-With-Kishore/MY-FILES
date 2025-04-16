# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:15:01 2024

@author: Admin
"""

a=input('Enter a string:')
b=a.split()
c=set(b)
stop_words=['Rockfort', 'kallanai', 'cauvery']
d=set(stop_words)
e=c.intersection(d)
print(e)

stopwords=len(e)
total=len(c)

percent=(stopwords/total*100)

print('matching of stopwords:',e)
print('percentage of stopwords:', percent)