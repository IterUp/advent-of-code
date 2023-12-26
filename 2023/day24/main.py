from itertools import combinations


def calc_t1(h1, h2):
    return calc_t2(h2, h1)


def calc_t2(h1, h2):
    p1, v1 = h1
    p2, v2 = h2
    px1, py1, _ = p1
    vx1, vy1, _ = v1
    px2, py2, _ = p2
    vx2, vy2, _ = v2

    numerator = vy1 * (px2 - px1) - vx1 * (py2 - py1)
    demoninator = vx1 * vy2 - vy1 * vx2

    return numerator / demoninator


def is_parallel(h1, h2):
    return h1[1][0] * h2[1][1] == h2[1][0] * h1[1][1]


def calc_pos(h, t):
    p, v = h
    return tuple(pi + t * vi for pi, vi in zip(p, v))


def print_hailstone(h, c):
    print(
        f"Hailstone {c}: {', '.join(str(v) for v in h[0])} @ {', '.join(str(v) for v in h[1])}"
    )


max_diff = (0, 0)


def check(h1, h2, min_val, max_val):
    if is_parallel(h1, h2):
        return False

    t1, t2 = calc_t1(h1, h2), calc_t2(h1, h2)
    if min(t1, t2) < 0:
        return False

    pos1, pos2 = calc_pos(h1, t1), calc_pos(h2, t2)
    return all(min_val <= val <= max_val for val in pos1[:-1])


is_test = False
if is_test:
    filename = "test_input.txt"
    min_val, max_val = 7, 27
else:
    filename = "input.txt"
    min_val, max_val = 200000000000000, 400000000000000


hailstones = [
    [
        tuple(int(v) for v in pos_str.split(", "))
        for pos_str in line.strip().split(" @ ")
    ]
    for line in open(filename).read().splitlines()
]
print(sum(check(h1, h2, min_val, max_val) for h1, h2 in combinations(hailstones, 2)))
