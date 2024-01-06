is_test = False


def part1(values):
    seq = [None] * 14
    stack = []

    for i, (a, b, c) in enumerate(values):
        if a == 1:
            stack.append((i, c))
        else:
            prev_i, prev_c = stack.pop()
            step = prev_c + b
            seq[prev_i] = 9 - max(step, 0)
            seq[i] = 9 + min(step, 0)
    return "".join(str(v) for v in seq)


def part2(instructions):
    return 0


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
