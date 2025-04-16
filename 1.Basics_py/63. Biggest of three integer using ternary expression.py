#pgm.no.63
#25/5/24
#biggest of three integer number using Ternary expression.

a=int(input('Enter a value:'))
b=int(input('Enter b value:'))
c=int(input('Enter c value:'))
d= a if a>b else b
d1= c if c>d else d
print(d1)