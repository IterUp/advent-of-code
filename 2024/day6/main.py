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


def part2():
    return 0


f = open("input.txt")
map = [line.strip() for line in f.readlines()]

print("Part 1 =", part1(map))
print("Part 2 =", part2())
