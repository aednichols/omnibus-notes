import unittest
from Hand import Hand
from Evaluator import score_hand, best_hand, best_hand_from_cards


royal_flush      = Hand(['AH', 'KH', 'QH', 'JH', '10H'])
straight_flush   = Hand(['9C', '8C', '7C', '6C', '5C'])
straight_flush_worse = Hand(['8C', '7C', '6C', '5C', '4C'])
four_of_a_kind   = Hand(['AH', 'AC', 'AS', 'AD', 'KD'])
full_house       = Hand(['AH', 'AC', 'AS', 'KS', 'KD']) # aces full of kings
full_house_worse = Hand(['KH', 'KC', 'KS', 'AS', 'AD']) # kings full of aces
flush            = Hand(['AS', '10S', '7S', '6S', '2S'])
straight         = Hand(['6S', '5D', '4C', '3H', '2S'])
three_of_a_kind  = Hand(['AH', 'AS', 'AD', 'KD', 'QS'])
two_pair         = Hand(['AH', 'AS', 'KC', 'KD', 'QS'])
one_pair         = Hand(['AH', 'AS', 'KH', 'QS', 'JD'])
high_card        = Hand(['AH', 'KS', 'QD', 'JS', '9S'])


class Tests(unittest.TestCase):
    def test_score_hand(self):
        self.assertEqual(score_hand(royal_flush)['score'], 1)
        self.assertEqual(score_hand(royal_flush)['tiebreak'], [])

        self.assertEqual(score_hand(straight_flush)['score'], 2)
        self.assertEqual(score_hand(straight_flush)['tiebreak'], [9])

        self.assertEqual(score_hand(four_of_a_kind)['score'], 3)
        self.assertEqual(score_hand(four_of_a_kind)['tiebreak'], [14, 13])

        self.assertEqual(score_hand(full_house)['score'], 4)
        self.assertEqual(score_hand(full_house)['tiebreak'], [14, 13])

        self.assertEqual(score_hand(flush)['score'], 5)
        self.assertEqual(score_hand(flush)['tiebreak'], [14, 10, 7, 6, 2])

        self.assertEqual(score_hand(straight)['score'], 6)
        self.assertEqual(score_hand(straight)['tiebreak'], [6])

        self.assertEqual(score_hand(three_of_a_kind)['score'], 7)
        self.assertEqual(score_hand(three_of_a_kind)['tiebreak'], [14, 13, 12])

        self.assertEqual(score_hand(two_pair)['score'], 8)
        self.assertEqual(score_hand(two_pair)['tiebreak'], [14, 13, 12])

        self.assertEqual(score_hand(one_pair)['score'], 9)
        self.assertEqual(score_hand(one_pair)['tiebreak'], [14, 13, 12, 11])

        self.assertEqual(score_hand(high_card)['score'], 10)
        self.assertEqual(score_hand(high_card)['tiebreak'], [14, 13, 12, 11, 9])

    def test_best_hand(self):
        self.assertEqual(best_hand([four_of_a_kind, three_of_a_kind]), four_of_a_kind)
        self.assertEqual(best_hand([high_card, one_pair, two_pair]), two_pair)
        self.assertEqual(best_hand([royal_flush, flush]), royal_flush)
        self.assertEqual(best_hand([royal_flush, high_card]), royal_flush)

        # Exercising tiebreaker
        self.assertEqual(best_hand([full_house, full_house_worse]), full_house)
        self.assertEqual(best_hand([straight_flush, straight_flush_worse]), straight_flush)

        # Make sure order doesn't matter
        self.assertEqual(best_hand([full_house_worse, full_house]), full_house)
        self.assertEqual(best_hand([straight_flush_worse, straight_flush]), straight_flush)

    def test_best_hand_from_cars(self):
        cards = ['10H', 'JD', '4H', 'AH', 'KH', 'QH', 'JH', '10S', '7D', '2H', '3S', 'QD']

        self.assertEqual(best_hand_from_cards(cards), Hand(['AH', 'KH', 'QH', 'JH', '10H']))
