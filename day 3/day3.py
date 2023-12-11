from typing import List, Tuple, Dict, Any

class PartNumber:
    number = 0
    is_valid = False

    def __init__(self, number:int, valid:bool) -> None:
        self.number = number
        self.is_valid = valid

def find_Parts(input: List[str]) -> List[PartNumber]:
    temp_partnumber = ""
    temp_valid = False
    temp_loc = None
    
    gears_found = {}
    parts = []    
    for y, l in enumerate(input):
        for x, v in enumerate(l):
            if v.isnumeric():
                temp_partnumber += v
                is_valid, loc = check_for_symbols(input, x, y)
                if is_valid:
                    temp_valid = True
                if loc:
                    temp_loc = loc
            else:
                if temp_partnumber:
                    parts.append(PartNumber(int(temp_partnumber), temp_valid))
                if temp_loc:
                    add_or_append(gears_found, temp_loc, int(temp_partnumber))
                temp_loc = None
                temp_valid = False
                temp_partnumber = ""
        
        if temp_partnumber:
            parts.append(PartNumber(int(temp_partnumber), temp_valid))
        if temp_loc:
            add_or_append(gears_found, temp_loc, int(temp_partnumber))
         
        temp_partnumber = ""
        temp_valid = False
        temp_loc = None
    return (parts, gears_found)

def check_for_symbols(input: List[str], x:int, y:int) -> Tuple[bool,Tuple[int,int]]:
    potential_cords = [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]
    allowed_cords = [
        (pot_y, pot_x)
        for pot_y,pot_x in potential_cords 
        if is_valid_coord(pot_x,pot_y, y_size=len(input), x_size=len(input[y]))
    ]
    not_allowed_symbols = ['0','1','2','3','4','5','6','7','8','9','.']
    next_to_symbol = False
    gear_location = None
    for c_y, c_x in allowed_cords:
        try:
            coord_value = input[c_y][c_x]
            if coord_value not in not_allowed_symbols:
                next_to_symbol = True
                if coord_value == '*':
                    gear_location = (c_y, c_x)
        except IndexError:
            continue

    return (next_to_symbol, gear_location)

def is_valid_coord(x:int, y:int, x_size:int, y_size:int)->bool:
    return not ( x < 0 or y < 0 or x >= x_size or y >= y_size)

def parts_sum(parts: List[PartNumber]) -> int:
    p_sum = 0
    for part in parts:
        if part.is_valid:
            p_sum += part.number
    return p_sum

def add_or_append(d:Dict, key: Any,  value: Any)-> None:
    if key in d.keys():
        d[key].append(value)
    else:
        d[key] = [value]

def calculate_gears(gears: Dict)->int:
    total_ratio = 0
    for x in gears.values():
        if len(x) == 2:
            new_ratio = x[0] * x[1]
            total_ratio += new_ratio
    return total_ratio 
                
if __name__ == "__main__":
    input = []
    with open('day3/input.txt', encoding="utf8") as f:
        for l in f:
            input.append(l.rstrip())
    parts, gears = find_Parts(input)
    print(f"Part 1: {parts_sum(parts)}")
    print(f"Part 2: {calculate_gears(gears)}")
