import Card
import Dealer
import Player
import time
import random

# Person who is playing
currentPlayer = 0
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

# Generates / stores players.
playerDictionary = {}
for _ in range(numOfPlayers):
    newPlayer = Player.Player(0)
    playerDictionary[_] = newPlayer
print(playerDictionary)

# Generate card function
cardDict = {}  # This stores cards that are created.
# This stores the values of each card.
valueDictionary = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 10, 12: 10, 13: 10, 14: 11}
suitList = ["clubs", "diamonds", "hearts", "spades"]
# How many decks the user wants to use.
deckCount = int(input("Enter a number for how many decks you want to play with: "))


def generate_card():
    # Generating values for a card object
    name = random.randint(1, 13)
    suit = random.randint(1, 4)
    count = 0
    value = int(valueDictionary[name])
    c = Card.Card()

    # Push the values into the object
    c.__int__(name, suit, count, value)

    # Create a card id
    card_key = str(name) + suitList[suit - 1]

    # check in list
    if card_key in cardDict.keys():
        # check for count
        if cardDict[card_key].count < deckCount:
            cardDict[card_key].count += 1
        else:
            generate_card()
    else:
        c.count = 1
        cardDict[card_key] = c

    # Update player score
    playerDictionary[currentPlayer].update_score(c.value)


# Hit function
def hit():
    generate_card()


# Hold function
def hold(currentPlayer):
    if currentPlayer + 1 < playerDictionary.__len__():
        currentPlayer += 1
    else:
        switch to dealer
        Set the current player back to 0
# compare scores
