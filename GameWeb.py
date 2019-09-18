import random
from Cards import Card
from BasicRules import possibleCard

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

def takeCard(hand, UnusedCards, playedCards):
    if len(UnusedCards) == 0:
        if len(playedCards) == 0:
            return "No cards remaining!"
        else:
            card = playedCards.pop()
            UnusedCards = Shuffle(playedCards)
            playedCards.append(card)

    hand.append(UnusedCards.pop())

def StartGame():
    packOfCards = [i for i in range(1, 53)]

    UnusedCards = Shuffle(packOfCards)

    playerHand = []                     # The player's set of cards
    computerHand = []                   # The computer's set of cards

    playedCards = []                    # The set of cards that have already been played

    for i in range(0,7):                            # Generates the hand of the computer and player
        playerHand.append(UnusedCards.pop())
        computerHand.append(UnusedCards.pop())

    takeCard(playedCards, UnusedCards, playedCards)

    return playerHand, computerHand, playedCards, UnusedCards  