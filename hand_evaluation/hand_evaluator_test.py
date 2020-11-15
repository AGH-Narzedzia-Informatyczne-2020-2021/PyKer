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

    # Straight tests

    def test_find_straight(self):
        self.assertTrue(HandEvaluator.check_for_straight(straight))
        self.assertTrue(HandEvaluator.check_for_straight(straight_flush))

    def test_find_no_straight(self):
        self.assertFalse(HandEvaluator.check_for_straight(flush))

    # Flush tests

    def test_find_flush(self):
        self.assertTrue(HandEvaluator.check_for_flush(flush))
        self.assertTrue(HandEvaluator.check_for_flush(straight_flush))

    def test_check_if_not_flush(self):
        self.assertFalse(HandEvaluator.check_for_flush(straight))

    def test_find_royal_flush(self):
        self.assertTrue(HandEvaluator.check_for_straight_flush(straight_flush))


if __name__ == '__main__':
    unittest.main()

straight_flush = [Card(Suit.SPADES, Rank.TEN), Card(Suit.SPADES, Rank.EIGHT),
                  Card(Suit.SPADES, Rank.NINE),
                  Card(Suit.SPADES, Rank.JACK), Card(Suit.SPADES, Rank.QUEEN)]

flush = [Card(Suit.SPADES, Rank.TEN), Card(Suit.SPADES, Rank.ACE), Card(Suit.SPADES, Rank.KING),
         Card(Suit.SPADES, Rank.TWO), Card(Suit.SPADES, Rank.FIVE), Card(Suit.DIAMONDS, Rank.QUEEN),
         Card(Suit.DIAMONDS, Rank.THREE)]

straight = [Card(Suit.DIAMONDS, Rank.TEN), Card(Suit.HEARTS, Rank.NINE), Card(Suit.CLUBS, Rank.EIGHT),
            Card(Suit.SPADES, Rank.SEVEN), Card(Suit.CLUBS, Rank.SIX), Card(Suit.DIAMONDS, Rank.ACE)]
