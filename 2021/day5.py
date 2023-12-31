is_test = False
filename = "test_input/day5.txt" if is_test else "input/day5.txt"


def part1(segments):
    segments = [s for s in segments if any(x == y for x, y in zip(*s))]

    s1 = set()
    s2 = set()

    for s in segments:
        if s[0][0] == s[1][0]:
            start = min(s[0][1], s[1][1])
            end = max(s[0][1], s[1][1])
            for i in range(start, end + 1):
                p = (s[0][0], i)
                if p in s1:
                    s2.add(p)
                else:
                    s1.add(p)
        else:
            start = min(s[0][0], s[1][0])
            end = max(s[0][0], s[1][0])
            for i in range(start, end + 1):
                p = (i, s[0][1])
                if p in s1:
                    s2.add(p)
                else:
                    s1.add(p)

    return len(s2)


def part2(segments):
    s1 = set()
    s2 = set()

    for s in segments:
        sizes = [y - x for x, y in zip(*s)]
        size = max(abs(v) for v in sizes)
        steps = [v // abs(v) if v else 0 for v in sizes]
        for i in range(size + 1):
            p = (s[0][0] + i * steps[0], s[0][1] + i * steps[1])
            if p in s1:
                s2.add(p)
            else:
                s1.add(p)

    return len(s2)


def make_segment(line):
    src, dst = line.split(" -> ")
    return [tuple(int(v) for v in pos.split(",")) for pos in line.split(" -> ")]


def read_segments(filename):
    return [make_segment(line) for line in open(filename).read().splitlines()]


def main():
    segments = read_segments(filename)
    print("Part 1:", part1(segments))
    print("Part 2:", part2(segments))


main()
