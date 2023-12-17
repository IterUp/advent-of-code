def move(h, t, direction):
    h[0] += direction[0]
    h[1] += direction[1]
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

h = [0, 0]
t = [0, 0]
visited = set()
visited.add(tuple(t))
for line in open("input.txt"):
    direction, steps = line.split()
    steps = int(steps)
    for i in range(steps):
        move(h, t, directions[direction])
        visited.add(tuple(t))

print(len(visited))
