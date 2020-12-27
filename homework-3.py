name=input(f"Please enter your name: ")
print('Welcome ' + name +'! Lets play a game')
import random as rnd
words=["bangkok",
       "paris",
       "london",
       "dubai",
       "singapore",
       "istanbul",
       "tokyo",
       "berlin",
       "roma",
       "amsterdam"]
wordChosen = ""
wordVisualization = ""
maxGuesses = 10
currentGuessesCounter = 0
lettersGuessed = []
currentGuess = ""
while True:
    wordChosen = rnd.choice(words)
    lettersGuessed = len(wordChosen) * "_"
    currentGuesses = 0
    print("You should guess what word I am thinking of. Otherwise, someone gonna dies because of you.")
    print("This word is ", len(lettersGuessed), " letters and one of the most popular cities in the world.")
    print("Remember, you have only 10 attempts")
    while currentGuessesCounter < maxGuesses:
        currentGuess = input("Enter a letter: ")
        for i in range(0, len(wordChosen)):
            if wordChosen[i] == currentGuess:
                lettersGuessed = lettersGuessed[:i] + currentGuess + lettersGuessed[i+1:]
                print("Congratulations!")
                print(lettersGuessed)
        if wordChosen == lettersGuessed:
            print("Someone's life was saved thanks to you!")
            exit()
        currentGuessesCounter+=1
    print("GAME OVER!!!")
    print("The word was:", wordChosen)
    break
          
