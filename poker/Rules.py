from Card import Rank


def royal_flush(hand):
    if hand.one_suit() and hand.is_consecutive() and hand.max_rank() == Rank.ACE:
        # TB: None
        return []
    else:
        return False


def straight_flush(hand):
    if hand.one_suit() and hand.is_consecutive():
        # TB: rank of the highest card
        return [hand.max_rank()]
    else:
        return False


def four_of_a_kind(hand):
    freq_to_rank = hand.frequency_to_rank()

    if 4 in freq_to_rank and 1 in freq_to_rank:
        # TB: rank of the four cards, rank of the kicker
        return [freq_to_rank[4][0], freq_to_rank[1][0]]

    return False


def full_house(hand):
    freq_to_rank = hand.frequency_to_rank()

    if 3 in freq_to_rank and 2 in freq_to_rank:
        # TB: rank of the three cards, rank of the pair
        return [freq_to_rank[3][0], freq_to_rank[2][0]]

    return False


def flush(hand):
    if not hand.one_suit():
        return False
    else:
        # TB: potentially every card is a tiebreaker; return ranks sorted descending
        return hand.sorted_int_ranks_desc()


def straight(hand):
    if hand.is_consecutive():
        # TB: highest rank in the straight
        return [hand.max_rank()]

    return False


def three_of_a_kind(hand):
    freq_to_rank = hand.frequency_to_rank()

    if 3 in freq_to_rank:
        # TB: rank of the three cards, ranks of remaining two cards
        # Implicit: downstream of full house; assume cards outside triple have freq. 1
        return [freq_to_rank[3][0]] + sorted(freq_to_rank[1], reverse=True)

    return False


def two_pair(hand):
    freq_to_rank = hand.frequency_to_rank()

    if 2 in freq_to_rank:
        if len(freq_to_rank[2]) == 2:
            # TB: rank of highest pair, rank of second highest pair, rank of fifth card
            return [max(freq_to_rank[2]), min(freq_to_rank[2]), freq_to_rank[1][0]]

    return False


def one_pair(hand):
    freq_to_rank = hand.frequency_to_rank()

    if 2 in freq_to_rank:
        # TB: rank of the pair, ranks of the remaining 3 cards descending
        # Implicit: downstream of two_pair; therefore, assume cards outside pair have freq. 1
        return [freq_to_rank[2][0]] + sorted(freq_to_rank[1], reverse=True)

    return False


# This function is trivial; all it does is generate tiebreak info
def high_card(hand):
    # TB: sorted ranks of all cards
    return hand.sorted_int_ranks_desc()
