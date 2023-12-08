from collections import Counter
from enum import IntEnum


class CardType(IntEnum):
    JACK    = 1
    TWO     = 2
    THREE   = 3
    FOUR    = 4
    FIVE    = 5
    SIX     = 6
    SEVEN   = 7
    EIGHT   = 8
    NINE    = 9
    TEN     = 10
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

    translation = {'T': 10, 'J': 1,'Q': 12, 'K': 13, 'A':14}

    def __init__(self, raw_hand, bid) -> None:
        self.bid = int(bid)
        self.hand = []
        for c in raw_hand:
            if c in self.translation:
                c = self.translation[c]
            self.hand.append(CardType(int(c)))

        self.__check_type__()

    def __fix_type__(self, i):
        if i == 3:
            return HandType.THREE_OF_A_KIND
        if i in (4,5):
            i += 2
        return HandType(i)

    def __check_type__(self):

        sorted_hand = Counter(self.hand)

        jokers = sorted_hand.pop(CardType.JACK, 0)
        types = []
        for _, i in sorted_hand.most_common():
            types.append(self.__fix_type__(i))

        types.sort()
        if types and jokers:
            if types[-1] == HandType.THREE_OF_A_KIND:
                types[-1] = self.__fix_type__(3 + jokers)
            else:
                types[-1] = self.__fix_type__(types[-1] + jokers)
        elif jokers:
            types.append(self.__fix_type__(jokers))

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

    part2 = 0
    for i, x in enumerate(puzzle_input):
        part2 += x.bid * (i+1)
    print(f"Part2: {part2}")

if __name__ == '__main__':
    main()
