#pgm.no.66
#25/5/24
#smallest of int no. using ternary expression.

a=int(input('Enter a value:'))
b=int(input('Enter b value:'))
c=int(input('Enter c value:'))
d= a if a<c else c if a<b else b if b>c else a
print(d)
