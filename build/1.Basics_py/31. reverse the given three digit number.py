#pgm no.31
#5.5.24
#reverse the given three digit number

a=int(input('enter a:'))
d1=a%10
d2=a//10
d3=d2%10
d4=d2//10
reverse=(d1*100)+(d3*10)+(d4*1)
print(reverse)


