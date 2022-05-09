userActive = True 

while userActive: 
    numberInput = (input("Please enter an even number: "))
    if numberInput.isnumeric():
        if int(numberInput) % 2 == 0:
            for x in range(0, (int(numberInput)+1), 2):
                print(x)
        else:
            print("Invalid Input... ")
    else:
        print("Invalid Input... ")
