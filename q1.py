"""Pure Gems Store sells different varieties of gems to its customers. Emerald, Ivory,
Jasper, Ruby, Garnet and their prices are 1760, 2119, 1599, 3920, 3999 respectively.
Write a Python program to calculate the bill amount to be paid by a customer based on
the list of gems and quantity purchased. Any purchase with a total bill amount above
Rs.30000 is entitled for 5% discount. If any gem required by the customer is not
available in the store, then consider total bill amount to be -1.
Assume that quantity required by the customer for any gem will always be greater than
0. Perform case-sensitive comparison wherever applicable."""
#The program are as follows:
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]
price_list=[1760,2119,1599,3920,3999]
reqd_gems=input("Enter the gems from gems_list: ").split(',')
bill=0
check=False
check=all(item in gems_list for item in reqd_gems)
if check == False:
    bill = -1
    print(f"Total Bill: {bill}")
    exit()
else:
    for i in reqd_gems:
        reqd_quantity = int(input(f"Enter the quantity of gems {i} : "))
        bill=bill+price_list[gems_list.index(i)]*reqd_quantity
if bill>30000:
    bill= bill - bill/20
print(f"Total bill: {bill} ")