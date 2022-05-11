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
