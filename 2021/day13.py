is_test = False


def fold(positions, instruction):
    direction, v = instruction
    return (
        [(x if x < v else 2 * v - x, y) for x, y in positions]
        if direction == "x"
        else [(x, y if y < v else 2 * v - y) for x, y in positions]
    )


def part1(input):
    positions, instructions = input
    return len(set(fold(positions, instructions[0])))


def part2(input):
    positions, instructions = input
    for instruction in instructions:
        positions = fold(positions, instruction)

    width = max(p[0] for p in positions) + 1
    height = max(p[1] for p in positions) + 1
    return "\n" + "\n".join(
        "".join("#" if (x, y) in positions else " " for x in range(width))
        for y in range(height)
    )


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
