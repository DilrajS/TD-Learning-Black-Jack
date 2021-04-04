import Card
import Dealer
import Player
import random
# import time

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
            print("The card drawn is: " + str(c.value))
            playerDictionary[current_player].update_score(c.value)  # Updates player score.
        else:
            generate_card()  # If found in dictionary, but not possible to create another card, generates a new card.
    else:
        c.count = 1  # If card not in dictionary, adds it and increases card count.
        cardDict[card_key] = c
        print("The card drawn is: " + str(c.value))
        playerDictionary[current_player].update_score(c.value)  # Updates player score.


# HIT FUNCTION.
def hit():
    generate_card()  # Calls generate function to generate a new card and updates player score.


# HOLD FUNCTION.
def hold():
    global current_player
    if current_player + 1 < numOfPlayers:  # If there is another player after the current player do this.
        current_player += 1  # Switches to the next player
        hit_check_helper()  # Calls hit_check_helper so next player can hit/hold.
    else:  # If the last player chose to hold, do the following.
        current_player += 1  # Switches to dealer (in the player library)


# COMPARE SCORES FUNCTION.
def compare_scores():  # If you bust or have a lower score than dealer, you lose.
    score_list = []
    for i in range(numOfPlayers + 1):
        if i <= numOfPlayers - 1:
            if playerDictionary[i].score == 0:
                score_list.append("Player " + str(i + 1) + ": Loss")
            elif playerDictionary[i].score >= 22:
                score_list.append("Player " + str(i + 1) + ": Loss")
            else:
                if playerDictionary[_].score >= dealer.score:
                    score_list.append("Player " + str(_ + 1) + ": Win")
                else:
                    score_list.append("Player " + str(_ + 1) + ": Loss")
        else:
            if playerDictionary[i].score == 0:
                score_list.append("Dealer Loss")
            elif playerDictionary[i].score >= 22:
                score_list.append("Dealer Loss")
            else:
                score_list.append("Dealer Win")
    print(score_list)


# GAME CODE.
# Create a dealer, give him 1 card (update score with 1 card.)
dealer = Dealer.Dealer(0)  # Creates a dealer object
playerDictionary[len(playerDictionary)] = dealer  # Puts the dealer last int he player dictionary
# print(playerDictionary)

# Give all players 2 cards (update points/score using 2 cards.)
for x in range(numOfPlayers):
    generate_card()
    generate_card()
    print("Current score of Player " + str(x + 1) + " is: " + str(playerDictionary[x].score))
    print("------------------------------------------------")
    current_player += 1
print("All players have been dealt cards! Switching to Hit/Hold phase... \n")
# Set current player back to 0 so we can go to Hit / Hold phase.
current_player = 0
hit_check = True


def hit_check_helper():
    global hit_check
    global current_player
    print("Current Player: " + str(current_player + 1) + " | Current Score: " +
          str(playerDictionary[current_player].get_score()))
    print("Enter 1 to hit and 0 to hold.")
    check_for_hit = int(input())
    if check_for_hit == 1:
        hit()
        if playerDictionary[current_player].get_score() > 21:
            print("New score is: " + str(playerDictionary[current_player].get_score()))
            print("Bust. Switching player...")
            playerDictionary[current_player].bust()
            hold()
    elif check_for_hit == 0:
        if current_player == len(playerDictionary):
            hit_check = False
        else:
            hold()
    else:
        print("Error: Only values of 1 and 0 are accepted.")
        hit_check_helper()


while hit_check and current_player < numOfPlayers:
    hit_check_helper()

# Dealer part
while dealer.get_score() <= 17:  # Code for how the Dealer plays, if his score is < 17, heep hitting.
    hit()
    print("Dealer's score is: " + str(dealer.get_score()))
if dealer.score > 21:  # If dealer hits over 21, it prints out Dealer busted.
    dealer.bust()
    print("Dealer bust.")

compare_scores()  # Compares all the scores by calling the compare scores method

# GUI.
