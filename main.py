from Card import *
from Dealer import *
from Player import *
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

# create that many players
if numOfPlayers == 3:
    p1 = Player(0)
    p2 = Player(0)
    p3 = Player(0)
elif numOfPlayers == 2:
    p1 = Player(0)
    p2 = Player(0)
elif numOfPlayers == 1:
    p1 = Player(0)
else:
    pass

# Function to create a new card
int(input("Enter a number for how many decks you want to play with: "))
# Once card is used add to dictionary

# Check if card has been used


# Hit function

# Hold function

# compare scores
