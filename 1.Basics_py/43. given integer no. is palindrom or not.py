#program no.43
#13/5/24
#given integer is palindrom or not

a=int(input('enter a value:'))
d1=a%10
d2=a//10
d3=d2%10
d4=d2//10
sum=(d1*100)+(d3*10)+(d4*1)
if(sum==a):
    print('palindrom')
else:
    print('not a palindrom')

