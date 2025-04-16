#pgm no.38
#9.5.24
#biggest of three integer number

a=int(input('enter first integer:'))
b=int(input('enter second integer:'))
c=int(input('enter third integer:'))
if(a>b):
    if(a>c):
        print(c)
    else:
        print(a)
else:
    if(b>c):
        print(c)
    else: 
        print(b)