# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 06:19:51 2024

@author: Admin
"""

x=input('Enter the string:')
def non_vowels(s):
    if s not in 'a,e,i,o,u':
        return True
    else:
        return False
    
#main
y=filter(non_vowels,x)
for i in y:
    print(i,end='')
        