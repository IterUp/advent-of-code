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

games = [convert_game(game) for game in open("input.txt").readlines()]
limits = dict(red=12, green=13, blue=14)
print(sum(game_id for game_id, game in games if is_valid_game(game, limits)))
