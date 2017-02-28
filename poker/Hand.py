from Card import Card
import operator, collections


class Hand:

    def __init__(self, card_list):
        self.cards = []

        for card_string in card_list:
            self.cards.append(Card(card_string))

    def __str__(self):
        return " ".join([str(card) for card in self.cards])

    def __eq__(self, other):
        # Card is hashable, so we can use Counter
        return collections.Counter(self.cards) == collections.Counter(other.cards)

    def max_rank(self):
        return max(self.cards, key=operator.attrgetter('int_rank')).int_rank

    def sorted_int_ranks_desc(self):
        sorted_cards = self.sort_by_rank_desc()

        return sorted([card.int_rank for card in sorted_cards], reverse=True)

    def is_consecutive(self):
        max_rank = self.max_rank()

        rank_to_freq = self.rank_to_frequency()

        for rank in range(max_rank, max_rank - 5, -1):
            if rank not in rank_to_freq or rank_to_freq[rank] != 1:
                return False

        return True

    def sort_by_rank_desc(self):
        return sorted(self.cards, key=operator.attrgetter('int_rank'), reverse=True)

    # Map to look up frequency of each rank
    def rank_to_frequency(self):
        frequency = {}

        for card in self.cards:
            if card.int_rank in frequency:
                frequency[card.int_rank] += 1
            else:
                frequency[card.int_rank] = 1

        return frequency

    # Map to look up ranks occurring at a given frequency
    def frequency_to_rank(self):
        # rank => frequency
        frequency = self.rank_to_frequency()

        # frequency => [int_rank1, int_rank2,...]
        result = {}

        for rank, frequency in frequency.items():
            if frequency in result:
                result[frequency].append(rank)
            else:
                result[frequency] = [rank]

        return result

    # Check that all cards are the same suit
    def one_suit(self):
        first_suit = self.cards[0].suit
        for card in self.cards[1:]:
            if card.suit != first_suit:
                return False

        return True
