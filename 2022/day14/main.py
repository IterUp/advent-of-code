lines = [[[int(x) for x in point.split(',')] for point in line.split(" -> ")] for line in open("input.txt")]

class Grid:
    def __init__(self, min_point, max_point):
        self.grid = [['.'] * (max_point[0] - min_point[0] + 1) for row in range(max_point[1] - min_point[1] + 1)]
        self.min_point = min_point
        self.max_point = max_point
        self.drop_point = (500 - self.min_point[0], 0 - self.min_point[1])
        self.width = max_point[0] - min_point[0]
        self.height = max_point[1] - min_point[1]

    def set(self, point, c):
        self.grid[point[1] - self.min_point[1]][point[0] - self.min_point[0]] = c

    def drop_sand(self):
        pos = self.drop_point
        while True:
            if pos[1] == self.height:
                return False
            new_pos = (pos[0], pos[1]+1)
            if self.grid[pos[1] + 1][pos[0]] == '.':
                pos = new_pos
            elif new_pos[0] == 0:
                return False
            elif self.grid[pos[1] + 1][pos[0] - 1] == '.':
                pos = (pos[0] - 1, pos[1]+1)
            elif new_pos[0] == self.width:
                return False
            elif self.grid[pos[1] + 1][pos[0] + 1] == '.':
                pos = (pos[0] + 1, pos[1]+1)
            else:
                self.grid[pos[1]][pos[0]] = 'o'
                return True

    def fill(self):
        count = 0
        while self.drop_sand():
            count += 1
        return count


    def dump(self):
        for line in self.grid:
            print(''.join(line))

max_point = tuple(max(max(point[i] for point in line) for line in lines) for i in range(2))
min_point = (min(min(point[0] for point in line) for line in lines), 0)
grid = Grid(min_point, max_point)

print(min_point, max_point)
for line in lines:
    for interval in zip(line[:-1], line[1:]):
        fixed_index, moving_index = (0,1) if interval[0][0] == interval[1][0] else (1,0)
        from_index = min(p[moving_index] for p in interval)
        to_index = max(p[moving_index] for p in interval)
        point = [0,0]
        point[fixed_index] = interval[0][fixed_index]
        for i in range(from_index, to_index + 1):
            point[moving_index] = i
            grid.set(point, '#')

print(grid.fill())
grid.dump()
