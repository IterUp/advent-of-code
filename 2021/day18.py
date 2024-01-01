from itertools import permutations
from copy import deepcopy

is_test = False


def add(numbers):
    number = numbers[0]
    for right in numbers[1:]:
        number = [number, right]
    return number


def score(number):
    return (
        number
        if isinstance(number, int)
        else 3 * score(number[0]) + 2 * score(number[1])
    )


class ExplodeDetails:
    def __init__(self):
        self.left = None
        self.right = None
        self.has_exploded = False


def explode(number):
    details = ExplodeDetails()
    inner_explode(number, 0, details)
    return details.has_exploded


def inner_explode(number, depth, details):
    if details is None:
        details = Details()

    if (details.right is not None) and isinstance(number[0], int):
        number[0] += details.right
        details.has_exploded = True
        return number

    if depth == 4:
        assert all(isinstance(v, int) for v in number)

        if (
            (details.left is not None)
            and (details.right is None)
            and not details.has_exploded
        ):
            if isinstance(details.left[1], int):
                details.left[1] += number[0]
            else:
                details.left[0] += number[0]
        details.right = number[1]
        return 0

    if not isinstance(number[0], int):
        assert not details.has_exploded
        number[0] = inner_explode(number[0], depth + 1, details)
        if details.has_exploded:
            return number
        if isinstance(number[1], int) and (details.right is not None):
            number[1] += details.right
            details.has_exploded = True
    else:
        details.left = number

    if not details.has_exploded:
        if not isinstance(number[1], int):
            number[1] = inner_explode(number[1], depth + 1, details)
        else:
            details.left = number

    return number


class SplitDetails:
    def __init__(self):
        self.has_split = False


def split(number):
    details = SplitDetails()
    inner_split(number, details)
    return details.has_split


def inner_split(number, details):
    if isinstance(number, int):
        if number > 9:
            details.has_split = True
            return [number // 2, (number + 1) // 2]
        else:
            return number

    number[0] = inner_split(number[0], details)
    if not details.has_split:
        number[1] = inner_split(number[1], details)

    return number


def reduce(number):
    while explode(number) or split(number):
        pass


def part1(numbers):
    numbers = deepcopy(numbers)
    number = numbers.pop(0)
    i = 0
    while numbers:
        i += 1
        number = [number, numbers.pop(0)]
        reduce(number)
    return score(number)


def part2(numbers):
    numbers = deepcopy(numbers)
    result = 0
    for left, right in permutations(numbers, 2):
        number = [deepcopy(left), deepcopy(right)]
        reduce(number)
        result = max(result, score(number))

    return result


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    return [eval(line) for line in open(filename).readlines()]


main(read_input("test_input/day18.txt" if is_test else "input/day18.txt"))
