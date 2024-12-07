import math


def check(line, num_ops=2):
    total, values = line.split(":")
    total = int(total)
    values = [int(v) for v in values.split()]

    for i in range(num_ops ** (len(values) - 1)):
        x = values[0]
        for v in values[1:]:
            op = i % num_ops
            if op == 0:
                x += v
            elif op == 1:
                x *= v
            else:
                x = x * (10 ** math.ceil(math.log10(v + 1))) + v
            i //= num_ops
        if x == total:
            return total

    return 0


def part1(lines):
    return sum(check(line) for line in lines)


def part2(lines):
    return sum(check(line, 3) for line in lines)


f = open("input.txt")
lines = f.readlines()

print("Part 1 =", part1(lines))
print("Part 2 =", part2(lines))
