f = open("input.txt")
lines = [line.strip() for line in f.readlines()]


def convert_line(line, c):
    _, back = line.split(":")
    x, y = back.split(",")
    return int(x.split(c)[-1]), int(y.split(c)[-1])


def convert(line1, line2, line3):
    return convert_line(line1, "+"), convert_line(line2, "+"), convert_line(line3, "=")


games = [convert(*lines[4 * i : 4 * i + 3]) for i in range(len(lines) // 4 + 1)]


def play_game(game, offset):
    r1, r2, t = game
    t = (t[0] + offset, t[1] + offset)
    b = (t[1] * r1[0] - t[0] * r1[1]) / (r2[1] * r1[0] - r2[0] * r1[1])
    a = (t[0] * r2[1] - t[1] * r2[0]) / (r1[0] * r2[1] - r1[1] * r2[0])
    result = (int(a), int(b))
    if a == result[0] and b == result[1]:
        return result
    return None


def solve(games, offset):
    total = 0
    for game in games:
        tokens = play_game(game, offset)
        if tokens:
            total += 3 * tokens[0] + tokens[1]
    return total


def part1(games):
    return solve(games, 0)


def part2(games):
    offset = 10000000000000
    return solve(games, offset)


print("Part 1 =", part1(games))
print("Part 2 =", part2(games))
