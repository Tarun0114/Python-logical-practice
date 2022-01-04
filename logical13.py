name=input("Enter name")
age= eval(input("Enter age :"))
gender=input("Enter Gender[male/female]: ")
if gender=='male':
    if age>30:
        ms=input("Are you Married? [yes/no]")
        if ms=='yes':
            print(name, "is eligible for Insurance")
        else:
            print(name, "is not eligible for Insurance")
    else:
        print("age is not sufficient")
else:
    if age>25:
        ms=input("Are you Married? [yes/no]")
        if ms=='yes':
            print(name, "is eligible for Insurance")
        else:
            print(name, "is not eligible for Insurance")
            
    else:
        print("age is not sufficient")   