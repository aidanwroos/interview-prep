import random


class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank   # Ace,1,2,3 ... King,Queen
        self.suit = suit   # Hearts, Diamonds, Clubs, Spades
        self.value = value # integer card value
    
    #special python "dunder method" to return card details
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    VALUES = {str(n): n for n in range(2, 11)} | {"Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

    #initialize deck of cards
    def __init__(self):
        self.cards = [
            Card(rank, suit, self.VALUES[rank])
            for rank in self.RANKS
            for suit in self.SUITS
        ]

    def shuffle(self):
        random.shuffle(self.cards)


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = [

        ]

        
    
    


deck = Deck()
for c in deck.cards:
    print(c)
    

