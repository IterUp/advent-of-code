from collections import defaultdict
import math

f = open("input.txt")
numbers = [int(v) for v in f.readline().split()]


def get_length(v):
    return math.floor(math.log10(v)) + 1


def solve(numbers, num_loops):
    d = defaultdict(lambda: 0)

    for n in numbers:
        d[n] += 1

    for i in range(num_loops):
        new_d = defaultdict(lambda: 0)
        for k in d:
            if k == 0:
                new_d[1] += d[k]
            else:
                length = get_length(k)
                if length % 2 == 0:
                    base = 10 ** (length // 2)
                    new_d[k // base] += d[k]
                    new_d[k % base] += d[k]
                else:
                    new_d[k * 2024] += d[k]
        d = new_d

    return sum(d.values())


def part1(numbers):
    return solve(numbers, 25)


def part2(numbers):
    return solve(numbers, 75)


print("Part 1 =", part1(numbers))
print("Part 2 =", part2(numbers))
