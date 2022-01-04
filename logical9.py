

 

number=int(input("enter number"))
if number%2==0:
    if number%8==0:
        print("it is even and 8")
    else:
        print("not divisible by 8")
else:
    print("not even number")