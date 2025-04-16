# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 06:32:02 2024

@author: Admin
"""

import random
x=lambda n: [random.randint(1,100)for i in range(n)]
n=int(input('Enter n value:'))
list1=x(n)
list2=x(n)
s=lambda list1,list2: [list1[i]+list2[i]for i in range(n)]
print('list1:',list1)
print('list2:',list2)
print('sum of two list:',s(list1,list2))
    
