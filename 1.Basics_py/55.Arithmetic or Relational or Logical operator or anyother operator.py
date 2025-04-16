#pgm.no.55
#17.5.24
#Given operator is Arithmetic, Relational, or Logical operator or anyother operator.

a=input('Enter a operator:')
if(a=='+' or a=='-' or a=='*' or a=='/' or a=='//' or a=='%' or a=='**'):
    print('Its a Arithmetic operator')
elif(a=='>' or a=='<' or a=='>=' or a=='<=' or a=='==' or a=='!='):
    print('Its a Relational operator')
elif(a=='and' or a=='or' or a=='not'):
    print('Its a Logical operator')
else:
    print('Anyother Operator')
