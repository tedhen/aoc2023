from typing import List, Tuple, Dict

def transpose(matrix: List[List[str]])->List[List[str]]:
    matrix_t = [list(x) for x in zip(*matrix)]
    return matrix_t

def extend_universe(universe: List[List[str]], rate: int) -> Dict[int, int]:
    inserted_rows = {}
    for i, x in enumerate(universe):
        if all([v == '.' for v in x]):
            inserted_rows[i] = rate
    return inserted_rows

def find_galaxies(universe: List[List[str]])-> List[Tuple[int,int]]:
    galaxies = []
    for y, row in enumerate(universe):
        for x, value in enumerate(row):
            if value not in '.':
                galaxies.append((y,x))
    return galaxies

def gen_galaxies_pairs(galaxies: List[Tuple[int,int]]) -> List[List[Tuple[int, int]]]:
    pairs = []
    for i, x in enumerate(galaxies):
        if i+1 < len(galaxies):
            for y in galaxies[i+1:]:
                pairs.append([x,y])
    return pairs

def find_shortest_path(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def expand_galaxies(galaxies: List[Tuple[int,int]], row_exp:Dict[int,int], col_exp: Dict[int,int]) -> List[Tuple[int,int]]:
    exp_galaxies = []
    for (y,x) in galaxies:
        y_exp = sum([v for k, v in row_exp.items() if k < y])
        x_exp = sum([v for k, v in col_exp.items() if k < x])
        exp_galaxies.append((y+y_exp, x+x_exp))
    return exp_galaxies

def main():
    with open('day11/input.txt', encoding='utf8') as f:
        puzzle_input = [list(l.strip()) for l in f]
    
    galaxies        = find_galaxies(puzzle_input)

    # Extend the universe in both rows and columns
    row_expansion = extend_universe(puzzle_input, 1)
    col_expansion = extend_universe(transpose(puzzle_input), 1)
    exp_galaxies    = expand_galaxies(galaxies, row_expansion, col_expansion)
    galaxies_pairs  = gen_galaxies_pairs(exp_galaxies)
    part1 = sum([find_shortest_path(x, y) for x, y in galaxies_pairs])
    print(f"Part 1: {part1}")

    row_large_expansion = extend_universe(puzzle_input, 999999)
    col_large_expansion = extend_universe(transpose(puzzle_input), 999999)
    exp_galaxies    = expand_galaxies(galaxies, row_large_expansion, col_large_expansion)
    galaxies_pairs  = gen_galaxies_pairs(exp_galaxies)
    part2 = sum([find_shortest_path(x, y) for x, y in galaxies_pairs])
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()