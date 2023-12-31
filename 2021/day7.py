is_test = False


def part1(positions):
    positions = sorted(positions)
    mid = positions[len(positions) // 2]
    return sum(abs(p - mid) for p in positions)


def cost(v):
    return (v + 1) * v // 2


def part2(positions):
    start, end = min(positions), max(positions)
    return min(
        sum(cost(abs(p - mid)) for p in positions) for mid in range(start, end + 1)
    )


def main(filename):
    positions = [int(v) for v in open(filename).readline().split(",")]
    print("Part 1:", part1(positions))
    print("Part 2:", part2(positions))


main("test_input/day7.txt" if is_test else "input/day7.txt")
