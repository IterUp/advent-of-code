f = open("input.txt")

grid = [line.strip() for line in f.readlines()]


def find_pos(grid, to_find):
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == to_find:
                return (x, y)


deltas = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}


def part1(grid):
    pos = find_pos(grid, "S")
    end_pos = find_pos(grid, "E")
    d = 0
    scores = {}
    stack = [(pos, d, False)]
    scores[(pos, d)] = 0
    while stack:
        pos, d, was_turn = stack.pop()
        delta = deltas[d]
        next_pos = (pos[0] + delta[0], pos[1] + delta[1])
        if grid[next_pos[1]][next_pos[0]] != "#":
            new_score = scores[(pos, d)] + 1
            key = (next_pos, d)
            if (key not in scores) or (new_score < scores[key]):
                scores[key] = new_score
                stack.append((next_pos, d, False))
        if not was_turn:
            for turn in (-1, 1):
                new_score = scores[(pos, d)] + 1000
                new_d = (d + turn) % 4
                key = (pos, new_d)
                if (key not in scores) or (new_score < scores[key]):
                    scores[key] = new_score
                    stack.append((pos, new_d, True))

    return min(scores[(end_pos, d)] for d in range(4) if (pos, d) in scores)


def part2(grid):
    return 0


print("Part 1 =", part1(grid))
print("Part 2 =", part2(grid))
