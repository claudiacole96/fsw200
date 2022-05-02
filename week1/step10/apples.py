applePrice = .50

customerName = str(input("Welcome to Bonny's Apples! What is your name? "))
print(f"Hi, {customerName}")

print(f"Would you like to buy any apples? Our apples are ${applePrice:.2f} each.")
appleQnt = int(input("How many would you like to buy? "))

def TotalCost(qnt, price):
    return qnt * price

print(f"Thank you for buying {appleQnt} apples, {customerName}! Your total is ${TotalCost(appleQnt, applePrice):,.2f}!")