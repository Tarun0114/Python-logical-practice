#sum of digits of a given number
pro=1
n=int(input("enter n value"))
while(n!=0):
    pr=n%10
    pro=pro*pr
    n=n//10
print(pro)