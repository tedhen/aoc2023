from typing import Tuple, List
from math import ceil
import matplotlib.path as path

def valid_paths(y:int , x:int, maze: List[str]) -> List[Tuple[int,int]]:
    potential_coords = [(y-1,x),(y,x-1),(y,x+1),(y+1,x)]

    if not is_valid_coord(y,x, len(maze), len(maze[y])):
        return []

    match maze[y][x]:
        case '|' :
            paths = [(y-1,x),(y+1,x)]
        case '-':
            paths = [(y,x-1),(y,x+1)]
        case 'L':
            paths = [(y-1,x),(y,x+1)]
        case 'J':
            paths = [(y-1,x),(y,x-1)]
        case '7':
            paths = [(y+1,x),(y,x-1)]
        case 'F':
            paths = [(y+1,x),(y,x+1)]
        case 'S':
            paths = [pos for pos in potential_coords if (y,x) in valid_paths(*pos, maze)]
        case '.':
            paths = []

    return [p for p in paths if is_valid_coord(*p, len(maze), len(maze[y]))]

def is_valid_coord(y:int,x:int, y_size:int, x_size:int)->bool:
    return not ( x < 0 or y < 0 or x >= x_size or y >= y_size)

def find_start(maze: List[str]) -> Tuple[int, int]:
    for y, row in enumerate(maze):
        for x, colum in enumerate(row):
            if colum == 'S':
                return (y,x)

def traverse_path(
        y:int,x:int, visited: List[Tuple[int,int]], maze:List[str]
        )-> List[Tuple[int, int]]:
# This is so ugly, but works
    while True:
        visited.append((y,x))
        potential_new_pos = [p for p in valid_paths(y,x,maze) if p not in visited]
        if potential_new_pos:
            y,x = potential_new_pos[0]
        else:
            return visited

def main():
    with open('day10/input.txt', encoding='utf8') as f:
        puzzle_input = [x.strip() for x in f]

    s_pos = find_start(puzzle_input)
    s_paths = valid_paths(*s_pos, puzzle_input)
    travel_path = traverse_path(*s_paths[0], [s_pos], puzzle_input)

    print(f"Part 1: {ceil(len(travel_path)/2)}")

    # Create a polygon matplotlib, s_pos added on the end to enclose the polygon
    t_polygon = path.Path(travel_path + [s_pos])

    # Walk over all points to see if they are inside or outside the polygon
    inside_count = 0
    for y, row in enumerate(puzzle_input):
        for x, _ in enumerate(row):
            # Dont test the point on the path.
            if (y,x) not in travel_path and t_polygon.contains_point((y,x)) :
                inside_count += 1

    print(f"Part 2: {inside_count}")

if __name__ == '__main__':
    main()
