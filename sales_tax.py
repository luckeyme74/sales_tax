cost = 1
totalCost = 0

print("This program will calculate your total, including sales tax.")
print("Enter your prices. After the last price is entered, enter 0.")

while cost != 0:
    strCost = raw_input("Enter the price: ")
    cost = float(strCost)
    totalCost += cost
else:
    print ("The total amount of your purchases, before tax, is $" + str(totalCost))

tax = totalCost * .06

print("The total tax on your purchases is " + str(round(tax, 2)))
grandTotal = float(tax) + totalCost
print("The grand total of your purchases plus sales tax is: $" + str(round(grandTotal, 2)))
