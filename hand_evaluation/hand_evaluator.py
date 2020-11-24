from typing import List, Optional

from card import Card, Suit, Rank
from hand_evaluation.evaluation import Evaluation
from hand_evaluation.handquickevaluation import HandQuickEvaluation


class HandEvaluator:

    @staticmethod
    def value_hand(hand: List[Card]) -> Evaluation:
        quick_eval = HandQuickEvaluation.HIGH_CARD

        if HandEvaluator._check_for_pair(hand):
            quick_eval = HandQuickEvaluation.ONE_PAIR

        if HandEvaluator._check_for_two_pair(hand):
            quick_eval = HandQuickEvaluation.TWO_PAIR

        if HandEvaluator._check_for_three_of_a_kind(hand):
            quick_eval = HandQuickEvaluation.THREE_OF_A_KIND

        if HandEvaluator._check_for_straight(hand):
            quick_eval = HandQuickEvaluation.STRAIGHT

        if HandEvaluator._check_for_flush(hand):
            quick_eval = HandQuickEvaluation.FLUSH

        if HandEvaluator._check_for_full_house(hand):
            quick_eval = HandQuickEvaluation.FULL_HOUSE

        if HandEvaluator._check_for_four_of_a_kind(hand):
            quick_eval = HandQuickEvaluation.FOUR_OF_A_KIND

        if HandEvaluator._check_for_straight_flush(hand):
            quick_eval = HandQuickEvaluation.STRAIGHT_FLUSH

        if HandEvaluator._check_for_royal_flush(hand):
            quick_eval = HandQuickEvaluation.ROYAL_FLUSH

        return Evaluation(quick_eval, hand)

    @staticmethod
    def _group_by_rank(hand):
        counts = {}
        for card in hand:
            if not counts.__contains__(card.rank):
                counts[card.rank] = 0
            counts[card.rank] += 1
        return counts

    @staticmethod
    def _get_threes(hand) -> List[Rank]:
        grouped = HandEvaluator._group_by_rank(hand)
        threes = {key for (key, value) in grouped.items() if value == 3}
        return list(threes)

    @staticmethod
    def _count_multiple(hand, filter_method):
        counts = HandEvaluator._group_by_rank(hand)
        pair_count = len(list(filter(filter_method, counts.values())))
        return pair_count

    @staticmethod
    def _count_pairs(hand: List[Card]):
        return HandEvaluator._count_multiple(hand, lambda x: x >= 2)

    @staticmethod
    def _check_for_pair(hand: List[Card]):
        return HandEvaluator._count_pairs(hand) == 1

    @staticmethod
    def _check_for_two_pair(hand: List[Card]):
        return HandEvaluator._count_pairs(hand) == 2

    @staticmethod
    def _check_for_three_of_a_kind(hand: List[Card]):
        return HandEvaluator._count_multiple(hand, lambda x: x >= 3)

    @staticmethod
    def _check_for_straight(hand: List[Card]) -> bool:
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
    def _find_flush_suit(hand) -> Optional[Suit]:
        suits = list(Suit)
        for suit in suits:
            suit_count = 0
            for card in hand:
                if card.suit == suit:
                    suit_count += 1

            if suit_count == 5:
                return suit
        return None

    @staticmethod
    def _check_for_flush(hand: List[Card]) -> bool:
        return HandEvaluator._find_flush_suit(hand) is not None

    @staticmethod
    def _check_for_full_house(hand: List[Card]) -> bool:
        threes = HandEvaluator._get_threes(hand)
        if len(threes) == 0:
            return False

        without_first_three = list(filter(lambda x: x.rank != threes[0], hand))
        return HandEvaluator._check_for_pair(without_first_three)

    @staticmethod
    def _check_for_straight_flush(hand: List[Card]) -> bool:
        is_flush = HandEvaluator._check_for_flush(hand)
        if not is_flush:
            return False

        assert (len(hand) <= 7)
        sorted_by_suit = sorted(hand, key=lambda ele: ele.suit.value)
        suit = sorted_by_suit[(len(sorted_by_suit) // 2)].suit

        only_suit_cards = list(filter(lambda e: e.suit == suit, sorted_by_suit))
        return HandEvaluator._check_for_straight(only_suit_cards)

    @staticmethod
    def _check_for_four_of_a_kind(hand: List[Card]):
        return HandEvaluator._count_multiple(hand, lambda x: x >= 4)

    @staticmethod
    def _check_for_royal_flush(hand: List[Card]) -> bool:
        if not HandEvaluator._check_for_straight_flush(hand):
            return False
        color = HandEvaluator._find_flush_suit(hand)
        filtered_cards = list(filter(lambda x: x.suit == color, hand))
        is_straight_flush = HandEvaluator._check_for_straight_flush(filtered_cards)
        contains_ace = len(list(filter(lambda x: x.rank == Rank.ACE, filtered_cards))) > 0
        if is_straight_flush and contains_ace:
            return True
        else:
            return False
