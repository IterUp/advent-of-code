is_test = False


def part1(p1, p2):
    num_rolls = 0
    p1score, p2score = 0, 0
    while p2score < 1000:
        print(f"{p1=} {p2=} {p1score=} {p2score=} {num_rolls=}")
        for i in range(3):
            p1 += (num_rolls % 100) + 1
            num_rolls += 1
        p1 = ((p1 - 1) % 10) + 1
        p1score += p1
        p1, p2 = p2, p1
        p1score, p2score = p2score, p1score

    print(f"{p1score=} {p2score=}")

    return num_rolls * p1score


def part2(p1, p2):
    return 0


def main(inputs):
    print("Part 1:", part1(*inputs))
    print("Part 2:", part2(*inputs))


def read_input(filename):
    return [int(line.split()[-1]) for line in open(filename).readlines()]


main(read_input("test_input/day21.txt" if is_test else "input/day21.txt"))
