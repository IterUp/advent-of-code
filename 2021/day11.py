is_test = False


def neighbours(matrix, curr_x, curr_y):
    for offset_x in range(-1, 2):
        for offset_y in range(-1, 2):
            if (offset_x, offset_y) != (0, 0):
                x = curr_x + offset_x
                y = curr_y + offset_y
                if 0 <= x < len(matrix[0]) and 0 <= y < len(matrix):
                    yield x, y


def make_matrix(lines):
    return [[int(v) for v in row] for row in lines]


def flash(matrix, curr_x, curr_y):
    to_flash = []
    for x, y in neighbours(matrix, curr_x, curr_y):
        if matrix[y][x] == 9:
            to_flash.append((x, y))
        matrix[y][x] += 1

    return to_flash


def advance(matrix):
    num_flashed = 0
    to_flash = []
    for y, row in enumerate(matrix):
        for x, v in enumerate(row):
            if matrix[y][x] == 9:
                to_flash.append((x, y))
            matrix[y][x] += 1

    while to_flash:
        num_flashed += 1
        curr_x, curr_y = to_flash.pop()
        to_flash += flash(matrix, curr_x, curr_y)

    for y, row in enumerate(matrix):
        for x, v in enumerate(row):
            if v > 9:
                matrix[y][x] = 0

    return num_flashed


def part1(lines):
    matrix = make_matrix(lines)
    num_flashes = 0

    for step in range(100):
        num_flashes += advance(matrix)
    return num_flashes


def part2(lines):
    matrix = make_matrix(lines)
    return 0


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    return open(filename).read().splitlines()


main(read_input("test_input/day11.txt" if is_test else "input/day11.txt"))
