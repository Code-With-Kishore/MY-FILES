# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 08:17:30 2024

@author: Admin
"""

import csv
f=open('studentdata.csv')
x=csv.reader(f)
a=next(x)
Roll_Number=input('Enter Roll.No:')
for i in x:
    if i[1] == Roll_Number:
        print()
        print( "DHANALAKSHMI SRINIVASAN MATRICULATION HIGHER SECONDARY SCHOOL.")
        print('              Woraiyur, Tiruchirappalli.')
        print()
    
        print("NAME OF STUDENT:",i[0] ,"\t\t","REGISTER NUMBER:",i[1])
        print()
        print('_'*30)
        print("|","Subjects",'  |',"Marks"'|',"Result"" |")
        print('_'*30)
    
    
        for j in range(4,9,1):
            if i[j]>='35':
                r='Pass'
            else:
                r='Fail'
        
            print("|",a[j],'\t ''|',i[j],"  |","",r," |")
            print('_'*30)
        
        total = i[9] 
        if total >= '450':
           grade = 'A'
        elif total >= '350':
           grade = 'B'
        elif total >='250':
           grade = 'C'
        else:
           grade = 'D' 
      
        print("|",'Total     ',"|",i[9]," |","","      |") 
        print('_'*30)
        print()
        print('OVERALL GRADE:',grade)
        print()
        print('Class Teacher Signature:',"\t\t",'Parents Signature:') 
        print()
        print('_'*75)