# Current Rules:
# You can place any card of the same suit or any card of the same number

def possibleCard(card1, card2):
    if card1.suit == card2.suit:
        return True
    elif card1.number == card2.number:
        return True
    else:
        return False
