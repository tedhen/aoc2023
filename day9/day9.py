from typing import List

def predict_next_value(seq: List[int]) -> int:
    pairs = list(zip(seq, seq[1:]))
    new_seq = []
    for x, y in pairs:
        new_seq.append(y-x)
    next_value = seq[-1]
    if any(new_seq):
        next_value += predict_next_value(new_seq)

    return next_value

def predict_previous_value(seq: List[int]) -> int:
    pairs = list(zip(seq, seq[1:]))
    new_seq = []
    for x, y in pairs:
        new_seq.append(y-x)
    next_value = seq[0]
    if any(new_seq):
        next_value -= predict_previous_value(new_seq)

    return next_value

def main():
    puzzle_history = []
    with open('day9/input.txt', encoding='utf8') as f:
        temp = [x.strip().split() for x in f]
        puzzle_history = list(map(lambda t: [int(x) for x in t], temp))

    predict_next_values = [predict_next_value(x) for x in puzzle_history]

    print(f"Part 1: {sum(predict_next_values)}")

    predict_previous_values = [predict_previous_value(x) for x in puzzle_history]

    print(f"Part 1: {sum(predict_previous_values)}")

if __name__ == '__main__':
    main()
