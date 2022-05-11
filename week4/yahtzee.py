"""
Create a class for a die (single dice)
    Define any necessary attributes.  Your die class should be able to
        handle any number of sides such as 4, 6, 8, 10, 12, 20, 100, etc.
    Create the following methods for the class:
        __init__ - Constructor method
        roll - Roll the die to get a new random value based on the
            number of sides of the die
        getCurrentFaceValue - Get the value currently showing on the die face
        showDieFace - Display the value currently showing on the die. 
Create a function that rolls five different dice.
    Display the roll results to the screen
    Checks to see if all five dice have the same face value.
        If they do, then print “YAHTZEE” to the screen.
Challenge: Display a die face to the screen instead of the numerical value of the die.  You can find images to use at 
emojipedia.org
"""
import random
class Die:
    def __init__(self, number, sides, faceValue):
        self.number = number
        self.sides = sides
        self.faceValue = faceValue
    
    def roll(self):
        self.faceValue = random.randrange(1, 6, 1)

die1 = Die(1, 6, 1)
die2 = Die(2, 6, 2)
die3 = Die(3, 6, 3)
die4 = Die(4, 6, 4)
die5 = Die(5, 6, 5)
dice = [die1, die2, die3, die4, die5]
rolls = []
def rollDice():
    for dicerolls in range(0, len(dice), 1):
        dice[dicerolls].roll()
        rolls.append(dice[dicerolls].faceValue)
    print(rolls)
    if all(x == rolls[0] for x in rolls):
        print("YAHTZEE!")

rollDice()