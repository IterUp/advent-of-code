is_test = False
filename = "test_input/day2.txt" if is_test else "input/day2.txt"


def part1():
    depth = 0
    pos = 0
    for line in open(filename).read().splitlines():
        command, size = line.split()
        size = int(size)
        if command == "forward":
            pos += size
        else:
            depth += size if command == "down" else -size
    return depth * pos


print(part1())
