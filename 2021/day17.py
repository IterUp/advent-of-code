is_test = False


def part1(ranges):
    _, y_range = ranges
    v = abs(min(y_range))
    return v * (v - 1) // 2


def part2(packet):
    return 0


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    line = open(filename).readline().strip()
    x_range = [int(v) for v in line[line.index("=") + 1 : line.index(",")].split("..")]
    y_range = [int(v) for v in line[line.rindex("=") + 1 :].split("..")]

    return x_range, y_range


main(read_input("test_input/day17.txt" if is_test else "input/day17.txt"))
