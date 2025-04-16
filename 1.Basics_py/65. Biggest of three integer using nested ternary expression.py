#pgm.no.65
#25/5/24
#Biggest of integer using Nested ternary expression.

a=int(input('Enter a value:'))
b=int(input('Enter b value:'))
c=int(input('Enter c value:'))
d= a if a>b else b if b>c else c if c>a else a
print(d)
