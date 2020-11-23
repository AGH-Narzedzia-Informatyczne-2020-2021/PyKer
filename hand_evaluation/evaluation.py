from typing import List

from card import Card
from hand_evaluation.handquickevaluation import HandQuickEvaluation


class Evaluation:
    def __init__(self, quick_eval: HandQuickEvaluation, cards: List[Card]):
        self.quick_eval = quick_eval
        self.cards = cards

    def __cmp__(self, other):
        if self.quick_eval == other.quick_eval:
            # TODO should compare the hands by the higher card where applicable
            return 0
        else:
            return self.quick_eval - other.quick_eval
