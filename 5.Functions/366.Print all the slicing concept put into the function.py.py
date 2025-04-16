# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:17:57 2024

@author: Admin
"""

def menu():
    print('1. Extract all the string')
    print('2. Extract n character')
    print('3. Extract n character from mth position')
    print('4. Extract all character from mth position')
    print('5. Copy the last n character')
    print('6. Reverse the string')
    print('7. Reverse the string and check palindrome or not')
    print('8. Reverse the string using negative indexing')
    print('9. Extract n char from right edge')
    print('10. Copy all the character from mth position using negative index')
    print('11. Copy last n char from right side edge using negative index')
    print('12. Exit')
    n=int(input('Select any method:'))
    return n

def copy_all(s):
    x=s[:]
    return x

def n_char(s,n):
    x=s[0:n]
    return x

def nchar_from_mthposition(s,n,m):
    x=s[m:m+n]
    return x

def all_char_from_mthposition(s,m):
    x=s[m:]
    return x

def copy_last_nchar(s,n):
    ln=len(s)
    a=ln-n
    x=s[a:]
    return x

def reverse(s):
    x=s[::-1]
    return x

def reverse_palindrom(s):
   
    x=s[::-1]
    if x==s:
        print('Palindrom')
    else:
        print('Not a palindrom')
        
        
def reverse_negative(s):
    x=s[-1::-1]
    return x
 
def nchar_rightedge(s,n):
    ln=len(s)
    d=ln-n
    x=s[d:ln]
    return x

def copyall_from_mth_negative(s,m):
    
    x=s[-m::-1]
    return x

def nchar_rightedge_negative(s,n):
    ln=len(s) 
    x=s[ln-n:ln+1]
    return x

y=menu()
while y!=12:
    if y==1:
        s=input('Enter string:')
        z=copy_all(s)
        print('The Extraction of all the string is:',z)
    elif y==2:
        s=input('Enter string:')
        n=int(input('Enter n value:'))
        z=n_char(s, n)
        print('The Extraction of n character is:',z)
    elif y==3:
        s=input('Enter string:')
        n=int(input('Enter n char value:'))
        m=int(input('Enter mth position value:'))
        z=nchar_from_mthposition(s, n, m)
        print(z)
    elif y==4:
        s=input('Enter string:')
        m=int(input('Enter mth position:'))
        z=all_char_from_mthposition(s, m)
        print(z)
    elif y==5:
        s=input('Enter string:')
        n=int(input('Enter n value:'))
        z=copy_last_nchar(s, n)
        print(z)
    elif y==6:
        s=input('Enter string:')
        z=reverse(s)
        print(z)
    elif y==7:
        s=input('Enter string:')
        z=reverse_palindrom(s)
        print(z)
    elif y==8:
        s=input('Enter string:')
        z=reverse_negative(s)
        print(z)
    elif y==9:
        s=input('Enter string:')
        n=int(input('Enter n value:'))
        z=nchar_rightedge(s, n)
        print(z)
    elif y==10:
        s=input('Enter string:')
        m=int(input('Enter mth position value:'))
        z=copyall_from_mth_negative(s,m)
        print(z)
    elif y==11:
        s=input('Enter string:')
        n=int(input('Enter n value:'))
        z=nchar_rightedge_negative(s, n)
        print(z)
        
    else:
        pass
    y=menu()
        
    