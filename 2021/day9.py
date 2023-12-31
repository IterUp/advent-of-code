is_test = False


def is_low_point(matrix, x, y, v):
    if x > 0 and matrix[y][x - 1] <= v:
        return False
    if (x < len(matrix[0]) - 1) and matrix[y][x + 1] <= v:
        return False
    if y > 0 and matrix[y - 1][x] <= v:
        return False
    if (y < len(matrix) - 1) and matrix[y + 1][x] <= v:
        return False
    return True


def part1(matrix):
    return sum(
        v + 1
        for y, row in enumerate(matrix)
        for x, v in enumerate(row)
        if is_low_point(matrix, x, y, v)
    )


def part2(matrix):
    return 0


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    lines = open(filename).read().splitlines()
    return [[int(c) for c in line] for line in lines]


main(read_input("test_input/day9.txt" if is_test else "input/day9.txt"))
