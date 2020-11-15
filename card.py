from enum import Enum


class Suit(Enum):
    HEARTS = 0
    DIAMONDS = 1
    CLUBS = 2
    SPADES = 3

    def to_unicode(self):
        if self == Suit.HEARTS:
            return '♥'
        if self == Suit.DIAMONDS:
            return '♦'
        if self == Suit.CLUBS:
            return '♣'
        if self == Suit.SPADES:
            return '♠'


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

    def to_short_string(self):
        if self.value <= 10:
            return str(self.value)
        else:
            return str(self).split('.')[1][0]


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        if not isinstance(suit, Suit):
            raise TypeError('suit must be of type Suit')
        if not isinstance(rank, Rank):
            raise TypeError('rank must be of type Rank')
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank.to_short_string()) + str(self.suit.to_unicode())
