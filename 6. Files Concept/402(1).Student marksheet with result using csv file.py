# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 00:49:25 2024

@author: Admin
"""

import csv
f=open('studentdata.csv')
x=csv.reader(f)
a=next(x)

for i in x:
    print()
    print( "Bishop Heber Matriculation Higher secondary school","- Tiruchirappalli.",)
    print()
    print("Name of Student:",i[0] ,"\t\t\t\t","Register Number:",i[1])
    print()
    print('_'*30)
    print("|","Subjects",'  |',"Marks"'|',"Result""  |")
    print('_'*30)
    
    
    for j in range(4,9,1):
        if i[j]>='35':
            r='Pass'
        else:
            r='Fail'
        
        print("|",a[j],'\t ''|',i[j],"  |","",r,"  |")
        print('_'*30)
      
    print("|",'Total     ',"|",i[9]," |","\t\t"," |") 
    print('_'*30)
    print()
    print('Class Teacher Signature:',"\t\t\t",'Parent Signature:') 
    print()
    print('_'*75)