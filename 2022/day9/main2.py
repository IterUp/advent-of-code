def move(h, t):
    if max(abs(x - y) for x, y in zip(h, t)) == 2:
        t[0] += t[0] < h[0]
        t[1] += t[1] < h[1]
        t[0] -= t[0] > h[0]
        t[1] -= t[1] > h[1]


directions = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, -1),
    "D": (0, 1),
}

rope = [[0, 0] for i in range(10)]
visited = set()
visited.add(tuple(rope[-1]))
for line in open("input.txt"):
    direction, steps = line.split()
    steps = int(steps)
    for _ in range(steps):
        rope[0][0] += directions[direction][0]
        rope[0][1] += directions[direction][1]
        for i in range(len(rope) - 1):
            move(rope[i], rope[i + 1])
        visited.add(tuple(rope[-1]))

print(len(visited))
