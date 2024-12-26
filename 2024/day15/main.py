f = open("input.txt")

grid = []
moves = ""
has_grid = False
for line in [x.strip() for x in f.readlines()]:
    if has_grid:
        moves += line.strip()
    elif line:
        grid.append(list(line))
    else:
        has_grid = True


def find_robot(grid):
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "@":
                return (x, y)
    assert False


pos = find_robot(grid)
grid[pos[1]][pos[0]] = "."

deltas = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}


def do_move(grid, delta, start_pos):
    pos = start_pos
    first_box = None
    while True:
        pos = (pos[0] + delta[0], pos[1] + delta[1])
        c = grid[pos[1]][pos[0]]
        if c == "#":
            return start_pos
        elif c == ".":
            if first_box:
                grid[pos[1]][pos[0]] = "O"
                grid[first_box[1]][first_box[0]] = "."
            return (start_pos[0] + delta[0], start_pos[1] + delta[1])
        else:
            assert c == "O"
            if first_box == None:
                first_box = pos


def part1(grid, moves, pos):
    for move in moves:
        delta = deltas[move]
        pos = do_move(grid, delta, pos)

    return sum(
        x + 100 * y
        for y, line in enumerate(grid)
        for x, c in enumerate(line)
        if c == "O"
    )


new_tiles = {"#": "##", "O": "[]", ".": ".."}


def can_move(grid, delta, pos):
    next_pos = (pos[0] + delta[0], pos[1] + delta[1])
    c = grid[next_pos[1]][next_pos[0]]
    if c == "#":
        return False
    if c == ".":
        return True
    if delta[0] == 0:
        assert c in ("[", "]")
        next_pos2 = (next_pos[0] + (1 if c == "[" else -1), next_pos[1])
        return can_move(grid, delta, next_pos) and can_move(grid, delta, next_pos2)
    else:
        return can_move(grid, delta, next_pos)


def do_move2(grid, delta, pos):
    next_pos = (pos[0] + delta[0], pos[1] + delta[1])
    c = grid[next_pos[1]][next_pos[0]]
    assert c != "#"
    if c == ".":
        return next_pos
    if delta[0] == 0:
        next_pos_b = (next_pos[0] + (1 if c == "[" else -1), next_pos[1])
        next_pos2a = do_move2(grid, delta, next_pos)
        next_pos2b = do_move2(grid, delta, next_pos_b)
        grid[next_pos2a[1]][next_pos2a[0]] = grid[next_pos[1]][next_pos[0]]
        grid[next_pos2b[1]][next_pos2b[0]] = grid[next_pos_b[1]][next_pos_b[0]]
        grid[next_pos[1]][next_pos[0]] = "."
        grid[next_pos_b[1]][next_pos_b[0]] = "."
    else:
        next_pos2 = do_move2(grid, delta, next_pos)
        grid[next_pos2[1]][next_pos2[0]] = grid[next_pos[1]][next_pos[0]]
        grid[next_pos[1]][next_pos[0]] = "."

    return next_pos


def part2(grid, moves, pos):
    grid = [list("".join(new_tiles[c] for c in line)) for line in grid]
    pos = (2 * pos[0], pos[1])
    for move in moves:
        delta = deltas[move]
        has_moved = False
        if can_move(grid, delta, pos):
            pos = do_move2(grid, delta, pos)
            has_moved = True

    return sum(
        x + 100 * y
        for y, line in enumerate(grid)
        for x, c in enumerate(line)
        if c == "["
    )


if False:
    print("Part 1 =", part1(grid, moves, pos))
else:
    print("Part 2 =", part2(grid, moves, pos))
