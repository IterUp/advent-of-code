import math

IS_TEST = False
if IS_TEST:
    f = open("test.txt")
    w, h = 11, 7
else:
    f = open("input.txt")
    w, h = 101, 103


def convert(line):
    p, v = line.split()
    _, p = p.split("=")
    p = tuple(int(t) for t in p.split(","))
    _, v = v.split("=")
    v = tuple(int(t) for t in v.split(","))
    return (p, v)


robots = [convert(line.strip()) for line in f.readlines()]


def part1(robots):
    time = 100
    new_robots = [
        ((p[0] + time * v[0]) % w, (p[1] + time * v[1]) % h) for p, v in robots
    ]
    quads = [0, 0, 0, 0]
    for pos in new_robots:
        if pos[0] < w // 2:
            if pos[1] < h // 2:
                quads[0] += 1
            elif pos[1] > h // 2:
                quads[1] += 1
        elif pos[0] > w // 2:
            if pos[1] < h // 2:
                quads[2] += 1
            elif pos[1] > h // 2:
                quads[3] += 1
    return math.prod(quads)


def part2(robots):
    return 0


print("Part 1 =", part1(robots))
print("Part 2 =", part2(robots))
