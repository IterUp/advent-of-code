def find_start_pos(map):
    for y, line in enumerate(map):
        try:
            return line.index("^"), y
        except ValueError:
            pass


dir_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def part1(map):
    pos = find_start_pos(map)
    dir_index = 0
    visited = set()
    visited.add(pos)
    while True:
        curr_dir = dir_list[dir_index]
        next_pos = (pos[0] + curr_dir[0], pos[1] + curr_dir[1])
        if (0 <= next_pos[0] < len(map[0])) and (0 <= next_pos[1] < len(map)):
            tile = map[next_pos[1]][next_pos[0]]
            if tile == "#":
                dir_index = (dir_index + 1) % len(dir_list)
            else:
                pos = next_pos
                visited.add(pos)
        else:
            return len(visited)


def is_loop(map):
    pos = find_start_pos(map)
    dir_index = 0
    visited = {}
    visited[pos] = set([pos])
    while True:
        curr_dir = dir_list[dir_index]
        next_pos = (pos[0] + curr_dir[0], pos[1] + curr_dir[1])
        if (0 <= next_pos[0] < len(map[0])) and (0 <= next_pos[1] < len(map)):
            tile = map[next_pos[1]][next_pos[0]]
            if tile == "#":
                dir_index = (dir_index + 1) % len(dir_list)
            else:
                pos = next_pos
                if pos not in visited:
                    visited[pos] = set()
                if dir_index in visited[pos]:
                    return True
                visited[pos].add(dir_index)
        else:
            return False


def part2(map):
    map = [list(line) for line in map]
    result = 0
    for y, line in enumerate(map):
        print(f"{y}/{len(map)}: {result}")
        for x, c in enumerate(line):
            if c == ".":
                map[y][x] = "#"
                if is_loop(map):
                    result += 1
                map[y][x] = "."
    return result


f = open("input.txt")
map = [line.strip() for line in f.readlines()]

print("Part 1 =", part1(map))
print("Part 2 =", part2(map))
