from typing import List, Tuple

def transpose(matrix: List[str])->List[str]:
    matrix_t = [list(x) for x in zip(*matrix)]
    return matrix_t

def extend_universe(universe: List[str]) -> List[str]:
    new_universe = universe.copy()
    
    inserted_rows = 0
    for i, x in enumerate(universe):
        if all([v == '.' for v in x]):
            new_universe.insert(i+inserted_rows,x.copy())
            inserted_rows += 1
    return new_universe

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

def main():
    with open('day11/test_input.txt', encoding='utf8') as f:
        puzzle_input = [list(l.strip()) for l in f]

    # Extend the universe in both rows and columns
    ex_universe = extend_universe(puzzle_input)
    ex_universe = transpose(ex_universe)
    ex_universe = extend_universe(ex_universe)
    ex_universe = transpose(ex_universe)

    galaxies = find_galaxies(ex_universe)
    galaxies_pairs = gen_galaxies_pairs(galaxies)

    print(sum([find_shortest_path(x, y) for x, y in galaxies_pairs]))

if __name__ == "__main__":
    main()