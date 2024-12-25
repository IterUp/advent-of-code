f = open("input.txt")
lines = [line.strip() for line in f.readlines()]


def convert_line(line, c):
    _, back = line.split(":")
    x, y = back.split(",")
    return int(x.split(c)[-1]), int(y.split(c)[-1])


def convert(line1, line2, line3):
    return convert_line(line1, "+"), convert_line(line2, "+"), convert_line(line3, "=")


games = [convert(*lines[4 * i : 4 * i + 3]) for i in range(len(lines) // 4 + 1)]


def play_game(game):
    r1, r2, t = game
    b = (t[1] * r1[0] - t[0] * r1[1]) / (r2[1] * r1[0] - r2[0] * r1[1])
    a = (t[0] * r2[1] - t[1] * r2[0]) / (r1[0] * r2[1] - r1[1] * r2[0])
    result = (int(a), int(b))
    if a == result[0] and b == result[1]:
        return result
    return None


def part1(games):
    total = 0
    wins = 0
    losses = 0
    for game in games:
        tokens = play_game(game)
        if tokens:
            total += 3 * tokens[0] + tokens[1]
            wins += 1
        else:
            losses += 1
    return total


def part2(games):
    return 0


print("Part 1 =", part1(games))
print("Part 2 =", part2(games))
