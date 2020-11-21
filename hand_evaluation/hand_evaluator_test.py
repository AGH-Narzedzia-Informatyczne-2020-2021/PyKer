import unittest

from card import *
from hand_evaluation.hand_evaluator import HandEvaluator
from hand_evaluation.handquickevaluation import HandQuickEvaluation


class MyTestCase(unittest.TestCase):

    # High card
    def test_high_card(self):
        hand = list_to_cards(['Ah', 'Qd', '10c', ])
        self.assertEqual(HandEvaluator.value_hand(hand).quick_eval, HandQuickEvaluation.HIGH_CARD)

    # Pair
    def test_pair(self):
        hand = list_to_cards(['Ah', 'Kc', 'Ad', '9h', '4c'])
        self.assertEqual(HandEvaluator.value_hand(hand).quick_eval, HandQuickEvaluation.ONE_PAIR)
        self.assertEqual(HandEvaluator.value_hand(one_pair).quick_eval, HandQuickEvaluation.ONE_PAIR)

    def test_pair_is_equal(self):
        hand_one = list_to_cards(['10h', '10s'])
        hand_two = list_to_cards(['10c', '10d'])
        self.assertEqual(HandEvaluator.value_hand(hand_one).quick_eval, HandEvaluator.value_hand(hand_two).quick_eval)

    # Two Pair
    def test_two_pair(self):
        hand = list_to_cards(['Ah', 'Ac', '10c', '10s', '2d', '5d'])
        self.assertEqual(HandEvaluator.value_hand(hand).quick_eval, HandQuickEvaluation.TWO_PAIR)
        self.assertEqual(HandEvaluator.value_hand(two_pair).quick_eval, HandQuickEvaluation.TWO_PAIR)

    # Three of a kind
    def test_three_of_a_kind(self):
        hand = list_to_cards(['Ah', 'Ac', 'Ah', '10c', '4h', '3c'])
        self.assertEqual(HandEvaluator.value_hand(hand).quick_eval, HandQuickEvaluation.THREE_OF_A_KIND)

    # Straight
    def test_find_straight(self):
        straight = list_to_cards(['10d', '9h', '8c', '7s', '6c', 'Ad'])
        self.assertEqual(HandEvaluator.value_hand(straight).quick_eval, HandQuickEvaluation.STRAIGHT)

    # Flush
    def test_find_flush(self):
        flush = list_to_cards(['10s', 'As', 'Ks', '2s', '5s', 'Qd', '3d'])
        self.assertEqual(HandEvaluator.value_hand(flush).quick_eval, HandQuickEvaluation.FLUSH)

    # Full House
    def test_full_house(self):
        hand = list_to_cards(['Ah', 'Ac', '10h', '10c', '10s', '5h', '9c'])
        self.assertEqual(HandEvaluator.value_hand(hand).quick_eval, HandQuickEvaluation.FULL_HOUSE)

    # Four of a kind
    def test_find_four_of_a_kind(self):
        hand = list_to_cards(['Ah', 'Ad', 'Ac', 'As', 'Ks', '9s', '2h'])
        self.assertEqual(HandEvaluator.value_hand(hand).quick_eval, HandQuickEvaluation.FOUR_OF_A_KIND)

    # Straight Flush
    def test_find_straight_flush(self):
        hand = list_to_cards(['Qh', 'Jh', '10h', '9h', '8h', '4c', 'Qs'])
        self.assertEqual(HandEvaluator.value_hand(hand).quick_eval, HandQuickEvaluation.STRAIGHT_FLUSH)

    # Royal Flush
    def test_find_royal_flush(self):
        hand = list_to_cards(['Ah', 'Kh', 'Qh', 'Jh', '10h', '7c', '3s'])
        self.assertEqual(HandEvaluator.value_hand(hand).quick_eval, HandQuickEvaluation.ROYAL_FLUSH)


if __name__ == '__main__':
    unittest.main()


def str_to_card(card_string: str):
    return Card(string=card_string)


def list_to_cards(card_list):
    return list(map(str_to_card, card_list))


one_pair = list_to_cards(['8s', '8d', 'Ad', 'Jc'])

two_pair = one_pair.__add__([Card(string='Ah')])

full_house = two_pair.__add__([Card(string='As')])
