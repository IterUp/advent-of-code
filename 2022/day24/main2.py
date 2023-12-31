import collections

is_test = False
filename = "test_input.txt" if is_test else "input.txt"
valley = open(filename).read().splitlines()

start_pos = (valley[0].index("."), 0)
end_pos = (valley[-1].index("."), len(valley) - 1)

mod_x = len(valley[0]) - 2
mod_y = len(valley) - 2


def is_free(pos, time):
    if pos[1] < 0:
        return False
    if pos[1] >= len(valley):
        return False
    if valley[pos[1]][pos[0]] == "#":
        return False
    if valley[pos[1]][(pos[0] - 1 + time) % mod_x + 1] == "<":
        return False
    if valley[pos[1]][(pos[0] - 1 - time) % mod_x + 1] == ">":
        return False
    if valley[(pos[1] - 1 + time) % mod_y + 1][pos[0]] == "^":
        return False
    if valley[(pos[1] - 1 - time) % mod_y + 1][pos[0]] == "v":
        return False
    return True


def search(src, dst, start_time):
    queue = collections.deque()
    queue.append((src, start_time))

    visited = set()

    while queue[0][0] != dst:
        pos, time = queue.popleft()
        next_time = time + 1
        for d in ((0, 1), (1, 0), (0, 0), (0, -1), (-1, 0)):
            next_pos = (pos[0] + d[0], pos[1] + d[1])
            if (next_pos, next_time) not in visited:
                visited.add((next_pos, next_time))
                if is_free(next_pos, next_time):
                    queue.append((next_pos, next_time))

    return queue[0][1]


t = search(start_pos, end_pos, 0)
t = search(end_pos, start_pos, t)
t = search(start_pos, end_pos, t)
print(t)
