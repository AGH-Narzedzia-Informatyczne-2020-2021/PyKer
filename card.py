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
    def __init__(self, suit: Suit = None, rank: Rank = None, string: str = ''):

        if string != '':
            suit = string[-1]
            rank = string[:-1]
            self.suit = Card._str_to_suit(suit)
            self.rank = Card._str_to_rank(rank)
        else:
            if not isinstance(suit, Suit):
                raise TypeError('suit must be of type Suit')
            if not isinstance(rank, Rank):
                raise TypeError('rank must be of type Rank')
            assert(Suit is not None)
            assert(Rank is not None)

            self.suit = suit
            self.rank = rank

    # TODO maybe move these to suit and rank classes

    @staticmethod
    def _str_to_suit(string: str):
        if not ['h', 'd', 'c', 's'].__contains__(string.lower()):
            raise ValueError(f'could not resolve suit: {string}')
        suits = {'h': Suit.HEARTS, 'd': Suit.DIAMONDS, 'c': Suit.CLUBS, 's': Suit.SPADES}
        return suits[string.lower()]

    @staticmethod
    def _str_to_rank(string: str):
        if len(string) == 2:
            if string != '10':
                raise ValueError(f'could not resolve suit: {string}')
            return Rank.TEN

        if len(string) == 1:
            ranks = {'A': Rank.ACE, 'K': Rank.KING, 'Q': Rank.QUEEN, 'J': Rank.JACK, '9': Rank.NINE, '8': Rank.EIGHT,
                     '7': Rank.SEVEN, '6': Rank.SIX, '5': Rank.FIVE, '4': Rank.FOUR, '3': Rank.THREE, '2': Rank.TWO}
            if not ranks.__contains__(string):
                raise ValueError(f'could not resolve rank {string}')
            return ranks[string]

        raise ValueError('String is too long or too short to be a card')

    def __str__(self):
        return str(self.rank.to_short_string()) + str(self.suit.to_unicode())
