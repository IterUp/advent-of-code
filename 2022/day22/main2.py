is_test = False
should_validate_stitches = False

class Cell:
    def __init__(self, pos, c):
        self.c = c
        self.pos = pos
        self.neighbours = [None] * 4
        self.spin = {}

    def __repr__(self):
        return f"{self.pos} '{self.c}'"

    def is_tile(self):
        return self.c == "."

lines = open("test_input.txt" if is_test else "input.txt").read().splitlines()
if should_validate_stitches:
    lines = [line.replace("#", ".") for line in lines] # TODO: REMOVE
max_line = max(len(line) for line in lines[:-2])
grids_wide = 4 if is_test else 3
assert max_line % grids_wide == 0
grid_size = max_line // grids_wide
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
            new_facing = curr.spin.get(self.facing, self.facing)
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
            self.facing = new_facing
            self.curr = curr

    def result(self):
        return 1000 * (self.curr.pos[1] + 1) + 4 * (self.curr.pos[0] + 1) + self.facing


def validate_graph(grid):
    
    for y2, row in enumerate(grid):
        assert len(row) == len(grid[0])
        for x2, cell in enumerate(row):
            if should_validate_stitches and grid[y2][x2].is_tile():
                if ((x2 % 50) == 3) and ((y2 % 50) == 2):
                    pos = Pos(cell)
                    for i in range(4 * grid_size):
                        pos.advance(200, grid)
                        pos.turn("R")
                        assert pos.curr is cell, f"{cell=} {pos.curr=}"
                assert cell.pos == (x2, y2)

            assert cell.c in (" ", "#", ".")
            assert len(cell.neighbours) == 4
            if cell.c == ".":
                for facing, n in enumerate(cell.neighbours):
                    assert isinstance(n, Cell) or n is None, f"{cell.pos=} {cell.neighbours=}"
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
                        # assert n.neighbours[(facing + 2) % 4] is cell
                        assert n.is_tile()
            else:
                assert all(n is None for n in cell.neighbours), f"{cell=} {cell.neighbours=}"

if is_test:
    stitches = (
        (((2,0),2), ((1,1),3), False), # a
        (((0,1),3), ((2,0),3), True), # b
        (((2,1),0), ((3,2),3), True), # c
        (((2,0),0), ((3,2),0), True), # d
        (((1,1),1), ((2,2),2), False), # e
        (((0,1),1), ((2,2),1), True), # f
        (((0,1),2), ((3,2),1), True), # g
    )
else:
    stitches = (
        (((2,0),1), ((1,1),0), False), # a
        (((2,0),0), ((1,2),0), True), # b
        (((1,2),1), ((0,3),0), False), # c
        (((1,1),2), ((0,2),3), False), # d
        (((1,0),2), ((0,2),2), True), # e
        (((1,0),3), ((0,3),2), False), # f
        (((2,0),3), ((0,3),1), False), # g
    )

def make_graph(input_grid):
    for i, grid in enumerate((input_grid, list(zip(*input_grid)))):
        for row_num, line in enumerate(grid):
            prev = None
            for cell in line:
                if cell.c != " ":
                    if cell.is_tile():
                        if prev and cell.is_tile():
                            prev.neighbours[i] = cell
                            cell.neighbours[2 + i] = prev
                        elif prev is None:
                            cell.neighbours[2 + i] = "X"
                    prev = cell if cell.is_tile() else False
                else:
                    if prev:
                        prev.neighbours[i] = "X"
                    prev = None
            if cell.is_tile():
                cell.neighbours[i] = "X"
    stritch_edges(input_grid)

def stritch_edges(grid):
    for left_edge, right_edge, is_reversed in stitches:
        left_grid, left_dir = left_edge
        left_start = [grid_size * left_grid[0] + (grid_size-1) * (left_dir == 0), grid_size * left_grid[1] + (grid_size-1) * (left_dir == 1)]

        right_grid, right_dir = right_edge
        right_start = [grid_size * right_grid[0] + (grid_size-1) * (right_dir == 0), grid_size * right_grid[1] + (grid_size-1) * (right_dir == 1)]
        for i in range(grid_size):
            if left_dir in (0, 2):
                left_pos = (left_start[0], left_start[1] + i)
            else:
                left_pos = (left_start[0] + i, left_start[1])

            j = (grid_size-1) - i if is_reversed else i
            if right_dir in (0, 2):
                right_pos = (right_start[0], right_start[1] + j)
            else:
                right_pos = (right_start[0] + j, right_start[1])

            left = grid[left_pos[1]][left_pos[0]]
            right = grid[right_pos[1]][right_pos[0]]

            if left.is_tile() and right.is_tile():
                assert left.neighbours[left_dir] == "X", f"{left_dir=} {left.neighbours[left_dir]=}"
                left.neighbours[left_dir] = right
                left.spin[left_dir] = (right_dir+2)%4

                assert right.neighbours[right_dir] == "X"
                right.neighbours[right_dir] = left
                right.spin[right_dir] = (left_dir+2)%4
            elif left.is_tile():
                assert left.neighbours[left_dir] == "X", f"{left_dir=} {left.neighbours[left_dir]=}"
                left.neighbours[left_dir] = None
            elif right.is_tile():
                assert right.neighbours[right_dir] == "X"
                right.neighbours[right_dir] = None


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
