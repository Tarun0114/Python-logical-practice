cgos=int(input("Enter cost of goods sold (cgos) : "))
re=int(input("Enter revenue generated: "))
oc=int(input("Enter operating cost : "))
np=re-cgos-oc
print("Gross profit is 2500 Net profit is: ",np)
per=(np/re)*100
print("Net profit percentage is :",per)