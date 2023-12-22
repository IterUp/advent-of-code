def get_neighbour_coords(lines, row, col):
    if (row > 0) and (lines[row - 1][col] != "#"):
        yield (row - 1, col)
    if (row + 1 < len(lines)) and (lines[row + 1][col] != "#"):
        yield (row + 1, col)
    if (col > 0) and (lines[row][col - 1] != "#"):
        yield (row, col - 1)
    if (col + 1 < len(lines[0])) and (lines[row][col + 1] != "#"):
        yield (row, col + 1)


def get_cells_for_distance(garden, start_row, start_col):
    visited = set()
    next_cells = [(start_row, start_col)]
    visited.add(next_cells[0])
    cells_for_distance = [0, 0]

    while next_cells:
        cells = next_cells
        cells_for_distance.append(len(next_cells) + cells_for_distance[-2])
        next_cells = []
        for cell in cells:
            for n in get_neighbour_coords(garden, *cell):
                if n not in visited:
                    visited.add(n)
                    next_cells.append(n)

    return cells_for_distance[1:]


def main(f, steps):
    garden = f.read().splitlines()

    height = len(garden)
    width = len(garden[0])

    bottom = height - 1
    right = width - 1

    horizontal = (0, right // 2, right)
    vertical = (0, bottom // 2, bottom)

    # Combine because of symmetry
    assert len(garden) == len(garden[0])
    mid = width // 2
    corner_counts_for_distance = [
        sum(a)
        for a in zip(
            *[
                get_cells_for_distance(garden, row, col)
                for row in (0, bottom)
                for col in (0, right)
            ]
        )
    ]
    small_corner = corner_counts_for_distance[65]
    large_corner = corner_counts_for_distance[65 + 131]
    side_counts_for_distance = [
        sum(a)
        for a in zip(
            *[
                get_cells_for_distance(garden, *pos)
                for pos in ((0, mid), (mid, 0), (bottom, mid), (mid, right))
            ]
        )
    ]

    cells_for_distance = [
        [get_cells_for_distance(garden, v, h) for h in horizontal] for v in vertical
    ]

    centre_distances = get_cells_for_distance(garden, mid, mid)
    if len(centre_distances) % 2 == 0:
        odd, even = centre_distances[-2:]
    else:
        even, odd = centre_distances[-2:]

    n = steps // width
    tip = side_counts_for_distance[131]
    return (
        tip
        + (n - 1) ** 2 * odd
        + n**2 * even
        + n * small_corner
        + (n - 1) * large_corner
    )


print(main(open("input.txt"), 26501365))
