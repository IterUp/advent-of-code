is_test = False


def part1(ranges):
    _, y_range = ranges
    v = abs(min(y_range))
    return v * (v - 1) // 2


def hits(vx, vy, x_range, y_range):
    x, y = 0, 0
    while y >= y_range[0]:
        x += vx
        y += vy

        if (x_range[0] <= x <= x_range[1]) and (y_range[0] <= y <= y_range[1]):
            return True

        vx = max(0, vx - 1)
        vy -= 1

    return False


def part2(ranges):
    x_range, y_range = ranges
    max_steps = 2 * (-y_range[0])

    total = 0

    for x_vel in range(1, x_range[1] + 1):
        for y_vel in range(y_range[0], -y_range[0] + 2):
            total += hits(x_vel, y_vel, x_range, y_range)

    return total


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    line = open(filename).readline().strip()
    x_range = [int(v) for v in line[line.index("=") + 1 : line.index(",")].split("..")]
    y_range = [int(v) for v in line[line.rindex("=") + 1 :].split("..")]

    return x_range, y_range


main(read_input("test_input/day17.txt" if is_test else "input/day17.txt"))
