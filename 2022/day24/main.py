import collections

is_test = False
filename = "test_input.txt" if is_test else "input.txt"
valley = open(filename).read().splitlines()

start_pos = (valley[0].index("."), 0)
# valley[0] = valley[0].replace(".", "#")
end_pos = (valley[-1].index("."), len(valley) - 1)

mod_x = len(valley[0]) - 2
mod_y = len(valley) - 2

queue = collections.deque()
queue.append(((start_pos[0], 1), 1))
pos = None

visited = set()


def is_free(pos, time):
    if pos[0] < 0:
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


max_pos = 0

while queue[0][0] != end_pos:
    pos, time = queue.popleft()
    # print(pos, time)
    if pos[0] + pos[1] > max_pos:
        print("New max:", pos, time)
        max_pos = sum(pos)
    next_time = time + 1
    for d in ((0, 1), (1, 0), (0, 0), (0, -1), (-1, 0)):
        next_pos = (pos[0] + d[0], pos[1] + d[1])
        if (next_pos, next_time) not in visited:
            visited.add((next_pos, next_time))
            if is_free(next_pos, next_time):
                queue.append((next_pos, next_time))

print(queue[0][1])
