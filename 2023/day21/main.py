def get_neighbours(lines, row, col):
    if row > 0:
        yield lines[row - 1][col]
    if row < len(lines) - 1:
        yield lines[row + 1][col]
    if col > 0:
        yield lines[row][col - 1]
    if col < len(lines[0]) - 1:
        yield lines[row][col + 1]


def main():
    lines = [list(line) for line in open("input.txt").read().splitlines()]
    new_map = [list(line) for line in lines]
    old_map = [list(line) for line in lines]

    for step in range(64):
        old_map, new_map = new_map, old_map
        for row_index, row in enumerate(old_map):
            for col_index, c in enumerate(row):
                if c != "#":
                    has_neighbour = any(
                        n in ("O", "S")
                        for n in get_neighbours(old_map, row_index, col_index)
                    )
                    new_map[row_index][col_index] = "O" if has_neighbour else "."

    print(sum(c == "O" for row in new_map for c in row))


main()
