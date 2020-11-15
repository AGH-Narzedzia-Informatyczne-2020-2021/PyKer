from typing import List

from card import Card, Suit
from hand_evaluation.evaluation import Evaluation


class HandEvaluator:

    @staticmethod
    def value_hand(hand: List[Card]) -> Evaluation:
        # TODO
        return 0

    @staticmethod
    def check_for_straight(hand: List[Card]) -> bool:
        sorted_hand = sorted(hand, key=lambda ele: ele.rank.value)
        if len(sorted_hand) < 5:
            return False

        streak = 1

        for i in range(len(sorted_hand)):
            if i > 0 and abs(sorted_hand[i].rank.value - sorted_hand[i - 1].rank.value) == 1:
                streak += 1
                if streak == 5:
                    return True
            else:
                streak = 1

        return streak == 5

    @staticmethod
    def check_for_flush(hand: List[Card]) -> bool:
        suits = list(Suit)
        for suit in suits:
            suit_count = 0
            for card in hand:
                if card.suit == suit:
                    suit_count += 1

            if suit_count == 5:
                return True

        return False

    @staticmethod
    def check_for_straight_flush(hand: List[Card]) -> bool:
        is_flush = HandEvaluator.check_for_flush(hand)
        if not is_flush:
            return False

        assert (len(hand) <= 7)
        sorted_by_suit = sorted(hand, key=lambda ele: ele.suit.value)
        suit = sorted_by_suit[(len(sorted_by_suit) // 2)].suit

        only_suit_cards = list(filter(lambda e: e.suit == suit, sorted_by_suit))
        return HandEvaluator.check_for_straight(only_suit_cards)
