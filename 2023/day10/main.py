def add_pos(pos, offset):
    return (pos[0]+offset[0], pos[1]+offset[1])

directions = ((0,1), (0,-1), (1,0), (-1, 0))

pipes = {
    "|": ((0,1), (0,-1)),
    "-": ((1,0), (-1, 0)),
    "L": ((1,0), (0, -1)),
    "J": ((-1,0), (0, -1)),
    "7": ((-1,0), (0, 1)),
    "F": ((1,0), (0,1)),
    "S": "S",
}

class Maze:
    def __init__(self):
        self.maze = [[pipes.get(c, None) for c in line] for line in open("input.txt").readlines()]

    def get_pipe(self, pos):
        if 0 <= pos[0] < len(self.maze[0]):
            if 0 <= pos[1] < len(self.maze):
                return self.maze[pos[1]][pos[0]]

    def find_start(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == "S":
                    return (x, y)

    def find_first_step(self, pos):
        for next_dir in directions:
            next_pos = add_pos(pos, next_dir)
            cell = self.get_pipe(next_pos)
            if cell and any(add_pos(next_pos, cell_dir) == pos for cell_dir in cell):
                return next_pos

    def find_next(self, pos, last_pos):
        cell = self.get_pipe(pos)
        for next_dir in cell:
            next_pos = add_pos(pos, next_dir)
            if next_pos != last_pos:
                return next_pos
        assert False

    def find_pipe_dir(self):
        for offset in ((0,1), (0,-1), (-1,0), (1,0)):
            cell = self.get(pos)
            if cell:
                assert cell != 'S'

maze = Maze()
pos = maze.find_start()
last_pos = pos
pos = maze.find_first_step(pos)
count = 1
while maze.get_pipe(pos) != 'S':
    last_pos, pos = pos, maze.find_next(pos, last_pos)
    count += 1
print(count, count/2)
