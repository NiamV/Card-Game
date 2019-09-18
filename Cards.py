import math

idToNumber = {
    0: "king",
    1: "ace",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "jack",
    12: "queen"
}

idToSuit = {
    0: "clubs",
    1: "diamonds",
    2: "hearts",
    3: "spades",
}

class Card:
    def __init__(self, id):
        self.id = id
        self.suit = idToSuit[math.floor((id-1) / 13)]
        self.number = idToNumber[id % 13]
    
    def imagePath(self):
        path = "static/" + self.number + "_of_" + self.suit + ".png"
        return path

    def imagePathWeb(self):
        path = self.number + "_of_" + self.suit + ".png"
        return path

    def name(self):
        name = self.number + self.suit
        return name


# card = Card(22)

# from PIL import Image

# cardImage = Image.open(card.imagePath())
# cardImage.show()

