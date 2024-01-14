is_test = False


def part1(grid):
    has_finished = False
    num_steps = 0
    while not has_finished:
        num_steps += 1
        has_finished = True

        for y, row in enumerate(grid):
            has_last_move = (row[-1] == ">") and (row[0] == ".")
            was_space = False
            for x, c in enumerate(row[:-1]):
                if not was_space and (c == ">") and (grid[y][x + 1] == "."):
                    has_finished = False
                    was_space = True
                    grid[y][x + 1] = ">"
                    grid[y][x] = "."
                else:
                    was_space = False
            if has_last_move:
                row[-1] = "."
                row[0] = ">"

        for x in range(len(grid[0])):
            has_last_move = (grid[-1][x] == "v") and (grid[0][x] == ".")
            was_space = False
            for y in range(len(grid) - 1):
                c = grid[y][x]
                if not was_space and (c == "v") and (grid[y + 1][x] == "."):
                    has_finished = False
                    was_space = True
                    grid[y + 1][x] = "v"
                    grid[y][x] = "."
                else:
                    was_space = False
            if has_last_move:
                grid[-1][x] = "."
                grid[0][x] = "v"

    return num_steps


def part2(values):
    return 0


def main(inputs):
    print("Part 1:", part1(*inputs))
    print("Part 2:", part2(*inputs))


def read_input(filename):
    return ([[c for c in line.strip()] for line in open(filename).readlines()],)


main(read_input("test_input/day25.txt" if is_test else "input/day25.txt"))
