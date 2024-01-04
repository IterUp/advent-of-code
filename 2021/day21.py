from collections import defaultdict

is_test = False


def part1(p1, p2):
    num_rolls = 0
    p1score, p2score = 0, 0
    while p2score < 1000:
        for i in range(3):
            p1 += (num_rolls % 100) + 1
            num_rolls += 1
        p1 = ((p1 - 1) % 10) + 1
        p1score += p1
        p1, p2 = p2, p1
        p1score, p2score = p2score, p1score

    return num_rolls * p1score


dice_outcomes = defaultdict(int)
for v in [a + b + c for a in range(1, 4) for b in range(1, 4) for c in range(1, 4)]:
    dice_outcomes[v] += 1


def num_wins(p1, p1score, p2, p2score, cache):
    key = (p1, p1score, p2, p2score)
    if key in cache:
        return cache[key]
    if p2score >= 21:
        return (0, 1)

    results = [
        (
            frequency,
            num_wins(
                p2,
                p2score,
                (p1 + dice_total - 1) % 10 + 1,
                p1score + (p1 + dice_total - 1) % 10 + 1,
                cache,
            ),
        )
        for dice_total, frequency in dice_outcomes.items()
    ]

    result = (
        sum(frequency * result[1] for frequency, result in results),
        sum(frequency * result[0] for frequency, result in results),
    )

    cache[key] = result

    return result


def part2(p1, p2):
    return max(num_wins(p1, 0, p2, 0, {}))


def main(inputs):
    print("Part 1:", part1(*inputs))
    print("Part 2:", part2(*inputs))


def read_input(filename):
    return [int(line.split()[-1]) for line in open(filename).readlines()]


main(read_input("test_input/day21.txt" if is_test else "input/day21.txt"))
