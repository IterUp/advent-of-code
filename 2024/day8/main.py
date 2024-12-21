import itertools

f = open("input.txt")
lines = [line.strip() for line in f.readlines()]

sites = {}

h = len(lines)
w = len(lines[0])

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != ".":
            if c not in sites:
                sites[c] = []
            sites[c].append((x, y))


def part1():
    matches = set()

    for c in sites:
        for a, b in itertools.combinations(sites[c], 2):
            diff = (b[0] - a[0], b[1] - a[1])
            p1 = (a[0] - diff[0], a[1] - diff[1])
            p2 = (b[0] + diff[0], b[1] + diff[1])
            for p in (p1, p2):
                if (0 <= p[0] < w) and (0 <= p[1] < h):
                    matches.add(p)
    return len(matches)


def part2():
    matches = set()

    for c in sites:
        for a, b in itertools.combinations(sites[c], 2):
            diff = (b[0] - a[0], b[1] - a[1])
            for direction in (-1, 1):
                is_done = False
                i = 0
                while not is_done:
                    p = (a[0] - direction * i * diff[0], a[1] - direction * i * diff[1])
                    if (0 <= p[0] < w) and (0 <= p[1] < h):
                        matches.add(p)
                        i = i + 1
                    else:
                        is_done = True

    return len(matches)


print("Part 1 =", part1())
print("Part 2 =", part2())
