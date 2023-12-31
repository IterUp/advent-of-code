from collections import defaultdict

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


def combine(f1, f2, c):
    f = f1.copy()
    for k in f2:
        f[k] += f2[k]
    f[c] -= 1
    return f


def calc_frequencies(template, rules, steps, cache):
    if len(template) > 2:
        return combine(
            calc_frequencies(template[:2], rules, steps, cache),
            calc_frequencies(template[1:], rules, steps, cache),
            template[1],
        )

    key = (template, steps)
    if key in cache:
        return cache[key]

    if steps == 0:
        d = defaultdict(int)
        for c in template:
            d[c] += 1
        return d

    c = rules[template]

    result = combine(
        calc_frequencies("".join((template[0], c)), rules, steps - 1, cache),
        calc_frequencies("".join((c, template[1])), rules, steps - 1, cache),
        c,
    )
    cache[key] = result
    return result


def part2(input):
    template, rules = input
    cache = {}
    frequencies = calc_frequencies(template, rules, 40, cache)
    # print(cache, frequencies)
    return max(frequencies.values()) - min(frequencies.values())


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    lines = open(filename).read().splitlines()
    template = lines[0]
    rules = dict(line.split(" -> ") for line in lines[2:])

    return template, rules


main(read_input("test_input/day14.txt" if is_test else "input/day14.txt"))
