from collections import deque

is_test = False


def make_counts(fish):
    return deque(fish.count(day) for day in range(9))


def count_fish(fish, days):
    fish_counts = make_counts(fish)
    for day in range(days):
        fish_counts.rotate(-1)
        fish_counts[6] += fish_counts[-1]
    return sum(fish_counts)


def part1(fish):
    return count_fish(fish, 80)


def part2(fish):
    return count_fish(fish, 256)


def main(filename):
    fish = [int(v) for v in open(filename).readline().split(",")]
    print("Part 1:", part1(fish))
    print("Part 2:", part2(fish))


main("test_input/day6.txt" if is_test else "input/day6.txt")
