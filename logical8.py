import math
a=int(input('Enter the value of a: '))
b=int(input('Enter the value of b: '))
c=int(input('Enter the value of c: '))
dis = (b**2) - (4*a*c)
ans1 = (-b -  math.sqrt(dis))/(2 * a)
ans2 = (-b + math.sqrt(dis))/(2 * a)
print('1st root is ',ans1,' 2nd root is ',ans2)