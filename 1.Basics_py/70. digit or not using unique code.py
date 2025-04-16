#pgm.no.70
#26/5/24
#given character is digit or not using unique code.

a=(input('Enter a character:'))
u=ord(a)
if(u>=48 and u<=57):
    print('digit')
else:
    print('not')
    