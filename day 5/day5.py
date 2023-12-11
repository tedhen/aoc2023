from typing import Dict, Any, List, Tuple

def extract_data(puzzle_input):
    data = {}
    seeds = [int(x) for x in puzzle_input.pop(0).split(':')[1].split()]

    key = ""
    for l in puzzle_input:
        if l[0].isalpha():
            key = l.split()[0]
        else:
            l_data = [int(x) for x in l.split()]
            add_or_append(data, key, l_data)

    return (seeds,data)

def source_to_dest_translation(seed, trans_map)-> int:
    translation = seed
    for d,s,r in trans_map:
        if s <= translation <= (s + r):
            translation = d + (seed - s)
            break

    return translation

def add_or_append(d:Dict, key: Any,  value: Any)-> None:
    if key in d.keys():
        d[key].append(value)
    else:
        d[key] = [value]

def seed_to_soil(seed, data):
    dest = seed
    for m in data.values():
        dest = source_to_dest_translation(dest, m)
    return dest

def get_seed_range(seeds):
    if seeds:
        return [(seeds[0], seeds[0] + seeds[1]-1)] + get_seed_range(seeds[2:])
    return []

def seed_pairs_to_soil(seeds, data):
    s_e = get_seed_range(seeds)
    lowest_soil = float('inf')
    for x in s_e:
        mappings = [x]
        for m in data.values():
            new_mapping = []
            for x in mappings:
                new_mapping += range_to_mapping(*x, m)
            mappings = new_mapping
        maybe_low = min(mappings, key=lambda t: t[0])
        if maybe_low[0] < lowest_soil:
            lowest_soil = maybe_low[0]
    return lowest_soil

def range_to_mapping(start: int, end: int, mapping) -> List[Tuple[int, int]]:
    for d, s, r in mapping:
        if s <= start <= (s+r-1):
            t_s = d + (start - s)
            if end <= s+r-1:
                t_e = d + (end - s)
                return [(t_s, t_e)]
            t_e = d + r-1
            rest_s = s+r
            return [(t_s, t_e)] + range_to_mapping(rest_s, end, mapping)
    return [(start, end)]

def main():
    puzzle_input = []
    with open('day5/input.txt', encoding='utf8') as f:
        for l in f:
            fixed_l = l.strip()
            if fixed_l:
                puzzle_input.append(fixed_l)
    seeds,data = extract_data(puzzle_input)
    part1 = min([seed_to_soil(x,data) for x in seeds])
    print(f"Part 1: {part1}")
    part2 = seed_pairs_to_soil(seeds, data)
    print(f"Part 2: {part2}")

if __name__ == '__main__':
    main()
