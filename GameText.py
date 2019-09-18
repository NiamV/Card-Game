import random
from Cards import Card
from BasicRules import possibleCard

packOfCards = [Card(i) for i in range(1, 53)]

def Shuffle(pack): # pack is an array of cards
    shuffledPack = []

    numberOfCards = len(pack)
    unshuffledPack = [i for i in range(0, numberOfCards)]

    shuffledIDs = []

    for i in range(0,numberOfCards):
        nextCard = random.randint(0, len(unshuffledPack)-1)
        shuffledIDs.append(unshuffledPack[nextCard])
        unshuffledPack.remove(unshuffledPack[nextCard])

    for id in shuffledIDs:
        shuffledPack.append(pack[id])

    return shuffledPack

UnusedCards = Shuffle(packOfCards)    # Cards in the pile to be taken

# To add to a stack use append, to remove use pop
# shuffledPack has the top card at the end of the list

playerHand = []                     # The player's set of cards
computerHand = []                   # The computer's set of cards

playedCards = []                    # The set of cards that have already been played

for i in range(0,7):                            # Generates the hand of the computer and player
    playerHand.append(UnusedCards.pop())
    computerHand.append(UnusedCards.pop())

def takeCard(hand, UnusedCards, playedCards):
    if len(UnusedCards) == 0:
        if len(playedCards) == 0:
            return "No cards remaining!"
        else:
            UnusedCards = Shuffle(playedCards)

    hand.append(UnusedCards.pop())

def printHand(hand):
    i = 1
    for card in hand:
        print(i, ":", card.number, card.suit)
        i += 1

# The Game

takeCard(playedCards, UnusedCards, playedCards)             #Plays the first card

while True:
    #Player turn
    printHand(playerHand)
    print(" ")

    print("The current card is:", playedCards[len(playedCards)-1].number, playedCards[len(playedCards)-1].suit)
    print(" ")
    
    print("Please enter the card number or TAKE to take a new card")

    action = input("Which card number: ")
    print(" ")

    if action == "TAKE":
        takeCard(playerHand, UnusedCards, playedCards)
    elif action == "END":
        break
    else:
        try:
            placedCard = playerHand[int(action) - 1]
            if possibleCard(placedCard, playedCards[len(playedCards)-1]) == True:
                playerHand.remove(placedCard)
                playedCards.append(placedCard)
            else:
                print("Incorrect card, 1 card penalty")
                print(" ")
                takeCard(playerHand, UnusedCards, playedCards)
        except:
            print("Incorrect input, try again!")
            print(" ")
            continue

    if len(playerHand) == 0:
        print("You Win!!!!")
        break

    #Computer Turn

    played = 0

    for card in computerHand:
        if possibleCard(card, playedCards[len(playedCards)-1]) == True and played == 0:
            playedCards.append(card)
            computerHand.remove(card)
            played = 1
            print("The computer played " + card.number + " " + card.suit)
            print(" ")

    if played == 0:
        takeCard(computerHand, UnusedCards, playedCards)
        print("The computer picked up a card")
        print(" ")

    if len(computerHand) == 0:
        print("The Computer Wins :(")
        break
            



