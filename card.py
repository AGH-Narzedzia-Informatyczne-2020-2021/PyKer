from enum import Enum


class Card:
    def __init__(self, suit, rank):
        if not isinstance(suit, Suit):
            raise TypeError('suit must be of type Suit')
        if not isinstance(rank, Rank):
            raise TypeError('rank must be of type Rank')
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank).split('.')[1] + ' OF ' + str(self.suit).split('.')[1]


class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4


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
