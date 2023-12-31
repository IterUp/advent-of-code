is_test = False


def grow(template, rules):
    result = []
    for i, c in enumerate(template):
        result.append(c)
        result.append(rules.get(template[i : i + 2], ""))

    return "".join(result)


def part1(input):
    template, rules = input
    for i in range(10):
        template = grow(template, rules)

    chars = set(template)
    frequencies = [template.count(c) for c in chars]

    return max(frequencies) - min(frequencies)


def part2(input):
    return 0


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    lines = open(filename).read().splitlines()
    template = lines[0]
    rules = dict(line.split(" -> ") for line in lines[2:])

    return template, rules


main(read_input("test_input/day14.txt" if is_test else "input/day14.txt"))
