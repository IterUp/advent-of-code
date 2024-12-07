def check(line):
    total, values = line.split(":")
    total = int(total)
    values = [int(v) for v in values.split()]

    for i in range(2 ** (len(values) - 1)):
        x = values[0]
        for v in values[1:]:
            if i % 2:
                x += v
            else:
                x *= v
            i //= 2
        if x == total:
            return total

    return 0


def part1(lines):
    return sum(check(line) for line in lines)


def part2(lines):
    return 0


f = open("input.txt")
lines = f.readlines()

print("Part 1 =", part1(lines))
print("Part 2 =", part2(lines))
