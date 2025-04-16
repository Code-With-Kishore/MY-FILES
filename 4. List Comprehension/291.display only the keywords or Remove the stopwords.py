# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:17:21 2024

@author: Admin
"""

a=input('Enter a string:')
b=a.split()
c=set(b)
key_words={'is','was','are','in','on','with','an','the','at', 'of','to','for'}
d=key_words
e=c-d
print(e)
