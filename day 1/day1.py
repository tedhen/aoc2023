from typing import List

def extract_numbers(l: List[str]) -> List[int]:
    numbers = []
    for x in l:
        num = [y for y in x if y.isnumeric()]
        numbers.append(int(num[0]  + num[-1]))
    return numbers

def extract_digits_and_text(l: List[str]) -> List[int]:
    fixed_list = map(search_text,l)
    return extract_numbers(fixed_list)

def search_text(text: str) -> str:
    numbers = []
    for i, x in enumerate(text):
        if x.isnumeric():
            numbers.append(x)
            continue

        if text[i:i+3] == "one":
            numbers.append('1')
        elif text[i:i+3] == 'two':
            numbers.append('2')
        elif text[i:i+5] == 'three':
            numbers.append('3')
        elif text[i:i+4] == 'four':
            numbers.append('4')
        elif text[i:i+4] == 'five':
            numbers.append('5')
        elif text[i:i+3] == 'six':
            numbers.append('6')
        elif text[i:i+5] == 'seven':
            numbers.append('7')
        elif text[i:i+5] == 'eight':
            numbers.append('8')
        elif text[i:i+4] == 'nine':
            numbers.append('9')

    return numbers
            

if __name__ == '__main__' :
    input = []
    with open('day1/input.txt') as f:
        input = f.readlines()

    numbers = extract_numbers(input)
    sum_numbers = sum(numbers)
    print(f"Part 1: {sum_numbers}")
    fixed_numbers = extract_digits_and_text(input)
    sum_numbers = sum(fixed_numbers)
    print(f"Part 2: {sum_numbers}")