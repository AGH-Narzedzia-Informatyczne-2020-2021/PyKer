import unittest

from card import *
from hand_evaluation.handquickevaluation import HandQuickEvaluation
from hand_evaluation.hand_evaluator import HandEvaluator


class MyTestCase(unittest.TestCase):

    # High card
    def test_find_high_card(self):
        self.assertEqual(HandEvaluator.value_hand(high_card), HandQuickEvaluation.HIGH_CARD)

    # Pair

    def test_find_pair(self):
        hand_one = [Card(Suit.HEARTS, Rank.TEN), Card(Suit.SPADES, Rank.TEN)]
        self.assertEqual(HandEvaluator.value_hand(hand_one), HandQuickEvaluation.ONE_PAIR)

    def test_pair_is_equal(self):
        hand_one = [Card(Suit.HEARTS, Rank.TEN), Card(Suit.SPADES, Rank.TEN)]
        hand_two = [Card(Suit.CLUBS, Rank.TEN), Card(Suit.DIAMONDS, Rank.TEN)]
        self.assertEqual(HandEvaluator.value_hand(hand_one), HandEvaluator.value_hand(hand_two))

    def test_stronger_pair_wins(self):
        hand_one = [Card(Suit.HEARTS, Rank.TEN), Card(Suit.SPADES, Rank.TEN)]
        hand_two = [Card(Suit.CLUBS, Rank.NINE), Card(Suit.DIAMONDS, Rank.NINE)]
        self.assertNotEqual(HandEvaluator.value_hand(hand_one), HandEvaluator.value_hand(hand_two))

    # Two Pair

    # Three of a kind

    # Straight

    def test_find_straight(self):
        self.assertTrue(HandEvaluator.check_for_straight(straight))
        self.assertTrue(HandEvaluator.check_for_straight(straight_flush))

    def test_find_no_straight(self):
        self.assertFalse(HandEvaluator.check_for_straight(flush))

    # Flush

    def test_find_flush(self):
        self.assertTrue(HandEvaluator.check_for_flush(flush))
        self.assertTrue(HandEvaluator.check_for_flush(straight_flush))

    def test_check_if_not_flush(self):
        self.assertFalse(HandEvaluator.check_for_flush(straight))

    def test_find_royal_flush(self):
        self.assertTrue(HandEvaluator.check_for_straight_flush(straight_flush))

    # Four of a kind


if __name__ == '__main__':
    unittest.main()


def str_to_card(card_string: str):
    return Card(string=card_string)


def list_to_cards(card_list):
    return list(map(str_to_card, card_list))


straight_flush = list_to_cards(['10s', '8s', '9s', 'Js', 'Qs'])

flush = list_to_cards(['10s', 'As', 'Ks', '2s', '5s', 'Qd', '3d'])

straight = list_to_cards(['10d', '9h', '8c', '7s', '6c', 'Ad'])

one_pair = list_to_cards(['8s', '8d', 'Ad', 'Jc'])

two_pair = one_pair.__add__([Card(string='Ah')])

full_house = two_pair.__add__([Card(string='As')])

high_card = list_to_cards(['Ad', 'Qh', '10c', '2d', '5d'])
