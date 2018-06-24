# CTI-110 
# P3HW2 - Software_Sales
# Adam Klover
# 06/24/18

NumberOfPackages = int(input("Please enter number of packages"+ \
                             " you're buying: "))
packagePrice = 99

if NumberOfPackages < 10:
    discount = 0;
elif NumberOfPackages < 20:
    discount = 0.10
elif NumberOfPackages < 50:
    discount = 0.20
elif NumberOfPackages < 100:
    discount = 0.30
elif NumberOfPackages >= 100:
    discount = 0.40

subTotal = NumberOfPackages * packagePrice
amountOFdiscount = discount * subTotal
total = subTotal - amountOFdiscount

print( "\nAmount of discount: $" + format( amountOFdiscount, ",.2f") + \
       "\nTotal amount: $" + format( total,",.2f" ))
