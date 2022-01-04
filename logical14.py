name = input("Employee Name: ")

exp = int(input("experience :"))

gender = input("Your Gender: ")

qualification = input("Your qualification: ")

if exp >= 10 and gender == 'male' and qualification == 'pg' :
    print("Yes" ,name ," is eligible for the Job with a salary of Rs.75000")
elif exp >= 10 and gender == 'female'and qualification == 'pg':
    print("Yes" ,name ," is eligible for the Job with a salary of Rs.60000") 
elif exp >5 and exp <10 and gender == 'male'and qualification == 'pg':
    print("Yes" ,name ," is eligible for the Job with a salary of Rs.60000") 
elif exp >5 and exp <10 and gender == 'male'  and qualification == 'graduate':
    print("Yes" ,name ," is eligible for the Job with a salary of Rs.35000")
elif exp >5 and exp <10 and gender == 'female' and qualification == 'graduate' :
    print("Yes" ,name ," is eligible for the Job with a salary of Rs.20000")
if exp >= 10 and gender == 'male' and qualification == 'graduate' :
    print("Yes" ,name ," is eligible for the Job with a salary of Rs.50000")
elif exp >= 10 and gender == 'female'and qualification == 'graduate':
    print("Yes" ,name ," is eligible for the Job with a salary of Rs.30000")