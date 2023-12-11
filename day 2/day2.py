from typing import Dict, List,NewType
Game_Data = NewType('Game_Data',Dict[int,Dict[str,int]])


def extract_cubes(input: List[str])-> Game_Data:
    set_data = {}
    clean = input.strip()
    sets = clean.split(';')
    for i, s in enumerate(sets):
        colors = s.split(',')
        color_set = {}
        for c in colors:
            clean = c.strip()
            count, color = clean.split(' ')
            color_set[color] = int(count)
        set_data[i] = color_set
    return set_data


def extract_game_data(inout: List[str])-> Dict[int,Game_Data]:
    game_data = {}
    for line in inout:
        game, data = line.split(':')
        _, game_number = game.split(' ')
        game_data[int(game_number)] = extract_cubes(data)
    return game_data


def find_valid_games(games: Dict[int,Game_Data])->List[int]:
    valid_games = []
    for g, sets in games.items():
        valid = True
        for _, s in sets.items():
            for color, count in s.items():
                if not valid_check(color, count):
                    valid = False
        if valid:
            valid_games.append(g)
    return valid_games
                        

def valid_check(color:str, count:int) -> bool:
    match color:
        case 'red':
            if count > 12:
                return False
        case 'green':
            if count > 13:
                return False
        case 'blue':
            if count > 14:
                return False
        case _:
            raise TypeError('Invalid game data')
    return True


def find_game_power(games: Dict[int, Game_Data])->List[int]:
    total_power = []
    for _, d in games.items():
        current_count = {'red': 1,'blue': 1,'green': 1}
        for _, s in d.items():
            for color, count in s.items():
                if current_count[color] < count:
                    current_count[color] = count
        game_power = 1
        for x in current_count.values():
            game_power = game_power * x
        total_power.append(game_power)
    return total_power


if __name__ == '__main__':
    input = []
    with open('day2/input.txt') as f:
        input = f.readlines()
        games = extract_game_data(input)
        valid_games = find_valid_games(games)
        print(f"Part 1: {sum(valid_games)}")
        power = find_game_power(games)
        print(f"Part 1: {sum(power)}")