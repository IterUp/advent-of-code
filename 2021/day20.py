is_test = False


def print_pixels(pixels):
    x_range, y_range = [
        (min(p[i] for p in pixels), max(p[i] for p in pixels)) for i in range(2)
    ]
    for y in range(y_range[0], y_range[1] + 1):
        print(
            "".join(
                "#" if (x, y) in pixels else "."
                for x in range(x_range[0], x_range[1] + 1)
            )
        )
    print()


def part1(lookup, pixels):
    for i in range(2):
        new_pixels = set()
        x_range, y_range = [
            (min(p[i] for p in pixels), max(p[i] for p in pixels)) for i in range(2)
        ]
        for y in range(y_range[0] - 1, y_range[1] + 2):
            for x in range(x_range[0] - 1, x_range[1] + 2):
                total = 0
                for b in range(-1, 2):
                    for a in range(-1, 2):
                        if (x_range[0] <= x + a <= x_range[1]) and (
                            y_range[0] <= y + b <= y_range[1]
                        ):
                            is_pixel = (x + a, y + b) in pixels
                        else:
                            is_pixel = (i % 2 == 1) and (lookup[0] == "#")
                        total = 2 * total + is_pixel
                if lookup[total] == "#":
                    new_pixels.add((x, y))
        pixels = new_pixels

    return len(pixels)


def part2(lookup, pixels):
    return 0


def main(inputs):
    print("Part 1:", part1(*inputs))
    print("Part 2:", part2(*inputs))


def read_input(filename):
    f = open(filename)
    lookup = f.readline().strip()
    f.readline()
    pixels = set()

    for y, row in enumerate(f.readlines()):
        for x, c in enumerate(row.strip()):
            if c == "#":
                pixels.add((x, y))
    return lookup, pixels


main(read_input("test_input/day20.txt" if is_test else "input/day20.txt"))
