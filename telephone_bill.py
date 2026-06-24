print("Enter Contact No")
cnt=int(input())
print("Enter No of calls")
noc=int(input())
if noc<=100:
    grossBill=noc*1
elif noc>100 and noc<=200:
    grossBill=100*1+(noc-100)*0.5
elif noc>200 and noc<=300:
    grossBill=100*1+(100*0.5)+(noc-200)*0.25
elif noc>300:
    grossBill=100*1+(100*0.5)+(100*0.25)+(noc-300)*0.1
tax=(grossBill*18)/100
print("Contact No    ",cnt)
print("No of Calls   ",noc)
print("Gross Bill    ",grossBill)
print("Tax           ",tax)
print("Net Bill      ",grossBill+tax)
