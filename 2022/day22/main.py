class Cell:
    def __init__(self, pos, c):
        self.c = c
        self.pos = pos
        self.neighbours = [None] * 4

    def __repr__(self):
        return f"{self.pos} '{self.c}'"

    def is_tile(self):
        return self.c == "."


lines = open("input.txt").read().splitlines()
max_line = max(len(line) for line in lines[:-2])
grid = [
    [Cell((x, y), c) for x, c in enumerate(line + (" " * (max_line - len(line))))]
    for y, line in enumerate(lines[:-2])
]
path = lines[-1]


class Pos:
    def __init__(self, curr):
        self.curr = curr
        self.facing = 0

    def turn(self, direction):
        assert direction in "LR"
        self.facing = (self.facing + (1 if direction == "R" else 3)) % 4

    def advance(self, distance, grid):
        curr = self.curr
        for _ in range(distance):
            curr = curr.neighbours[self.facing]
            if curr is None:
                x, y = self.curr.pos
                if self.facing == 0:
                    x = (x + 1) % len(grid[0])
                elif self.facing == 2:
                    x = (x - 1) % len(grid[0])
                elif self.facing == 1:
                    y = (y + 1) % len(grid)
                elif self.facing == 3:
                    y = (y - 1) % len(grid)
                assert not grid[y][
                    x
                ].is_tile(), f"Should not be tile {x} {y} {self.facing=}"
                return
            assert curr.is_tile()
            self.curr = curr

    def result(self):
        return 1000 * (self.curr.pos[1] + 1) + 4 * (self.curr.pos[0] + 1) + self.facing


def validate_graph(grid):
    for y2, row in enumerate(grid):
        assert len(row) == len(grid[0])
        for x2, cell in enumerate(row):
            assert cell.pos == (x2, y2)
            assert cell.c in (" ", "#", ".")
            assert len(cell.neighbours) == 4
            if cell.c == ".":
                for facing, n in enumerate(cell.neighbours):
                    x, y = cell.pos
                    if facing == 0:
                        x = (x + 1) % len(grid[0])
                    elif facing == 2:
                        x = (x - 1) % len(grid[0])
                    elif facing == 1:
                        y = (y + 1) % len(grid)
                    elif facing == 3:
                        y = (y - 1) % len(grid)
                    if n is None:
                        assert not grid[y][x].is_tile()
                    else:
                        assert n.neighbours[(facing + 2) % 4] is cell
                        assert n.is_tile()
            else:
                assert all(n is None for n in cell.neighbours)


def make_graph(input_grid):
    for i, grid in enumerate((input_grid, zip(*input_grid))):
        for row_num, line in enumerate(grid):
            first = None
            prev = None
            last = None
            for cell in line:
                if cell.c != " ":
                    first = first or cell
                    last = cell
                    if prev and cell.is_tile():
                        prev.neighbours[i] = cell
                        cell.neighbours[2 + i] = prev
                    prev = cell if cell.is_tile() else None
                else:
                    prev = None

            if first.is_tile() and last.is_tile():
                last.neighbours[i] = first
                first.neighbours[i + 2] = last


def first_tile(grid):
    for row in grid:
        for cell in row:
            if cell.is_tile():
                return cell


make_graph(grid)
validate_graph(grid)
pos = Pos(first_tile(grid))


def process_path(path, pos):
    distance = 0
    for c in path:
        if c in "LR":
            yield distance
            distance = 0
            pos.turn(c)
        else:
            distance = 10 * distance + ord(c) - ord("0")
    yield distance


for distance in process_path(path, pos):
    pos.advance(distance, grid)

print(pos.result())
