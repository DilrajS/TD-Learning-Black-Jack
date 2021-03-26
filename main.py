import Card
import Dealer
import Player
import time
import random

# Asks User for input on number of players.
inputCheck = False
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

print(numOfPlayers)

# create that many players
playerNames = ["player1", "player2", "player3"]
for x in range(numOfPlayers):
    print(playerNames[x])
    playerNames[x] == Player(0)

# distribute initial cards to dealer & players
# choose hit of hold
# compare scores
