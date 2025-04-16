# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 09:32:03 2024

@author: Admin
"""
b=c=d=e=0
a=input('enter a character:')
while a!='$':
    u=ord(a)
    if(u>=65 and u<=90):
        b=b+1
    elif(u>=97 and u<=122):
        c=c+1
    elif(u>=48 and u<=57):
        d=d+1
    else:
        e=e+1
    a=input('enter a character')
    print(b)
    print(c)
    print(d)
    print(e)
    
        