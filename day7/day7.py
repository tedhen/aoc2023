from enum import IntEnum

class Card(IntEnum):
    TWO     = 2
    THREE   = 3
    FOUR    = 4
    FIVE    = 5
    SIX     = 6
    SEVEN   = 7
    EIGHT   = 8
    NINE    = 9
    TEN     = 10
    JACK    = 11
    QUEEN   = 12
    KING    = 13
    ACE     = 14


class HandType(IntEnum):
    HIGH_CARD       = 1
    ONE_PAIR        = 2
    TWO_PAIR        = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE      = 5
    FOUR_OF_A_KIND  = 6
    FIVE_OF_A_KIND  = 7


class Hand:

    translation = {'T': 10, 'J': 11,'Q': 12, 'K': 13, 'A':14}

    def __init__(self, raw_hand, bid) -> None:
        self.bid = int(bid)
        self.hand = []
        for c in raw_hand:
            if c in self.translation:
                c = self.translation[c]
            self.hand.append(Card(int(c)))

        self.__check_type__()

    def __check_type__(self):

        sorted_hand = sorted(self.hand)

        card_count = 1
        types = []
        for i, c in enumerate(sorted_hand):
            try:
                if c == sorted_hand[i+1]:
                    card_count += 1
                    continue
            except IndexError:
                pass
            if card_count == 3:
                card_count += 1
            elif card_count in (4,5):
                card_count += 2
            types.append(HandType(card_count))
            card_count = 1

        if HandType.ONE_PAIR in types:
            if HandType.THREE_OF_A_KIND in types:
                types.append(HandType.FULL_HOUSE)
            if len([x for x in types if x == HandType.ONE_PAIR]) > 1:
                types.append(HandType.TWO_PAIR)

        types.sort()
        self.type = types[-1]

    def __lt__(self, other_hand):
        if self.type == other_hand.type:
            for i, c in enumerate(self.hand):
                if c == other_hand.hand[i]:
                    continue
                return c < other_hand.hand[i]
        return self.type < other_hand.type


def main():
    puzzle_input = []
    with open('day7/input.txt', encoding='utf8') as f:
        for l in f:
            ext_l = l.strip().split()
            puzzle_input.append(Hand(ext_l[0], ext_l[1]))

    puzzle_input.sort()

    part1 = 0
    for i, x in enumerate(puzzle_input):
        part1 += x.bid * (i+1)
    print(f"Part1: {part1}")

if __name__ == '__main__':
    main()
