itemDescrip = str(input("Please enter item description. "))

itemQnt = int(input(f"How many {itemDescrip} are you purchasing today? "))

itemPrice = float(input("What is the price of the product? "))

fifteenOff = .15
twentyFiveOff = .25

tax = .065

def finalItemPrice():
    if itemPrice > 19.99:
        return itemPrice * (1 - fifteenOff)
    elif itemPrice > 39.99:
        return itemPrice * (1 - twentyFiveOff)
    else:
        return itemPrice

def salesTax():
    return (finalItemPrice() * itemQnt) * (tax)

def totalPrice():
    return (finalItemPrice() * itemQnt) * (tax + 1)

def savedAmount():
    return (itemPrice * itemQnt) - (finalItemPrice() * itemQnt)

print("Your Receipt")
print("---------------------------")
print(f"{itemQnt} {itemDescrip} priced at {finalItemPrice():,.2f}")
print(f"Sales tax {salesTax():,.2f}")
print(f"Total amount due: {totalPrice():,.2f}")
print(f"You saved {savedAmount():,.2f}")