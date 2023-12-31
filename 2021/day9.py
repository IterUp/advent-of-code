from math import prod

is_test = False


def neighbours(matrix, x, y):
    if x > 0:
        yield x - 1, y
    if x < len(matrix[0]) - 1:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y < len(matrix) - 1:
        yield x, y + 1


def is_low_point(matrix, x, y, v):
    return all(matrix[y][x] <= v for x, y in neighbours(matrix, x, y))


def part1(matrix):
    return sum(
        v + 1
        for y, row in enumerate(matrix)
        for x, v in enumerate(row)
        if is_low_point(matrix, x, y, v)
    )


def flood(start_x, start_y, matrix):
    visited = set()
    start = (start_x, start_y)
    queue = [start]
    visited.add(start)
    while queue:
        curr = queue.pop(0)
        for x, y in neighbours(matrix, curr[0], curr[1]):
            p = (x, y)
            if p not in visited and matrix[y][x] != 9:
                visited.add(p)
                queue.append(p)

    return len(visited)


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


def part2(matrix):
    sizes = sorted(
        flood(x, y, matrix)
        for y, row in enumerate(matrix)
        for x, v in enumerate(row)
        if is_low_point(matrix, x, y, v)
    )

    return prod(sizes[-3:])


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    lines = open(filename).read().splitlines()
    return [[int(c) for c in line] for line in lines]


main(read_input("test_input/day9.txt" if is_test else "input/day9.txt"))
