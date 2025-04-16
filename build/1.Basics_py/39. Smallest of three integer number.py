#pgm.no.39
#10.5.24
#Smallest of three integer number

a=int(input('Enter first integer:'))
b=int(input('Enter second integer:'))
c=int(input('Enter third integer:'))
if(a<b):
    if(a<c):
        print(a)
    else:
        if(b<c):
            print(b)
        else:
            print(c)
