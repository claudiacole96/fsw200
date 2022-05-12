invalidMsg = "Invalid Input... Not a positive number."

while True: 
    numberInput = (input("Please enter a positive number: "))
    if numberInput.isnumeric():
        if int(numberInput) > 0:
            for x in range(0, (int(numberInput)+1), 2):
                print(x)
        else:
            print(invalidMsg)
    else:
        print(invalidMsg)
