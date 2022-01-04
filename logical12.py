quantity = int(input("Enter the required Quantity: "))
price = float(input("price per unit is:"))

if quantity > 200:
    total = quantity*price
    discount = total *(0.2)
    gst = total*(0.18)
    print("Quantity Ordered" ,quantity , "Price per item is Rs.",price , "Total amount" , total , "Discount" , discount , "Gst- ",gst,"Total payable amount" , (total+gst-discount) )
else:
    total = quantity*price
    
    gst = total*(0.18)
    print("Quantity Ordered" ,quantity , "Price per item is Rs.",price , "Total amount" , total , "Gst- ",gst,"Total payable amount" , (total+gst) )