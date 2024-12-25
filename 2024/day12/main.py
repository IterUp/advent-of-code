f = open("input.txt")
grid = [line.strip() for line in f.readlines()]
offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
offsets2 = [
    ((0, -1), (-1, 0), (-1, -1)),
    ((0, 1), (-1, 0), (-1, 1)),
    ((-1, 0), (0, -1), (-1, -1)),
    ((1, 0), (0, -1), (1, -1)),
]


def neighbours_of(pos):
    for offset in offsets:
        yield (pos[0] + offset[0], pos[1] + offset[1])


def neighbours2_of(pos):
    for o1, o2, o3 in offsets2:
        offsets = (
            (pos[0] + o1[0], pos[1] + o1[1]),
            (pos[0] + o2[0], pos[1] + o2[1]),
            (pos[0] + o3[0], pos[1] + o3[1]),
        )
        yield offsets


def cost1(region):
    area = len(region)
    perimeter = 0
    for pos in region:
        perimeter += sum(n not in region for n in neighbours_of(pos))

    return area * perimeter


def is_first_edge(neighbours, region):
    n1, n2, n3 = neighbours
    r1, r2, r3 = (n1 in region, n2 in region, n3 in region)
    result = not r1 and (not r2 or not (r2 and not r3))
    return result


def cost2(region):
    area = len(region)
    perimeter = 0
    for pos in region:
        new_perimeter = sum(
            is_first_edge(neighbours, region) for neighbours in neighbours2_of(pos)
        )
        perimeter += new_perimeter
        # perimeter += sum(is_first_edge(neighbours, region) for neighbours in neighbours2_of(pos))

    return area * perimeter


def solve(grid, cost):
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


def part1(grid):
    return solve(grid, cost1)


def part2(grid):
    return solve(grid, cost2)


print("Part 1 =", part1(grid))
print("Part 2 =", part2(grid))
