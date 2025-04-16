# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:09:01 2024

@author: Admin
"""
n=100
fahrenheit=[i for i in range(0,n+1)]
celsius=[(j-32)*5/9 for j in fahrenheit]
print(fahrenheit)
print(celsius)