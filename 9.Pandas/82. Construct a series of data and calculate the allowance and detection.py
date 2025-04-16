# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 18:53:45 2025

@author: Admin
"""

import numpy as np
import pandas as pd
n =int(input('Enter n value: '))
bp=np.random.randint(10000,60000,n)
id_no= [225214201 + i for i in range(n)]
NA_val = [225214205, 225214207, 225214209]
s= pd.Series(bp,index=id_no)

for j in NA_val:
    s[j]=pd.NA

# Clean the missing (N/A) values.
x=s.dropna()

# Allowances
hra = x* 0.10  
ta = x* 0.10 
cca=x*0.05  
total_salary =x+hra+ta+cca  

# Detections
pf =x* 0.08 
tds = x* 0.05  
total_deductions = pf + tds
net_salary = total_salary - total_deductions

print('\nTotal Salary:\n',total_salary)
print('\nNet Salary:\n',net_salary)