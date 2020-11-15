import unittest

from card import *
from hand_evaluation.handquickevaluation import HandQuickEvaluation
from hand_evaluation.hand_evaluator import HandEvaluator


class MyTestCase(unittest.TestCase):
    def test_find_pair(self):
        hand_one = [Card(Suit.HEARTS, Rank.TEN), Card(Suit.SPADES, Rank.TEN)]
        self.assertEqual(HandEvaluator.value_hand(hand_one).quick_eval, HandQuickEvaluation.ONE_PAIR)

    def test_pair_is_equal(self):
        hand_one = [Card(Suit.HEARTS, Rank.TEN), Card(Suit.SPADES, Rank.TEN)]
        hand_two = [Card(Suit.CLUBS, Rank.TEN), Card(Suit.DIAMONDS, Rank.TEN)]
        self.assertEqual(HandEvaluator.value_hand(hand_one), HandEvaluator.value_hand(hand_two))

    def test_stronger_pair_wins(self):
        hand_one = [Card(Suit.HEARTS, Rank.TEN), Card(Suit.SPADES, Rank.TEN)]
        hand_two = [Card(Suit.CLUBS, Rank.NINE), Card(Suit.DIAMONDS, Rank.NINE)]
        self.assertNotEqual(HandEvaluator.value_hand(hand_one), HandEvaluator.value_hand(hand_two))


if __name__ == '__main__':
    unittest.main()
