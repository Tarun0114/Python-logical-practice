n=int(input("Enter n value: "))
i=1
print("Even numbers: ")
while(i<=n):
    if i%2==0:
        print(i,end=' ')
    i=i+1

print('odd numbers : ')
for i in range(1,n):
    if i%2!=0:
        print(i,end=' ')
    i=i+1
       
    
    