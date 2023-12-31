from heapq import heappush, heappop

is_test = False


def neighbours(grid, x, y):
    if x > 0:
        yield (x - 1, y)

    if x < len(grid[0]) - 1:
        yield (x + 1, y)

    if y > 0:
        yield (x, y - 1)

    if y < len(grid) - 1:
        yield (x, y + 1)


def part1(grid):
    heap = [(0, (0, 0))]
    end = (len(grid[0]) - 1, len(grid) - 1)
    visited = set()

    while heap:
        cost, pos = heappop(heap)
        if pos == end:
            return cost
        for neighbour in neighbours(grid, pos[0], pos[1]):
            if neighbour not in visited:
                visited.add(neighbour)
                heappush(heap, (cost + grid[neighbour[1]][neighbour[0]], neighbour))
    assert False
    return 0


def part2(grid):
    return 0


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    return [[int(c) for c in row] for row in open(filename).read().splitlines()]


main(read_input("test_input/day15.txt" if is_test else "input/day15.txt"))
