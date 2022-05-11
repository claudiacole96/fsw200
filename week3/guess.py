word = "TUXEDO"
guesses = 5
guessedLetters = []
wordBoard = ["_","_","_","_","_","_"]

def showBoard():
    print(wordBoard)

def checkGuess(guess):
    return guess in word

print("Can you guess this 6 letter word?")
while guesses > 0 and "_" in wordBoard:
    showBoard()
    guess = (str(input("Guess a letter: "))).upper()

    if guess in guessedLetters:
        print("I'm sorry you've already guessed that letter, please try again.")
    else:
        guessedLetters.append(guess)
        if checkGuess(guess):
            print(f"Yes! There is a {guess} in the word!")
            for index, letter in enumerate(word):
                if(letter == guess):
                    wordBoard[index] = guess
        else:
            guesses = guesses -1
            print(f"I'm sorry, but there is no {guess} in the word.")
            if guesses == 1:
                print(f"You have {guesses} guess remaining.")
            else:
                print(f"You have {guesses} guesses remaining.")

if guesses == 0:
    print("You have ran out of chances.")
    print(f"You have lost the game.. the word was {word}")
else:
    showBoard()
    print("You won the game!")