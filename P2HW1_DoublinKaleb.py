# Total Purchases HW
# 02/22/22
# CTI-110 P2HW1 – Total Purchases
#Kaleb Doublin
#
item1 = float(input("Enter the price for item 1: "))
item2 = float(input("Enter the price for item 2: "))
item3 = float(input("Enter the price for item 3: "))
item4 = float(input("Enter the price for item 4: "))
item5 = float(input("Enter the price for item 5: "))

sales_tax = .07
subtotal = float(item1 + item2 + item3 + item4 + item5) 
total_sales_tax = subtotal * sales_tax
total = subtotal + total_sales_tax

print('\nTotal = $', format(total, ',.2f’), sep= '', end='\n’)
