import sys
from collections import Counter

card_labels = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
types = ['five_of_a_kind', 'four_of_a_kind', 'full_house', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']


def solve():
    hand_bids = parse_hands(sys.stdin.readlines())
    ranked_hand_bids = list(sorted(hand_bids))
    return sum(i * bid for i, (_, bid) in enumerate(ranked_hand_bids, 1))


def parse_hands(input_lines):
    return [
        (Hand(cards), int(bid))
        for cards, bid
        in (line.split() for line in input_lines)
    ]


class Hand:
    def __init__(self, cards):
        self.cards = list(cards)
        self.type = self._init_type()

    def __lt__(self, other):
        return (
            types.index(self.type) > types.index(other.type)
            or (self.type == other.type and self._cards_less_than(other))
        )

    def __str__(self):
        return ''.join(self.cards)

    def __repr__(self):
        return f"Hand('{self.__str__()}')"

    def _init_type(self):
        counter = Counter(self.cards)
        counts = [count for card, count in counter.most_common() if card != 'J']
        joker_count = counter['J']

        if joker_count == 5 or counts[0] + joker_count == 5:
            return 'five_of_a_kind'

        if counts[0] + joker_count == 4:
            return 'four_of_a_kind'

        if counts[0] + joker_count == 3 and counts[1] == 2:
            return 'full_house'

        if counts[0] + joker_count == 3:
            return 'three_of_a_kind'

        if counts[0] == 2 and counts[1] + joker_count == 2:
            return 'two_pair'

        if counts[0] + joker_count == 2:
            return 'one_pair'

        return 'high_card'

    def _cards_less_than(self, other):
        for i, card in enumerate(self.cards):
            other_card = other.cards[i]

            if card_labels.index(card) < card_labels.index(other_card):
                return False

            if card_labels.index(card) > card_labels.index(other_card):
                return True

        return False


solution = solve()
print(solution)
