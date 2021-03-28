import Card
import Dealer
import Player
import time
import random

# Asks User for input on number of players.
inputCheck = False
numOfPlayers = 0
while not inputCheck:
    try:
        numOfPlayers = int((input("How many players are going to play (0 - 3)? : \n")))
        if type(numOfPlayers) == int:
            inputCheck = True
    except ValueError:
        print("Incorrect input, try again.")

# Caps number of players.
if numOfPlayers > 3:
    numOfPlayers = 3

# Generates players.
playerDictionary = {}
for _ in range(numOfPlayers):
    newPlayer = Player.Player(0)
    playerDictionary[_] = newPlayer.score
# print(playerDictionary)

# Generate card function
cardDictionary = {}  # This stores cards that are created.
# This stores the values of each card.
valueDictionary = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 10, 12: 10, 13: 10, 14: 10}
# How many decks the user wants to use.
deckCount = int(input("Enter a number for how many decks you want to play with: "))
name = 0
suit = 0
count = deckCount
value = valueDictionary[name]
print("This is the value of the generated card." + value)

for x in range(10):
    pass



# Once card is used add to dictionary

# Check if card has been used

# Hit function

# Hold function

# compare scores
