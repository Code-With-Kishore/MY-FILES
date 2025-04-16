# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:20:36 2024

@author: Admin
"""
import pickle
n=int(input('Enter n value:'))
f=open('biodata','rb')
for i in range(n):
    x=pickle.load(f)
    print(x)
f.close()