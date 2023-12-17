from heapq import heappush, heappop


class Cell:
    def __init__(self, heat):
        self.heat = heat
        self.cost = [None, None]

    def add_cost(self, new_cost, direction):
        if self.cost[direction] is None or new_cost < self.cost[direction]:
            self.cost[direction] = new_cost
            return True

        return False


directions = [((0, 1), (0, -1)), ((1, 0), (-1, 0))]

grid = [[Cell(int(c)) for c in line.strip()] for line in open("input.txt")]
end = (len(grid[0]) - 1, len(grid) - 1)


def find_path(pos):
    heap = []
    heappush(heap, (0, pos, True, ()))
    heappush(heap, (0, pos, False, ()))
    grid[0][0].cost = [0, 0]
    while heap:
        cost, pos, direction, path = heappop(heap)
        path = path + ((pos, cost),)
        direction = not direction
        if pos == end:
            print(path)
            return cost
        for next_dir in directions[direction]:
            curr_cost = cost
            next_pos = pos
            for i in range(10):
                next_pos = (next_pos[0] + next_dir[0], next_pos[1] + next_dir[1])
                if all(0 <= next_pos[i] <= end[i] for i in range(2)):
                    cell = grid[next_pos[1]][next_pos[0]]
                    curr_cost += cell.heat
                    if i >= 3:
                        if cell.add_cost(curr_cost, direction):
                            heappush(heap, (curr_cost, next_pos, direction, path))


print(find_path((0, 0)))
