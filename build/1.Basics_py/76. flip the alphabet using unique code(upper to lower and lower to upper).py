# -*- coding: utf-8 -*-
"""
Created on Thu May 30 06:47:28 2024

@author: Admin
"""
#flip the alphabet using unique code.(upper to lower and lower to upper.)
a=input('Enter a value:')
u=ord(a)
if(u>=65 and u<=90):
    x=u+32
    c=chr(x)
    print(c)
elif(u>=97 and u<=122):
     y=u-32
     d=chr(y)
     print(d)     
else:
     print('not')
         