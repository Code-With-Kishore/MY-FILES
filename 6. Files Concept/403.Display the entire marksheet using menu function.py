# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:25:07 2024

@author: Admin
"""

def menu():
    print('1. Display Student Marksheet.')
    print('2. Display Student Marksheet with Result.')
    print('3. Display Student Marksheet with Grade. ')
    print('4. Display Only Passed students Marksheet.')
    print('5. Display Only Failed students Marksheet.')
    print('6. Display Only a Particular student Marksheet.')
    print('7. Exit.')
    n=int(input('Select the Marksheet:'))
    return n


def student_marksheet():
    import csv
    f=open('studentdata.csv')
    x=csv.reader(f)
    a=next(x)
    for i in x:
        print( "Bishop Heber Matriculation Higher secondary school","- Tiruchirappalli",)
        print()
        print("Student Name: ",i[0] ,"\t        \t","Register Number: ",i[1])
        print()
        print("_" *25)
        print('|',"Subject",'   |\t', "Marks",'  |')
        print("_" *25)     
        print('|',a[4],"\t |\t",i[4],'     |')
        print("_" *25)
        print('|',a[5],"\t |\t",i[5],'     |')
        print("_" *25)
        print('|',a[6],"\t |\t",i[6],'     |')
        print("_" *25)
        print('|',a[7],"\t |\t",i[7],'     |')
        print("_" *25)
        print('|',a[8],"\t |\t",i[8],'     |')
        print("_" *25)
        print('|',a[9],"\t |\t",i[9],'    |')
        print("_" *25)
        print()          
        print('Class Teacher Signature:',"\t\t\t",'Parent Signature:') 
        print('_'*75)

        
def Result():
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
        
        
def Grade():
    import csv
    f=open('studentdata.csv')
    x=csv.reader(f)
    a=next(x)

    for i in x:
        print()
        print( "DHANALAKSHMI SRINIVASAN MATRICULATION HIGHER SECONDARY SCHOOL.")
        print('              Woraiyur, Tiruchirappalli.')
        print()
        
        print("NAME OF STUDENT:",i[0] ,"\t\t","REGISTER NUMBER:",i[1])
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
            
        total = i[9] 
        if total >= '450':
           grade = 'A'
        elif total >= '350':
            grade = 'B'
        elif total >='250':
            grade = 'C'
        else:
            grade = 'D'        
        print("|",'Total     ',"|",i[9]," |","","       |") 
        print('_'*30)
        print()
        print('OVERALL GRADE:',grade)
        print()
        print('Class Teacher Signature:',"\t\t",'Parents Signature:') 
        print()
        print('_'*75)
        
def Passed():
    import csv
    f = open('studentdata.csv')
    x = csv.reader(f)
    a = next(x)

    for i in x:
        print()
        print("DHANALAKSHMI SRINIVASAN MATRICULATION HIGHER SECONDARY SCHOOL.")
        print('              Woraiyur, Tiruchirappalli.')
        print()
            
        print("NAME OF STUDENT:", i[0], "\t\t", "REGISTER NUMBER:", i[1])
        print()
        print('_' * 30)
        print("|", "Subjects", '  |', "Marks", '|', "Result", "|")
        print('_' * 30)
            
        for j in range(4, 9, 1):
            if int(i[j]) >= 30:
                r = 'Pass'
            else:
                r = 'Fail'          
            print("|", a[j], '\t', '|', i[j], "  |", "", r,  "  |")
            print('_' * 30)
            
        total = int(i[9])
        if total >= 450:
            grade = 'A'
        elif total >= 350:
            grade = 'B'
        elif total >= 250:
            grade = 'C'
        else:
            grade = 'D'
                
        print("|", 'Total     ', "|", i[9], " |", "", "       |")
        print('_' * 30)
        print()
        print('OVERALL GRADE:', grade)
        print()
        print('Class Teacher Signature:', "\t\t", 'Parents Signature:')
        print()
        print('_' * 75)
                
        
def Failed():
    import csv
    f = open('studentdata.csv')
    x = csv.reader(f)
    a = next(x)

    for i in x:
        
        print()
        print("DHANALAKSHMI SRINIVASAN MATRICULATION HIGHER SECONDARY SCHOOL.")
        print('              Woraiyur, Tiruchirappalli.')
        print()      
        print("NAME OF STUDENT:", i[0], "\t\t", "REGISTER NUMBER:", i[1])
        print()
        print('_' * 30)
        print("|", "Subjects", '  |', "Marks", '|', "Result", "|")
        print('_' * 30)
            
        for j in range(4, 9, 1):
            if int(i[j]) >= 35:
                r = 'Pass'
            else:
                r = 'Fail'               
            print("|", a[j], '\t', '|', i[j], "  |", "", r,  "  |")
            print('_' * 30)
            
        total = int(i[9])
        if total >= 450:
           grade = 'A'
        elif total >= 350:
            grade = 'B'
        elif total >= 250:
            grade = 'C'
        else:
            grade = 'D'
                
            print("|", 'Total     ', "|", i[9], " |", "", "       |")
            print('_' * 30)
            print()
            print('OVERALL GRADE:', grade)
            print()
            print('Class Teacher Signature:', "\t\t", 'Parents Signature:')
            print()
            print('_' * 75)

def Particular_student():
    import csv
    f=open('studentdata.csv')
    x=csv.reader(f)
    a=next(x)
    num=input('Enter roll.no:')
    for i in x:
        if i[1] == num:
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
            

y=menu()
while y!=7:
    if y==1:
        a=student_marksheet()
    elif y==2:
        Result()
    elif y==3:
        Grade()
    elif y==4:
        Passed()
    elif y==5:
        Failed()
    elif y==6:
        Particular_student()
    else:
        pass
    y=menu()
                


     