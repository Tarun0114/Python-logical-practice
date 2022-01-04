n=int(input("Enter an integer value: "))
rev=0
temp=n;
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if temp==rev:
    print("output")
    print("1")
else:
    print("output")
    print("0")