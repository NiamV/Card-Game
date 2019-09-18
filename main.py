import os
import requests
import traceback

from flask import *

from wtforms import Form, BooleanField, validators, SubmitField, StringField

from GameWeb import *
from Cards import *
from BasicRules import *

def generateCardSelectForm(hand):
    class CardSelect(Form):
        pass  
        
    for card in hand:
        name = Card(card).number + " " + Card(card).suit
        setattr(CardSelect, str(card), BooleanField())

    setattr(CardSelect, "Pickup", BooleanField())
    setattr(CardSelect, "Play", SubmitField())

    form = CardSelect(request.form)

    return form


app = Flask(__name__)
app.secret_key = b'\xa6\xdd\x99,\xd9F9\xcf\x12\xf6\xf7\x08tk\xd6\x7f\x02C\x8c&\xc7?*\x91'

@app.route('/',  methods = ['POST', 'GET'])

def home():
    return render_template('home.html')

@app.route('/game/', methods = ['POST', 'GET'])

def game():
    # if started == 0:
    #     started += 1

    form = generateCardSelectForm(session["playerHand"])
    
    if request.method == 'POST':
        #Player Turn

        session["playerHand"] = []
        counter = 0

        for field in form:
            if field.name != "Play":
                if field.data:
                    counter += 1

        if counter != 1:
            for field in form:
                if str(field.name) != "Pickup":
                    if str(field.name) != "Play":
                        card = int(str(field.name))
                        session["playerHand"].append(card)
            if counter > 1:
                message = "You entered more than one option, please try again"
            if counter == 0:
                message = "You did not enter an option, please try again"
        
        elif counter == 1:
            message = "Correct input"
            for field in form:
                if field.name == "Pickup":
                    if field.data:
                        takeCard(session["playerHand"], session["UnusedCards"], session["playedCards"])
                elif field.name != "Play":
                    card = int(str(field.name))
                    if field.data == False:
                        session["playerHand"].append(card)
                    else:
                        if possibleCard(Card(card), Card(session["playedCards"][len(session["playedCards"]) - 1])):
                            session["playedCards"].append(card)
                        else:
                            takeCard(session["playerHand"], session["UnusedCards"], session["playedCards"])
                            session["playerHand"].append(card)
                            message = "You played an incorrect card, 1 card penalty"

            #Computer Turn

            played = 0

            for card in session["computerHand"]:
                if possibleCard(Card(card), Card(session["playedCards"][len(session["playedCards"]) - 1])) == True and played == 0:
                    session["playedCards"].append(card)
                    session["computerHand"].remove(card)
                    played = 1
                    compMessage = "The computer played " + Card(card).number + " " + Card(card).suit

            if played == 0:
                takeCard(session["computerHand"], session["UnusedCards"], session["playedCards"])
                compMessage = "The computer picked up a card"

            if len(session["computerHand"]) == 0:
                compMessage = "The Computer Wins :("        

        if len(session["playerHand"]) == 0:
            message = "You win!!!"
        
        form = generateCardSelectForm(session["playerHand"])

        print( len(session["playerHand"]) , len(session["computerHand"]) , len(session["playedCards"]) , len(session["UnusedCards"]))
        print( len(session["playerHand"]) + len(session["computerHand"]) + len(session["playedCards"]) + len(session["UnusedCards"]))

        return render_template(
            'game.html',
            hand = [{"imageurl": Card(card).imagePathWeb(), "name": Card(card).number + " " + Card(card).suit} for card in session["playerHand"]],
            currentCard = Card(session["playedCards"][len(session["playedCards"]) - 1]).imagePathWeb(),
            form = form,
            message = message,
            compMessage = compMessage
        )

    else:
        initialPiles = StartGame()

        session["playerHand"] = initialPiles[0]
        session["computerHand"] = initialPiles[1]
        session["playedCards"] = initialPiles[2]
        session["UnusedCards"] = initialPiles[3]

        form = generateCardSelectForm(session["playerHand"])

        return render_template(
            'game.html',
            hand = [{"imageurl": Card(card).imagePathWeb(), "name": Card(card).number + " " + Card(card).suit} for card in session["playerHand"]],
            currentCard = Card(session["playedCards"][len(session["playedCards"]) - 1]).imagePathWeb(),
            form = form
        )

