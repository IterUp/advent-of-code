is_test = False


def part1(inputs):
    return sum(len(s) in (2, 3, 4, 7) for input, output in inputs for s in output)


def part2(input):
    return 0


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    lines = open(filename).read().splitlines()
    return [
        (inputs.split(), outputs.split())
        for inputs, outputs in [line.split("|") for line in lines]
    ]


main(read_input("test_input/day8.txt" if is_test else "input/day8.txt"))
