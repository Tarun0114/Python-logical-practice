p=int(input(' Enter start number='))
n=int(input('Enter end  second number='))
if p<n:
    for i in range(p,n):
        print(i)
elif p>n:
    for i in range(n-1,p):
        print(p)
        p=p-1