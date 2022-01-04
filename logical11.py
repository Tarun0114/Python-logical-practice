invested=50000
term = input("Enter the Fixed Deposit Scheme [Long/Short]")
years=eval(input("Enter the period"))
if term=="long":
    if years>=7:
        total=invested*7.5
        print("Rs.50000 invested in long term scheme, Interest amount per annum is Rs.",total)
        interest=total*7
        print("Rs.",interest,"is the interest that Mr.Ravi will earn after 7 years")
    #else:
        #print("Investement is sufficient")
else :
    total=invested*4.5
    print("Rs.50000 invested in long term scheme, Interest amount per annum is Rs.",total)
    interest=total*6
    print("Rs.",interest,"is the interest that Mr.Ravi will earn after 6 years")
    
    