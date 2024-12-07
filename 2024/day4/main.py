def words(lines, col, row):
    deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    w = len(lines[0])
    h = len(lines)
    for dc, dr in deltas:
        c_end = col + dc * 3
        r_end = row + dr * 3
        if (0 <= c_end < w) and (0 <= r_end < h):
            yield "".join([lines[row + i * dr][col + i * dc] for i in range(4)])


expected_letters = set(["M", "S"])


def test_x_mas(lines, col, row):
    if lines[row][col] != "A":
        return False

    return (
        set([lines[row - 1][col - 1], lines[row + 1][col + 1]]) == expected_letters
    ) and (set([lines[row + 1][col - 1], lines[row - 1][col + 1]]) == expected_letters)


f = open("input.txt")
lines = [line.strip() for line in f.readlines()]
first = list(words(lines, 0, 0))
print(
    "Part 1 =",
    sum(
        w == "XMAS"
        for c in range(len(lines[0]))
        for r in range(len(lines))
        for w in words(lines, c, r)
    ),
)
print(
    "Part 2 =",
    sum(
        test_x_mas(lines, r, c)
        for c in range(1, len(lines[0]) - 1)
        for r in range(1, len(lines) - 1)
    ),
)
