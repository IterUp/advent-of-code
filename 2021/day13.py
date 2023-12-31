is_test = False


def part1(input):
    positions, instructions = input
    direction, v = instructions[0]

    if direction == "x":
        return len(set((x if x < v else 2 * v - x, y) for x, y in positions))
    else:
        return len(set((x, y if y < v else 2 * v - y) for x, y in positions))


def part2(input):
    return 0


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    positions = []
    instructions = []

    for line in open(filename).read().splitlines():
        if "," in line:
            positions.append(tuple(int(v) for v in line.split(",")))
        elif "=" in line:
            left, right = line.split("=")
            instructions.append((left[-1], int(right)))

    return positions, instructions


main(read_input("test_input/day13.txt" if is_test else "input/day13.txt"))
