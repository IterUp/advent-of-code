is_test = False


def part1(positions):
    positions = sorted(positions)
    mid = positions[len(positions) // 2]
    return sum(abs(p - mid) for p in positions)


def part2(positions):
    return 0


def main(filename):
    positions = [int(v) for v in open(filename).readline().split(",")]
    print("Part 1:", part1(positions))
    print("Part 2:", part2(positions))


main("test_input/day7.txt" if is_test else "input/day7.txt")
