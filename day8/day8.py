from typing import Dict, List

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

def main():
    puzzle_path  = ""
    puzzle_graph = {}
    with open('day8/input.txt', encoding='utf8') as f:
        puzzle_path =  [1 if x == 'R' else 0 for x in f.readline().strip()]
        _ = f.readline()
        for l in f:
            ext_l = l.strip().translate({ord(c): None for c in '()=,'}).split()
            puzzle_graph[ext_l[0]] = (ext_l[1], ext_l[2])

    print(validate_puzzle_path(puzzle_graph, 'AAA', 'ZZZ', puzzle_path))

if __name__ == '__main__':
    main()