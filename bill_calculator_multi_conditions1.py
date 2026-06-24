print("Enter Price")
price=int(input())
print("Enter Quantity")
qty=int(input())
print("Price    ", price)
print("Quantity ", qty)
print("Gross Bill", price*qty)
grossBill =price*qty
dis=grossBill/10
noDis=0
if grossBill>=5000 and qty>=3:
    print("Discount ", dis)
    print("Net Bill ", grossBill-dis)
else:
    print("Discount ", noDis)
    print("Net Bill", grossBill)

#Completed


    
    
