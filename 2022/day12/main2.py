def find_limits(grid):
    for row, line in enumerate(grid):
        try:
            index = line.index("S")
            start = (row, index)
        except ValueError:
            pass
        try:
            index = line.index("E")
            end = (row, index)
        except ValueError:
            pass
    return start, end

grid = [line.strip() for line in open("input.txt").readlines()]
curr, end = find_limits(grid)
grid = [[ord("z" if c == "E" else "a" if c == "S" else c) for c in line] for line in grid]

def find_dist(grid, curr, end):
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    queue = []

    def neighbours(pos):
        if pos[0] > 0:
            yield (pos[0] - 1, pos[1])
        if pos[0] < len(grid) - 1:
            yield (pos[0] + 1, pos[1])
        if pos[1] > 0:
            yield (pos[0], pos[1] - 1)
        if pos[1] < len(grid[0]) - 1:
            yield (pos[0], pos[1] + 1)

    dist = 0

    def get_height(grid, pos):
        return grid[pos[0]][pos[1]]

    def push(pos, dist, visited):
        if not visited[pos[0]][pos[1]]:
            queue.append((pos, dist))
            visited[pos[0]][pos[1]] = True

    push(curr, 0, visited)

    while curr != end:
        if not queue:
            return 2**20
        curr, dist = queue.pop(0)
        height = get_height(grid, curr)
        for neighbour in neighbours(curr):
            other_height = get_height(grid, neighbour)
            if height + 1 >= get_height(grid, neighbour):
                push(neighbour, dist+1, visited)

    return dist

def find_all_starts(grid):
    for row, line in enumerate(grid):
        for col, height in enumerate(line):
            if height == ord('a'):
                yield (row, col)

print(min(find_dist(grid, pos, end) for pos in find_all_starts(grid)))
