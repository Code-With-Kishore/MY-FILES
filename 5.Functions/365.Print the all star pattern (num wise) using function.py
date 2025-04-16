# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 02:18:45 2024

@author: Admin
"""

def menu():
    print('1.five_by_five pattern')
    print('2.right_half_diamond')
    print('3.left_half_diamond')
    print('4.triangle')
    print('5.inverse_triangle')
    print('6.diamond_pattern')
    print('7.int_diamond_pattern')
    print('8.alphabet_diamond_pattern')
    print('9.hollow_diamond_pattern')
    print('10.exit')
    n=int(input('select the pattern:'))
    return n
    
def five_by_five(n):
    for i in range(1,n):
        print('*'*5)
    
def right_half_diamond(n):
    for i in range(1, n):
        print('*'*i)
    for j in range(n, 0, -1):
        print('*'*j)
    
def left_half_diamond(n):
    for i in range(1,n+1):
        print(' '*(n-i)+'*'*i)
        
def triangle(n):
    for i in range(1, n):
        print(' '*(n-i) +'*'*((2*i)-1))
        
def inverse_triangle(n):
    for i in range(0, n):
        print(' '*i+'*'*(2*(n-i)-1))
        
def diamond_pattern(n):
    for i in range(1, n):
        print(' '*(n-i) +'*'*((2*i)-1))

    for j in range(0, n):
        print(' '*j+'*'*(2*(n-j)-1))
        
def int_diamond_pattern(n):
    
    for i in range(1,n):
        print(' '*(n-i), end="")
        for j in range((2*i)-1):
            print(j, end="")
        print()
            
    for i in range(0,n):
        print(' '*i, end="")
        for j in range((2*(n-i)-1)):
            print(j, end="")
        print()
    
def alphabet_diamond_pattern(n):
   
    for i in range(1,n):
        print(' '*(n-i), end="")
        for j in range((2*i)-1):
            print(chr(97+j), end="")
        print()

    for i in range(0,n):
        print(' '*i, end="")
        for j in range((2*(n-i)-1)):
            print(chr(97+j), end="")
        print()
    
def hollow_diamond_pattern(n):
    print(' '*n +'*')

    for i in range(1,n):
        print(' '*(n-i) +'*' + ' ' * ((2*i)-1)+'*')

    for j in range(0,n):
        print(' '*j+'*' + ' '*(2*(n-j)-1)+'*')
    
    print(' '*n +'*')
    
#main
x=menu()
while x!=10:
    if x==1:
        n=int(input('Enter pattern count value:'))
        five_by_five(n)
    elif x==2:
        n=int(input('Enter pattern count value:'))
        right_half_diamond(n)
    elif x==3:
        n=int(input('Enter pattern count value:'))
        left_half_diamond(n)
    elif x==4:
        n=int(input('Enter pattern count value:'))
        triangle(n)
    elif x==5:
        n=int(input('Enter pattern count value:'))
        inverse_triangle(n)
    elif x==6:
        n=int(input('Enter pattern count value:')) 
        diamond_pattern(n)
    elif x==7:
        n=int(input('Enter pattern count value:'))
        int_diamond_pattern(n)
    elif x==8:
        n=int(input('Enter pattern count value:'))
        alphabet_diamond_pattern(n)
    elif x==9:
        n=int(input('Enter pattern count value:'))
        hollow_diamond_pattern(n)
    else:
        pass
    x=menu()
        
        
    
    
    
    
    