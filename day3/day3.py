from typing import List

class PartNumber:
    number = 0
    is_valid = False

    def __init__(self, number:int, valid:bool) -> None:
        self.number = number
        self.is_valid = valid

def find_Parts(input: List[str]) -> List[PartNumber]:
    temp_partnumber = ""
    temp_valid = False
    parts = []    
    for y, l in enumerate(input):
        for x, v in enumerate(l):
            if v == '.':
                if temp_partnumber:
                    parts.append(PartNumber(int(temp_partnumber), temp_valid))
                temp_valid = False
                temp_partnumber = ""
            elif v.isnumeric():
                temp_partnumber += v
                if check_for_symbols(input, x, y):
                    temp_valid = True
            
    if temp_partnumber:
        parts.append(PartNumber(int(temp_partnumber), temp_valid))
    return parts


def check_for_symbols(input: List[str], x:int, y:int) -> bool:
    # Generate coordinates
    potential_cords = [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]
    allowed_cords = [(pot_y, pot_x) for pot_y,pot_x in potential_cords if is_valid_cord(pot_x,pot_y, y_size=len(input), x_size=len(input[y]))]
    not_allowed_symbols = ['1','2','3','4','5','6','7','8','9','.']
    next_to_symbol = False
    for c_y, c_x in allowed_cords:
        try:
            cord = input[c_y][c_x]
            if cord not in not_allowed_symbols:
                next_to_symbol = True
        except IndexError:
            continue

    return next_to_symbol


def is_valid_cord(x:int, y:int, x_size:int, y_size:int)->bool:
    if x < 0 or y < 0 or x >= x_size or y >= y_size:
        return False
    return True


def parts_sum(parts: List[PartNumber]) -> int:
    sum = 0
    for part in parts:
        if part.is_valid:
            sum += part.number
    return sum

if __name__ == "__main__":
    input = []
    with open('day3/test_input.txt') as f:
        for l in f:
            input.append(l.rstrip())
    parts = find_Parts(input)
    print(f"Part 1: {parts_sum(parts)}")