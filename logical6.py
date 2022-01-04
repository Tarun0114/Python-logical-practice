import math 
a=float(input('enter value of side a: '))
b=float(input('enter value of side b: '))
c=float(input('enter value of side c: '))
s=(a+b+c)/2
print('s: ',s)
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('area ',area)