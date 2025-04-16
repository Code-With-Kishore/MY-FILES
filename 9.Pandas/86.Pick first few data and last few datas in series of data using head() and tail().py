# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 18:43:40 2025

@author: Admin
"""

import pandas as pd
import random as rd

daily_wages=int(input("Enter dailywages: "))
days=[rd.randint(29,31)for i in range(12)]
holidays=[rd.randint(1,4)for i in range(12)]
months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov','Dec']

x=pd.Series(data=days,index=months)
y=pd.Series(data=holidays,index=months)

working_days=x-y
month_salary=working_days*daily_wages

print('\nMonthly Salary:\n',month_salary)
print('\nFirst few lines:\n',month_salary.head())
print('\nLast few lines:\n',month_salary.tail())
