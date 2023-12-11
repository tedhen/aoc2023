from typing import Dict, List
from math import lcm

def validate_puzzle_path(graph: Dict[str,List[str]], start: str, end: str, p_path: List[str])->int:
    travel_length = -1
    current_node = start
    while True: 
        travel_length += 1
        if current_node == end:
            break
        path_selection = travel_length % len(p_path)
        current_node = graph[current_node][p_path[path_selection]]
    return travel_length

def find_ghost_path(graph: Dict[str,List[str]], start: str, p_path: List[str])->int:
    travel_length = -1
    current_node = start
    while True: 
        travel_length += 1
        if current_node.endswith('Z'):
            break
        path_selection = travel_length % len(p_path)
        current_node = graph[current_node][p_path[path_selection]]
    return travel_length

def main():
    puzzle_path  = ""
    puzzle_graph = {}
    with open('day8/input.txt', encoding='utf8') as f:
        puzzle_path =  [1 if x == 'R' else 0 for x in f.readline().strip()]
        _ = f.readline()
        for l in f:
            ext_l = l.strip().translate({ord(c): None for c in '()=,'}).split()
            puzzle_graph[ext_l[0]] = (ext_l[1], ext_l[2])

    print(f"Part 1: {validate_puzzle_path(puzzle_graph, 'AAA', 'ZZZ', puzzle_path)}")

    start_nodes = list(filter(lambda x: x.endswith('A'), puzzle_graph.keys()))

    ghost_lengths = []
    for s in start_nodes:
        ghost_lengths.append(find_ghost_path(puzzle_graph, s, puzzle_path))

    print(f"Part 2: {lcm(*ghost_lengths)}")

if __name__ == '__main__':
    main()