# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 17:56:54 2025

@author: Admin
"""

import pandas as pd
import random as rd
daily_wages=int(input("Enter dailywages: "))
days=[rd.randint(1,31)for i in range(12)]
holidays=[rd.randint(1,4)for i in range(12)]
months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov','Dec']
x=pd.Series(data=days,index=months)
y=pd.Series(data=holidays,index=months)
working_days=x-y
month_salary=working_days*daily_wages
print(month_salary)