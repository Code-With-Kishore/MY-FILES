# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 06:16:19 2024

@author: Admin
"""

import random
n=int(input('Enter n number:'))
x={random.randint(0,10000) for i in range(n)}
a={ i for i in x if(i>=0 and i<=9)}
b={ i for i in x if(i>=10 and i<=99)}
c={ i for i in x if(i>=100 and i<=999)}
d={ i for i in x if(i>=1000 and i<=9999)}
print('Its a single digit:', a)
print('Its a two digit:', b)
print('Its a three digit:', c)
print('Its a four digit:', d)
