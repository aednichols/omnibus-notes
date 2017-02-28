import Rules
from Hand import Hand
import collections, itertools


# Given a list of card codes ('10H', 'JD', etc.) return the best possible Hand
def best_hand_from_cards(cards):
    assert(len(cards) >= 5)

    # Create a hand for every possible combination of cards
    hands = [Hand(card_list) for card_list in itertools.combinations(cards, 5)]

    return best_hand(hands)


def best_hand(hands):
    # Prime the loop
    best_seen_hand = hands[0]
    best_score = score_hand(hands[0])  # score_hand returns a tuple of

    for candidate_hand in hands[1:]:  # Skip the first hand
        new_score = score_hand(candidate_hand)
        if new_score['score'] < best_score['score']:  # Scoring - lower is better
            best_seen_hand = candidate_hand
            best_score = new_score
        elif new_score['score'] == best_score['score']:
            if break_tie(new_score['tiebreak'], best_score['tiebreak']) > 0:
                best_seen_hand = candidate_hand
                best_score = new_score

    return best_seen_hand


def score_hand(hand):

    '''
    Business rules are evaluated in order of descending priority.
    Many lower-ranked rules are subsets of higher-ranked ones, so
    it is important that the order is correct.

    For example, every four-of-a-kind would trivially match three-
    of-a-kind as well.
    '''

    score_functions = collections.OrderedDict()

    score_functions[Rules.royal_flush] = 1
    score_functions[Rules.straight_flush] = 2
    score_functions[Rules.four_of_a_kind] = 3
    score_functions[Rules.full_house] = 4
    score_functions[Rules.flush] = 5
    score_functions[Rules.straight] = 6
    score_functions[Rules.three_of_a_kind] = 7
    score_functions[Rules.two_pair] = 8
    score_functions[Rules.one_pair] = 9
    score_functions[Rules.high_card] = 10

    for score_function in score_functions:
        tiebreak_or_false = score_function(hand)

        if tiebreak_or_false != False:
            tiebreak = tiebreak_or_false

            # Return score, tiebreak list
            return {'score': score_functions[score_function], 'tiebreak': tiebreak}


# Tiebreak information is always in the form of an integer list descending by priority.
# The first unequal element between the lists determines the result
def break_tie(tiebreak1, tiebreak2):
    assert(len(tiebreak1) == len(tiebreak2))  # Within a category, structure of TB list should be identical

    for value1, value2 in zip(tiebreak1, tiebreak2):  # Parallel iteration
        if value1 > value2:
            return 1
        elif value1 < value2:
            return -1

    return 0