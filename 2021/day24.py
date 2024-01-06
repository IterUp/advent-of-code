is_test = False


def calc(values, calc_pair):
    seq = [None] * 14
    stack = []

    for i, (a, b, c) in enumerate(values):
        if a == 1:
            stack.append((i, c))
        else:
            prev_i, prev_c = stack.pop()
            seq[prev_i], seq[i] = calc_pair(prev_c + b)
    return "".join(str(v) for v in seq)


def part1(values):
    return calc(values, lambda step: (9 - max(step, 0), 9 + min(step, 0)))


def part2(values):
    return calc(values, lambda step: (1 - min(step, 0), 1 + max(step, 0)))


def main(inputs):
    print("Part 1:", part1(*inputs))
    print("Part 2:", part2(*inputs))


def read_input(filename):
    lines = open(filename).readlines()
    return (
        [
            (
                int(lines[18 * i + 4].split()[-1]),
                int(lines[18 * i + 5].split()[-1]),
                int(lines[18 * i + 15].split()[-1]),
            )
            for i in range(14)
        ],
    )


main(read_input("test_input/day24.txt" if is_test else "input/day24.txt"))
# 93997999296912
