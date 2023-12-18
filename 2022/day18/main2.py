def neighbours(block):
    for sign in (-1, 1):
        for i in range(3):
            yield tuple(b + sign * (j == i) for j, b in enumerate(block))


orig_blocks = set(eval(line) for line in open("input.txt"))

low = tuple(min(coord) for coord in zip(*orig_blocks))
high = tuple(max(coord) for coord in zip(*orig_blocks))

blocks = set(
    tuple(v - lower + 1 for v, lower in zip(block, low)) for block in orig_blocks
)
bounds = tuple(h - l + 1 for l, h in zip(low, high))
outside = [
    [[False for z in range(bounds[2] + 2)] for y in range(bounds[1] + 2)]
    for x in range(bounds[0] + 2)
]

to_visit = [(0, 0, 0)]
while to_visit:
    curr = to_visit.pop()
    for n in neighbours(curr):
        if all(0 <= n[i] < bounds[i] + 2 for i in range(3)):
            if n not in blocks:
                if not outside[n[0]][n[1]][n[2]]:
                    outside[n[0]][n[1]][n[2]] = True
                    to_visit.append(n)

print(
    sum(sum(outside[n[0]][n[1]][n[2]] for n in neighbours(block)) for block in blocks)
)
