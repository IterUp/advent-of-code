def f(lines, col, row):
    deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    w = len(lines[0])
    h = len(lines)
    for dc, dr in deltas:
        c_end = col + dc * 3
        r_end = col + dc * 3
        if (0 <= c_end < w) and (0 <= r_end < h):
            yield "".join(lines[row + i * dc][col + i * dr])


f = open("input.txt")
lines = [line.strip() for line in f.readlines()]
print(
    sum(
        w == "XMAS"
        for w in f(lines, c, r)
        for c in range(len(lines[0]))
        for r in range(len(lines))
    )
)
