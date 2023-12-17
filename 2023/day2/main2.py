from collections import defaultdict

def is_valid_turn(turn, limits):
    return all(turn[k] <= limits[k] for k in turn)

def is_valid_game(game, limits):
    return all(is_valid_turn(turn, limits) for turn in game)

def convert_turn(turn):
    d = defaultdict(int)
    pairs = turn.split(',')
    for pair in pairs:
        count, name = pair.split()
        d[name] = int(count)
    return d

def convert_game(line):
    game_label, game_line = line.split(':')
    game_id = int(game_label.split()[-1])
    turns = [convert_turn(turn) for turn in game_line.split(';')]
    return [game_id, turns]

def min_of(name, game):
    return max(turn[name] for turn in game)

def power(game):
    return min_of("red", game) * min_of("blue", game) * min_of("green", game)

games = [convert_game(game) for game in open("input.txt").readlines()]
print(sum(power(game) for game_id, game in games))
