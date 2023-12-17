pieces = (
    ("####",),
    (
        ".#.",
        "###",
        ".#.",
    ),
    (
        "###",
        "..#",
        "..#",
    ),
    (
        "#",
        "#",
        "#",
        "#",
    ),
    (
        "##",
        "##",
    ),
)


def get_size(grid):
    return sum(row.count("#") for row in grid)


max_piece_height = max(len(piece) for piece in pieces)
max_piece_width = max(len(piece[0]) for piece in pieces)


class Board:
    drop_height = 3
    width = 7

    def __init__(self, wind_generator):
        self.wind_generator = wind_generator
        floor = ["+"] + ["-"] * self.width + ["+"]
        self.data = [floor]
        self.wall_layer = ["|"] + ["."] * self.width + ["|"]
        self.rock_height = 0
        self.build_walls()

    def build_walls(self):
        top_buffer = self.drop_height + max_piece_height
        floor_depth = 1
        new_height = self.rock_height + top_buffer + floor_depth
        for i in range(new_height - len(self.data)):
            self.data.append(self.wall_layer[:])

    def drop_piece(self, piece):
        pos = (3, self.get_rock_height() + self.drop_height + 1)
        has_landed = False
        while not has_landed:
            wind_dir = self.wind_generator.next()
            wind_pos = (pos[0] + wind_dir, pos[1])
            if not self.hits(wind_pos, piece):
                pos = wind_pos

            fall_pos = (pos[0], pos[1] - 1)
            if self.hits(fall_pos, piece):
                has_landed = True
            else:
                pos = fall_pos
        piece_top = pos[1] + len(piece) - 1
        self.rock_height = max(piece_top, self.rock_height)
        self.build_walls()
        self.write_piece(pos, piece)

    def hits(self, pos, piece):
        for y, row in enumerate(piece):
            for x, piece_c in enumerate(row):
                if piece_c == "#" and self.data[y + pos[1]][x + pos[0]] != ".":
                    return True
        return False

    def write_piece(self, pos, piece):
        for y, row in enumerate(piece):
            for x, piece_c in enumerate(row):
                if piece_c == "#":
                    self.data[y + pos[1]][x + pos[0]] = piece_c

    def get_rock_height(self):
        return self.rock_height

    def dump(self):
        for row in self.data[::-1]:
            print("".join(row))

    def get_size(self):
        return get_size(self.data)


class WindGenerator:
    def __init__(self, line):
        self.line = line.strip()
        self.pos = 0

    def next(self):
        c = self.line[self.pos % len(self.line)]
        self.pos += 1
        assert c in ("<", ">")
        return -1 if c == "<" else 1


wind_generator = WindGenerator(open("input.txt").readline())
board = Board(wind_generator)

for i in range(2022):
    piece = pieces[i % len(pieces)]
    board.drop_piece(piece)

print(board.get_rock_height())
