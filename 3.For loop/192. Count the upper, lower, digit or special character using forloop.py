# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 07:13:23 2024

@author: Admin
"""
s=input('Enter a string:')
a=0
b=0
c=0
d=0
for i in s:
    u=ord(i)
    if (u>=65 and u<=90):
        a+=1
    elif (u>=97 and u<=122):
        b+=1
    elif (u>=0 and u<=9):
        c+=1
    else:
        d+=1
print('upper count is:',a)
print('lower count is:',b)
print('digit count is:',c)
print('special character count is:',d)
        
        
    
    