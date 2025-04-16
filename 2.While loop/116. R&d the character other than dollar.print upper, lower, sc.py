# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:30:07 2024

@author: Admin
"""

a=input('enter a character:')
while a!='$':
    u=ord(a)
    if(u>=65 and u<=90):
       print('upper')
    elif(u>=97 and u<=122):
        print('lower')
    elif(u>=48 and u<=57):
        print('digit')
    else:
        print('special character')
    a=input('enter a character')
        
    