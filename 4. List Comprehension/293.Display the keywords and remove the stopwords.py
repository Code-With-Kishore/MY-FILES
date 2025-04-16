# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:15:00 2024

@author: Admin
"""

a=input('Enter a string:')
b=a.split()
c=set(b)
stop_words={'Rockfort', 'Thanjavur periya kovil', 'mukkamboor', 'cauvery river', 'kallanai dam'}
d=stop_words
e=c.intersection(d)
print(e)