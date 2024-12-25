f = open("input.txt")
lines = [[int(c) for c in line.strip()] for line in f.readlines()]


def update_neighbours(lines, reaches, row, col, i):
    result = set()
    w, h = len(lines[0]), len(lines)
    for offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        r, c = row + offset[0], col + offset[1]
        if (0 <= r < h) and (0 <= c < w):
            if lines[r][c] == i + 1:
                result.update(reaches[r][c])
    return result


def part1(lines):
    reaches = [
        [set([(row, col)]) if c == 9 else None for col, c in enumerate(line)]
        for row, line in enumerate(lines)
    ]
    for i in range(8, -1, -1):
        for row, line in enumerate(lines):
            for col, c in enumerate(line):
                if c == i:
                    reaches[row][col] = update_neighbours(lines, reaches, row, col, i)

    return sum(
        len(reaches[row][col])
        for row, line in enumerate(lines)
        for col, c in enumerate(line)
        if c == 0
    )


def sum_neighbours(lines, counts, row, col, i):
    total = 0
    w, h = len(lines[0]), len(lines)
    for offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        r, c = row + offset[0], col + offset[1]
        if (0 <= r < h) and (0 <= c < w):
            if lines[r][c] == i - 1:
                total += counts[r][c]
    return total


def part2(lines):
    counts = [[1 if c == 0 else 0 for c in line] for line in lines]
    for i in range(1, 10):
        for row, line in enumerate(lines):
            for col, c in enumerate(line):
                if c == i:
                    counts[row][col] = sum_neighbours(lines, counts, row, col, i)
    return sum(
        counts[row][col]
        for row, line in enumerate(lines)
        for col, c in enumerate(line)
        if c == 9
    )


print("Part 1 =", part1(lines))
print("Part 2 =", part2(lines))
