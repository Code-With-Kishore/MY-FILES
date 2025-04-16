# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 08:43:29 2024

@author: Admin
"""

import csv
f=open('studentdata.csv')
x=csv.reader(f)
a=next(x)

for i in x:
    print( "Bishop Heber Matriculation Higher secondary school","- Tiruchirappalli",)
    print()
    print("Student Name: ",i[0] ,"\t\t","Roll.No: ",i[1])
    print()
    print("Subject",'\t', "Marks","\t\t")
    print()
    
    print(a[4],"\t\t",i[4])
    print(a[5],"\t",i[5])
    print(a[6],"\t\t",i[6])
    print(a[7],"\t",i[7])
    print(a[8],"\t\t",i[8])
    print()
    print(a[9],"\t\t",i[9])  
    print()
        
    print('Class Teacher Signature:',"\t\t\t",'Parent Signature:') 
       
    print('_'*75)
    
        
        
