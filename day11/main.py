from itertools import combinations
is_part2 = True
expand_amount = 999999 if is_part2 else 1
grid = [s.strip() for s in open("input.txt").readlines()]
x_shift, y_shift = [], []
shifts = 0
for y, row in enumerate(grid):
    if not '#' in row:
        shifts += expand_amount
    y_shift.append(shifts)

shifts = 0
for x in range(len(grid[0])):
    if not '#' in [row[x] for row in grid]:
        shifts += expand_amount
    x_shift.append(shifts)

galaxies = []

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == '#':
            pos = (x+x_shift[x], y+y_shift[y])
            galaxies.append(pos)

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 

print(sum(dist(a, b) for a, b in combinations(galaxies, 2)))
