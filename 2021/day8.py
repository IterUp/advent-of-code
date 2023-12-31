from itertools import permutations

is_test = False
digits = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]


def part1(inputs):
    return sum(len(s) in (2, 3, 4, 7) for input, output in inputs for s in output)


def convert(value, perm):
    return "".join(sorted(perm[ord(c) - ord("a")] for c in value))


def is_valid(value, perm):
    return convert(value, perm) in digits


def find_perm(values):
    for perm in permutations("abcdefg"):
        if all(is_valid(value, perm) for value in values):
            return perm


def make_number(outputs, perm):
    total = 0
    for value in outputs:
        total = 10 * total + digits.index(convert(value, perm))
    return total


def part2(inputs):
    total = 0
    for input, output in inputs:
        perm = find_perm(input + output)
        total += make_number(output, perm)

    return total


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

"""
 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc

aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""
