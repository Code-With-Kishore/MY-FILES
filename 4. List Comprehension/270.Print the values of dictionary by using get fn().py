# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 23:14:17 2024

@author: Admin
"""

a=input('Enter name:')
b=int(input('Enter age:'))
c=input('Enter qualification:')
d=input('Enter gender:')
e=input('Enter location:')

x=dict(Name=a, Age=b, Qualification=c, Gender=d, Location=e)

i=x.get('Name')
j=x.get('Age')
k=x.get('Qualification')
l=x.get('Gender')
m=x.get('Location')

print(x)
print('Value of key is:', i)
print('Value of key is:', j)
print('Value of key is:', k)
print('Value of key is:', l)
print('Value of key is:', m)

