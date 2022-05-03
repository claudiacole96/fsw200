itemDescrip = str(input("Please enter item description. "))

itemQnt = int(input(f"How many {itemDescrip} are you purchasing today? "))

itemPrice = float(input("What is the price of the product? "))

fifteenOff = 15
twentyFiveOff = 25

def finalItemPrice(itemPrice):
    if itemPrice > 19.99:
        return itemPrice * (100 - fifteenOff)
    elif itemPrice > 39.99:
        return itemPrice * (100 - twentyFiveOff)
    else:
        return itemPrice

def salesTax()

print("Your Receipt")
print("---------------------------")
print(f"{itemDescrip} priced at {finalItemPrice(itemPrice):,.2f}")
print(f"Sales tax {salesTax:,.2f}")
print(f"Total amount due: {totalPrice:,.2f}")
print(f"You saved {savedAmount:,.2f}")