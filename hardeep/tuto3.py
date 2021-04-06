from collections import namedtuple
import random

Card = namedtuple("Card", ["rank", "suit"])


class FrenchDeck:

    ranks = [x for x in range(2, 11)] + list("JKQA")
    suits = ["Clubs", "Spade", "Heart", "Diamond"]

    def __init__(self):
        self.cards = [(Card(rank, suit)) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __setitem__(self, key, value):
        self.cards[key] = value


deck = FrenchDeck()
x = FrenchDeck

x = random.choice(deck)
print(x)


for cards in deck:

    random.shuffle(deck)
    print(cards)

"""
class variable
data classes
dunder,

"""
