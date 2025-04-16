# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:29:16 2024

@author: Admin
"""

stopwords = open('project.txt', 'r')
b = stopwords.read()
c = b.split()
d = set(c)

n = int(input('Enter n value:'))
files = []
for y in range(n):
    e = input('Enter filename:')
    files.append(e)

f = open('task.txt', 'r')
g = f.read()
h = g.split()
i = set(h) - d

file_total = len(h)
ln = len(i)



print('Original_filename:',f, ',' 'total no.of.words:',ln)
print('_' *125)



for x in range(1,ln):
    j = open(files[x], 'r')
    k = j.read()
    l = k.split()
    m = set(l)
    current_file_total = len(l)
    
    common_word = i.intersection(m)  
    total_duplicate_value = len(common_word)
    unique_value = i.union(m)
    total_unique_value = len(unique_value)
    total_percent = (total_duplicate_value / total_unique_value) * 100 
    
    
    print('Total words:', current_file_total)
    print('Total Duplicate values:', total_duplicate_value)
    print('Percentage:'+ str(total_percent))
