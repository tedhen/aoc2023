def get_numbers(puzzle_input):
    numbers = []
    for x in puzzle_input:
        card = x.split(':')[1].strip().split('|')
        winners = card[0].split()
        your_numbers = card[1].split()
        numbers.append((winners,your_numbers))
    return numbers

def get_winners(cards):
    cards_winners = []
    for w,n in cards:
        winners = [value for value in n if value in w]
        cards_winners.append(winners)
    return cards_winners

def get_score(w):
    s = 0
    if w:
        if len(w) == 1:
            s = 1
        else:
            s = pow(2, len(w)-1)
    return s

def count_cards(cards):
    if cards:
        c = cards.pop(0)
        for i in range(len(c[0])):
            w, count = cards[i]
            cards[i] = (w, count+c[1])
        return c[1] + count_cards(cards)
    return 0

def main():
    puzzle_input = []
    with open('day4/input.txt', encoding='utf8') as f:
        for l in f:
            puzzle_input.append(l)
    cards = get_numbers(puzzle_input)
    winners = get_winners(cards)
    score = map(get_score,winners)
    print(f"Part1: {sum(score)}")
    gen_card_count = [(x,1) for x in winners]
    count = count_cards(gen_card_count)
    print(f"Part2: {count}")

if __name__ == "__main__":
    main()
