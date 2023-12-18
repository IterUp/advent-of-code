directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

import time

def approach_pos(start, end):
    return tuple(s + (1 if s < e else -1 if s > e else 0) for s, e in zip(start, end))

class DigInstruction:
    def __init__(self, line):
        direction, distance, colour = line.split()
        self.direction = directions[direction]
        self.distance = int(distance)

    def move(self, pos):
        return tuple(p + self.distance*d for p, d in zip(pos, self.direction))

class DigInstructions:
    def __init__(self, f):
        self.instructions = [DigInstruction(line) for line in f]
        self.start_pos, self.grid = self.make_grid()
        self.draw_outline((-self.start_pos[0], -self.start_pos[1]))
        self.fill()
        self.dump()

    def get_verts(self, start_pos = (0, 0)):
        pos = start_pos
        yield pos
        for instruction in self.instructions:
            pos = instruction.move(pos)
            yield pos

    def get_bounds(self, start_pos = (0, 0)):
        return [[f(coords) for coords in zip(*self.get_verts(start_pos))] for f in (min, max)]

    def make_grid(self):
        bounds = self.get_bounds()
        print(bounds, self.get_bounds((-bounds[0][0], -bounds[0][1])))
        sizes = [high - low + 1 for low, high in zip(*bounds)]
        return bounds[0], [["."] * sizes[0] for _ in range(sizes[1])]

    def draw_outline(self, start_pos):
        pos = None
        for next_pos in self.get_verts(start_pos):
            if pos:
                # print(pos, next_pos)
                draw_pos = pos
                while draw_pos != next_pos:
                    self.grid[draw_pos[1]][draw_pos[0]] = '#'
                    draw_pos = approach_pos(draw_pos, next_pos)
                    # self.dump()
                    # print()
                    # time.sleep(0.2)

            pos = next_pos

    def fill(self):
        for row, line in enumerate(self.grid):
            if row != 0:
                is_inside = False
                wall_count = 0
                for col, c in enumerate(line):
                    if c == '#':
                        wall_count += 1
                    else:
                        if wall_count == 1:
                            is_inside = not is_inside
                        elif wall_count > 1:
                            is_inside = self.grid[row - 1][col] != '.'
                        wall_count = 0
                        if is_inside:
                            self.grid[row][col] = "*"

    def dump(self):
        for line in self.grid[:60]:
            print(''.join(line[:100]))

    def count_lava(self):
        return sum(line.count("#") for line in self.grid) + \
            sum(line.count("*") for line in self.grid)

d = DigInstructions(open("input.txt"))
print(d.count_lava())
