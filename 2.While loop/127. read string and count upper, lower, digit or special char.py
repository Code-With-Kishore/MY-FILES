# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 08:17:11 2024

@author: Admin
"""
a=input('Enter a string:')
ln=len(a)
b=0
c=0
d=0
e=0
i=0
while i<=ln-1:
 
    if(a>='A' and a<='Z'):
        b=b+1
    elif(a>='a' and a<='z'):
        c=c+1
    elif(a>='0' and a<='9'):
        d=d+1
    else:
        e=e+1
    i=i+1
print(b)
print(c)
print(d)
print(e)
       