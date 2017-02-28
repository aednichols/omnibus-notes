class Card:
    def __init__(self, card_string):
        self.rank = card_string[0:-1]  # Slice from first to second-to-last, exclusive to accommodate 10
        self.suit = card_string[-1]

    @property
    def int_rank(self):
        map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11}

        if self.rank in map:
            return map[self.rank]
        else:
            return int(self.rank)

    def __str__(self):
        return self.rank + self.suit

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.rank + self.suit)

class Rank:
    ACE = 14 # Per requirements - "Aces are treated as high cards only"
    KING = 13
    QUEEN = 12
    JACK = 11