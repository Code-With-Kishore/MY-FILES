# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 05:34:42 2024

@author: Admin
"""

a=input('Enter the string:')
b=a.split()
c=set(b) #unique words.

unique_words=len(c)
total_words=len(a)


unique_percent=(unique_words/total_words*100)
duplicate_percent=(total_words-unique_percent)

print('unique words:',c)
print('unique percentage:',unique_percent)
print('duplicate percentage:',duplicate_percent)


