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

parity_for_cell = {
        ((0,1), (0,-1)): 1,
        ((1,0), (-1, 0)): 0,
        ((1,0), (0, -1)): 1,
        ((-1,0), (0, -1)): 1,
        ((-1,0), (0, 1)): 0,
        ((1,0), (0,1)): 0,
    "S": 0,
}

class Maze:
    def __init__(self):
        self.maze = [[pipes.get(c, None) for c in line.strip()] for line in open("input.txt").readlines()]
        width = len(self.maze[0])
        self.visited = [[False] * width for i in range(len(self.maze))]

    def get_pipe(self, pos):
        if 0 <= pos[0] < len(self.maze[0]):
            if 0 <= pos[1] < len(self.maze):
                return self.maze[pos[1]][pos[0]]

    def set_pipe(self, pos):
        self.visited[pos[1]][pos[0]] = True

    def is_pipe(self, pos):
        return self.visited[pos[1]][pos[0]]

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

    def count_inner(self):
        count = 0
        for y, row in enumerate(self.maze):
            s=""
            parity = 0
            for x, c in enumerate(row):
                if self.is_pipe((x,y)):
                    parity = (parity + parity_for_cell[c])%2
                    s += str(parity)
                elif parity:
                    s += '#'
                    self.visited[y][x] = None
                    count += 1
                else:
                    s += '*'
            print(s)
        return count

maze = Maze()
pos = maze.find_start()
last_pos = pos
pos = maze.find_first_step(pos)
maze.set_pipe(pos)
while maze.get_pipe(pos) != 'S':
    last_pos, pos = pos, maze.find_next(pos, last_pos)
    maze.set_pipe(pos)

print(maze.count_inner())

for row in maze.visited:
    print(''.join('o' if c else '*' if c is None else '.' for c in row))
