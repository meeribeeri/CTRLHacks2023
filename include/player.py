from random import randint

class Player():
    def __init__(self,deck : list,hp : int = 100,max_hp : int = 100):
        self.hp = hp
        self.max_hp = max_hp
        self.deck = deck
        self.hand = []
        self.discard = []
        while True:
            if len(self.hand) < 5:
                cardDrawn = deck.pop(randint(0,len(deck)-1))
                self.discard.append(cardDrawn)
                self.hand.append(cardDrawn)

    def damage(self, damage_taken : int):
        self.hp-=damage_taken