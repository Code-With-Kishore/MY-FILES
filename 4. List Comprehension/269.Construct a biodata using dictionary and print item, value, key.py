# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 07:07:35 2024

@author: Admin
"""

a=input('Enter name:')
b=int(input('Enter age:'))
c=input('Enter qualification:')
d=input('Enter gender:')
e=input('Enter location:')

x=dict(Name=a, Age=b, Qualification=c, Gender=d, Location=e)
i=x.items()
j=x.keys()
k=x.values()

print('Biodata:', x)
print('Items of Biodata:', i)
print('Keys of Biodata:', j)
print('Values of Biodata:', k)
