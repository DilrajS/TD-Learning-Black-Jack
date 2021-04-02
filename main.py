import Card
import Dealer
import Player
import random
import time

# IMPORTANT VARIABLES AND DICTIONARIES
current_player = 0  # Keeps track of who is playing.
numOfPlayers = 0  # Number of players user wants.
playerDictionary = {}  # Keeps players (& dealer) in a dictionary.
cardDict = {}  # This stores cards that are created.
suitList = ["clubs", "diamonds", "hearts", "spades"]  # List of suits.
valueDictionary = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
                   8: 8, 9: 9, 10: 10, 11: 10, 12: 10, 13: 10, 14: 11}  # How much each card is worth.
# Need to make A worth 11 points (or 14 in list) automatically unless score > 21.


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
# print(playerDictionary)

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

    print("The card drawn is: " + str(c.value))
    playerDictionary[current_player].update_score(c.value)  # Updates player score.
    print(current_player)
    print(playerDictionary[current_player].get_score())


# HIT FUNCTION.
def hit():
    generate_card()  # Calls generate function to generate a new card and updates player score.


# HOLD FUNCTION.
def hold(current_player):
    if current_player + 1 < playerDictionary.__len__():
        current_player += 1
    else:
        pass
        # we can make game end here.
        # switch to dealer (dealer plays)
        # Set the current player back to 0 (Why?)


# COMPARE SCORES FUNCTION.
def compare_scores():
    compare_helper = playerDictionary.__len__()
    for x in range(compare_helper):
        print(playerDictionary[x].score)  # Prints scores of all the players in order, can change when/how needed.


# GAME CODE.
# Create a dealer, give him 1 card (update score with 1 card.)
dealer = Dealer.Dealer(0)  # Creates a dealer object
playerDictionary[len(playerDictionary)] = dealer  # Puts the dealer last int he player dictionary
# print(playerDictionary)

# Give all players 2 cards (update points/score using 2 cards.)
for x in range(len(playerDictionary) - 1):
    generate_card()
    generate_card()
    print("Current score of Player " + str(x) + " is: " + str(playerDictionary[x].score))
    print("------------------------------------------------")
    current_player += 1

# Set current player back to 0 so we can go to Hit / Hold phase.
current_player = 0
hit_check = True

def hit_check_helper():
    print("Enter 1 to hit and 0 to hold.")
    check_for_hit = int(input())
    if check_for_hit == 1:
        hit()
        if playerDictionary[current_player].get_score() > 21:
            hit_check = False
        hit_check_helper()
        print(current_player)
        print(playerDictionary[current_player].get_score())

    elif check_for_hit == 0:
        hold(playerDictionary[current_player])
        hit_check = False
    else:
        hit_check_helper()


while hit_check:
    hit_check_helper()

print(playerDictionary[current_player].get_score())


# GUI.
