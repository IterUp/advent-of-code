f = open("input.txt")
grid = [line.strip() for line in f.readlines()]
offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def neighbours_of(pos):
    for offset in offsets:
        yield (pos[0] + offset[0], pos[1] + offset[1])


def cost(region):
    area = len(region)
    perimeter = 0
    for pos in region:
        perimeter += sum(n not in region for n in neighbours_of(pos))

    return area * perimeter


def part1(grid):
    visited = [[False] * len(line) for line in grid]
    total = 0
    w, h = len(grid[0]), len(grid)
    for row, line in enumerate(grid):
        for col, value in enumerate(line):
            if not visited[row][col]:
                stack = [(row, col)]
                region = set(stack)
                visited[row][col] = True
                while stack:
                    curr = stack.pop()
                    for pos in neighbours_of(curr):
                        y, x = pos
                        if (
                            (0 <= x < w)
                            and (0 <= y < h)
                            and (grid[y][x] == value)
                            and (not visited[y][x])
                        ):
                            visited[y][x] = True
                            region.add(pos)
                            stack.append(pos)
                total += cost(region)
    return total


def part2(grid):
    return 0


print("Part 1 =", part1(grid))
print("Part 2 =", part2(grid))
