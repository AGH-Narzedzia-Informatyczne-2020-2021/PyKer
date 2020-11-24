from card import Card, Suit, Rank
import random


class Deck:

    def __init__(self):
        self.cards = []
        self._create_deck()

    def _create_deck(self):
        for i in range(0, 4):
            for j in range(2, 15):
                self.cards.append(Card(Suit(i), Rank(j)))

    def shuffle(self):
        random.shuffle(self.cards)

    def top(self):
        return self.cards.pop()
