from heapq import heappush, heappop


class Cell:
    def __init__(self, heat):
        self.heat = heat
        self.cost = None
        self.second_cost = None
        self.direction = (1, 0)

    def add_cost(self, cost, direction, count):
        new_cost = cost + self.heat
        if self.cost is None:
            self.cost = new_cost
            self.direction = direction
            self.count = count
        elif direction == self.direction:
            if count < self.count:
                self.count = count
            else:
                return None
        elif self.second_cost is None:
            self.second_cost = new_cost
        else:
            return None
        return new_cost

    @property
    def was_visited(self):
        return self.cost is not None

    @property
    def dir_char(self):
        return {(0, 1): "v", (1, 0): ">", (0, -1): "^", (-1, 0): "<"}[self.direction]


directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
last_direction = None
count = 0

grid = [[Cell(int(c)) for c in line.strip()] for line in open("input.txt")]
end = (len(grid[0]) - 1, len(grid) - 1)


def find_path(pos):
    heap = []
    heappush(heap, (0, pos, (0, 1), 0, ()))
    grid[0][0].cost = 0
    while heap:
        cost, pos, direction, count, path = heappop(heap)
        path = path + ((pos, cost),)
        # print("From:", pos, "Cost:", cost, direction, count)
        if pos == end:
            # print("Path:", path)
            return cost
        for next_dir in directions:
            if any(x + y != 0 for x, y in zip(next_dir, direction)):
                next_pos = (pos[0] + next_dir[0], pos[1] + next_dir[1])
                if all(0 <= next_pos[i] <= end[i] for i in range(2)):
                    cell = grid[next_pos[1]][next_pos[0]]
                    if count < 3 or next_dir != direction:
                        new_count = count + 1 if next_dir == direction else 1
                        new_cost = cell.add_cost(cost, next_dir, new_count)
                        if new_cost is not None:
                            # print("To:", next_pos)
                            heappush(
                                heap, (new_cost, next_pos, next_dir, new_count, path)
                            )


print(find_path((0, 0)))
# for line in grid:
#     print([str(cell.cost)+cell.dir_char for cell in line])
