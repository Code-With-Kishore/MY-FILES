#pgm.no.45
#13/5/24
#given integer no. is single digit, two digit, three digit or not.

a=int(input('enter a value:'))
if(a>=0 and a<=9):
    print('single digit')
else:
    if(a>=10 and a<=99):
        print('two digit')
    else:
        if(a>=100 and a<=999):
            print('three digit')
        else:
            if(a>=1000 and a<=9999):
                print('four digits')
            else:
                print('zero')
                
        
        
    