is_test = False
filename = "test_input/day3.txt" if is_test else "input/day3.txt"
lines = open(filename).read().splitlines()


def most_common(line):
    count0 = line.count("0")
    count1 = line.count("1")
    return "0" if count0 > count1 else "1"


def least_common(line):
    count0 = line.count("0")
    count1 = line.count("1")
    return "0" if count0 < count1 else "1"


def part1(lines):
    gamma = int("".join(most_common(line) for line in zip(*lines)), 2)
    epsilon = int("".join(least_common(line) for line in zip(*lines)), 2)
    return gamma * epsilon


def part2(lines):
    return 0


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
