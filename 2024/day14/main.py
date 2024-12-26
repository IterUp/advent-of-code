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


def calc_new_pos(p, v, t):
    return ((p[0] + t * v[0]) % w, (p[1] + t * v[1]) % h)


def robot_positions(robots, time):
    for p, v in robots:
        yield calc_new_pos(p, v, time)


def part1(robots):
    time = 100
    new_robots = [calc_new_pos(p, v, time) for p, v in robots]
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


def print_tree(robots, t):
    grid = [[0] * w for _ in range(h)]
    for p in robot_positions(robots, t):
        grid[p[1]][p[0]] += 1
    for line in grid:
        print("".join("#" if c > 0 else " " for c in line))


def part2(robots):
    max_x_freq = 0
    max_x_freq_time = 0
    max_y_freq = 0
    max_y_freq_time = 0
    for t in range(max(w, h)):
        x_freq = [0] * w
        y_freq = [0] * h
        for p in robot_positions(robots, t):
            x_freq[p[0]] += 1
            y_freq[p[1]] += 1
        if max(x_freq) > max_x_freq:
            max_x_freq = max(x_freq)
            max_x_freq_time = t
        if max(y_freq) > max_y_freq:
            max_y_freq = max(y_freq)
            max_y_freq_time = t
    for t in range(w * h):
        if ((t % w) == max_x_freq_time) and ((t % h) == max_y_freq_time):
            # print_tree(robots, t)
            # print("Time:", t)
            return t

    return 0


print("Part 1 =", part1(robots))
print("Part 2 =", part2(robots))
