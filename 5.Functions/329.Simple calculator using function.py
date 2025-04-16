# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:55:14 2024

@author: Admin
"""
def calculate(a,b,opr):
    def add():
        c=a+b
        return c
    def sub():
        c=a-b
        return c
    def mul():
        c=a*b
        return c
    def div():
        c=a/b
        return c
    def biggest():
        x=a if a>b else b
        return x
    def smallest():
        y=a if a<b else b
        return y
    if opr=='+':
        return add()
    if opr=='-':
        return sub()
    if opr=='*':
        return mul()
    if opr=='/':
        return div()
    if opr=='>':
        return biggest()
    if opr=='<':
        return smallest()
    
#main
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
opr=input('Enter the operator:')
result=calculate(a,b,opr)
print(result)
    
    