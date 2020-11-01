from enum import Enum


class Suit(Enum):
    HEARTS = 0
    DIAMONDS = 1
    CLUBS = 2
    SPADES = 3


class Rank(Enum):
    ACE = 14
    KING = 13
    QUEEN = 12
    JACK = 11
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        if not isinstance(suit, Suit):
            raise TypeError('suit must be of type Suit')
        if not isinstance(rank, Rank):
            raise TypeError('rank must be of type Rank')
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank).split('.')[1] + ' OF ' + str(self.suit).split('.')[1]
