grid = [line.strip() for line in open("input.txt")]
curr_dir = (0, 1)
pos = (0, 0)
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
print(len(counter))
