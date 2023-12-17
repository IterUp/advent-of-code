grid = [line.strip() for line in open("input.txt")]


def count(grid, start_dir, start_pos):
    curr_dir = start_dir
    pos = start_pos
    stack = [(curr_dir, pos)]

    visited = set()

    def push(curr_dir, pos):
        new = (curr_dir, pos)
        if new not in visited:
            if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
                stack.append(new)
                visited.add(new)

    while stack:
        curr_dir, pos = stack.pop()
        push(curr_dir, pos)
        mirror = grid[pos[0]][pos[1]]
        if curr_dir[0] == 0:
            if mirror == "/":
                curr_dir = (-1, 0) if curr_dir[1] == 1 else (1, 0)
            elif mirror == "\\":
                curr_dir = (-1, 0) if curr_dir[1] == -1 else (1, 0)
            elif mirror == "|":
                curr_dir = (-1, 0)
                push(curr_dir, (pos[0] + curr_dir[0], pos[1] + curr_dir[1]))
                curr_dir = (1, 0)
            else:
                assert mirror in (".", "-")

            push(curr_dir, (pos[0] + curr_dir[0], pos[1] + curr_dir[1]))
        else:
            assert curr_dir[1] == 0
            if mirror == "/":
                curr_dir = (0, -1) if curr_dir[0] == 1 else (0, 1)
            elif mirror == "\\":
                curr_dir = (0, -1) if curr_dir[0] == -1 else (0, 1)
            elif mirror == "-":
                curr_dir = (0, -1)
                push(curr_dir, (pos[0] + curr_dir[0], pos[1] + curr_dir[1]))
                curr_dir = (0, 1)
            else:
                assert mirror in (".", "|")

            push(curr_dir, (pos[0] + curr_dir[0], pos[1] + curr_dir[1]))

    counter = set(pos for curr_dir, pos in visited)
    return len(counter)


max1 = max(count(grid, (0, 1), (i, 0)) for i in range(len(grid)))
max2 = max(count(grid, (0, -1), (i, len(grid) - 1)) for i in range(len(grid)))
max3 = max(count(grid, (1, 0), (0, i)) for i in range(len(grid[0])))
max4 = max(count(grid, (-1, 0), (len(grid[0]) - 1, i)) for i in range(len(grid[0])))
print(max(max1, max2, max3, max4))
