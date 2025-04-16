#pgm.no.47
#13/5/24
#print single, two, three, and four digits using elif.

a=int(input('enter a value:'))
if(a>=0 and a<=9):
  print('single digit')
elif(a>=10 and a<=99):
    print('two digit')
elif(a>=100 and a<=999):
    print('three digit')
elif(a>=1000 and a<=9999):
    print('four digit')
else:
    print('not')
        