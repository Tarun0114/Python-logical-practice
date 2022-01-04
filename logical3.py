n=int(input("Enter a number :"))

z = int('%d%d' % (n, n))
x = int('%d%d' % (n, z))
s=n+z+x
print("The value is: ",s)