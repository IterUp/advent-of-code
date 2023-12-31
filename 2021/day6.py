from collections import deque

is_test = False


def part1(fish_counts):
    for day in range(80):
        fish_counts.rotate(-1)
        fish_counts[6] += fish_counts[-1]
    return sum(fish_counts)


def part2(fish):
    return 0


def main(filename):
    fish = [int(v) for v in open(filename).readline().split(",")]
    fish_counts = deque(fish.count(day) for day in range(9))
    print("Part 1:", part1(fish_counts))
    print("Part 2:", part2(fish))


main("test_input/day6.txt" if is_test else "input/day6.txt")
