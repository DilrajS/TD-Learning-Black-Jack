import Card
import Dealer
import Player
import random
import time

# IMPORTANT VARIABLES AND DICTIONARIES
current_player = 0  # Keeps track of who is playing.
numOfPlayers = 0  # Number of players user wants.
playerDictionary = {}  # Keeps players in a dictionary.
cardDict = {}  # This stores cards that are created.
valueDictionary = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
                   8: 8, 9: 9, 10: 10, 11: 10, 12: 10, 13: 10, 14: 11}  # How much each card is worth.
suitList = ["clubs", "diamonds", "hearts", "spades"]  # List of suits.

# CREATING PLAYER(S).
inputCheck = False
while not inputCheck:  # Asks user how many players will play.
    try:
        numOfPlayers = int((input("How many players are going to play (0 - 3)? : \n")))
        if type(numOfPlayers) == int:
            inputCheck = True
    except ValueError:
        print("Incorrect input, try again.")

# Caps number of players.
if numOfPlayers > 3:
    numOfPlayers = 3

# Generate and store players in a dictionary.
for _ in range(numOfPlayers):
    newPlayer = Player.Player(0)
    playerDictionary[_] = newPlayer
print(playerDictionary)

# GENERATE CARDS.
deckCount = int(input("Enter a number for how many decks you want to play with: "))  # How many decks to use.


def generate_card():
    # Generating values for a card object
    name = random.randint(1, 13)
    suit = random.randint(1, 4)
    count = 0
    value = int(valueDictionary[name])
    c = Card.Card()
    c.__int__(name, suit, count, value)  # Push the values into the object.
    card_key = str(name) + suitList[suit - 1]  # Creates a card ID to store the card in the dictionary.

    if card_key in cardDict.keys():  # Check if card already exists in the dictionary by searching for the card ID.
        if cardDict[card_key].count < deckCount:  # If found in dictionary, checks if possible to create another card.
            cardDict[card_key].count += 1
        else:
            generate_card()  # If found in dictionary, but not possible to create another card, generates a new card.
    else:
        c.count = 1  # If card not in dictionary, adds it and increases card count.
        cardDict[card_key] = c

    playerDictionary[current_player].update_score(c.value)  # Updates player score.


# HIT FUNCTION.
def hit():
    generate_card()  # Calls generate function to generate a new card and updates player score.


# HOLD FUNCTION.
def hold(current_player):
    if current_player + 1 < playerDictionary.__len__():
        current_player += 1
    else:
        pass
        # switch to dealer
        # Set the current player back to 0

# compare scores
