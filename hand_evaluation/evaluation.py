from typing import List

from card import Card
from hand_evaluation.hand import Hand


class Evaluation:
    def __init__(self, hand: Hand, cards: List[Card]):
        self.hand = hand
        self.cards = cards

    def __cmp__(self, other):
        if self.hand == other.hand:
            # TODO should compare the hands by the higher card where applicable
            return 0
        else:
            return self.hand - other.hand
