#pgm.no.58
#17/5/24
#given integer no. is leapyear or not using implicit check.

a=int(input('Enter a value:'))
r=a%4
if(r):
    print('not')
else:
    print('leapyear')
    