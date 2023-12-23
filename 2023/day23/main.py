moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

directions = {0: "<", 1: "^", 2: ">", 3: "v"}


class Node:
    def __init__(self, pos):
        self.pos = pos
        self.edges = []
        self.is_goal = False

    def add_edge(self, dst, length):
        for i, edge in enumerate(self.edges):
            if edge[0] is dst:
                if edge[1] < length:
                    self.edges[i] = (dst, length)
                return

        assert len(self.edges) < 3
        self.edges.append((dst, length))

    def __repr__(self):
        return f"N({self.pos})"

    def max_distance_to_goal(self, path=()):
        if self.is_goal:
            return 0
        else:
            new_path = path + (self.pos,)
            value = max(
                (
                    edge[0].max_distance_to_goal(new_path) + edge[1]
                    for edge in self.edges
                ),
                default=0,
            )
            return value


def calc_is_forward(to_dir, c):
    if c == ".":
        return None
    return directions[to_dir] != c


def get_neighbours(maze, pos, from_dir):
    for to_dir, move in enumerate(moves):
        if to_dir != from_dir:
            x, y = pos[0] + move[0], pos[1] + move[1]
            assert 0 <= x < len(maze[0]), f"{(x,y)=} {from_dir=} {to_dir=}"
            assert 0 <= y < len(maze), f"{(x,y)=} {from_dir=} {to_dir=}"
            c = maze[y][x]
            if c != "#":
                yield (x, y), (to_dir + 2) % 4, calc_is_forward(to_dir, c)


def find_next_node(maze, pos, from_dir):
    path_is_forward = calc_is_forward((from_dir + 2) % 4, maze[pos[1]][pos[0]])
    length = 0
    while True:
        if pos[1] == len(maze) - 1:
            return pos, from_dir, True, length
        length += 1

        next_pos = None
        next_dir = None
        this_is_forward = None
        for neighbour_pos, next_from_dir, next_is_forward in get_neighbours(
            maze, pos, from_dir
        ):
            if next_is_forward is not None:
                this_is_forward = next_is_forward
            if next_pos is not None:
                return pos, from_dir, path_is_forward, length
            else:
                next_pos, next_dir = neighbour_pos, next_from_dir
        if this_is_forward is not None:
            assert path_is_forward is None or this_is_forward == path_is_forward
            path_is_forward = this_is_forward

        if next_pos is None:
            return None
        pos, from_dir = next_pos, next_from_dir


def make_graph(maze):
    nodes = {}

    start_pos = (maze[0].index("."), 0)
    src = Node(start_pos)
    nodes[start_pos] = src
    node_positions = set()

    dst_pos = (maze[-1].index("."), len(maze) - 1)
    nodes[dst_pos] = Node(dst_pos)
    nodes[dst_pos].is_goal = True

    from_dir = 3
    to_explore = [(src, src.pos, from_dir)]

    while to_explore:
        node, pos, from_dir = to_explore.pop(0)
        next_node_pos, new_from_dir, is_forward, length = find_next_node(
            maze, pos, from_dir
        )
        if next_node_pos in nodes:
            assert is_forward is not None
            next_node = nodes[next_node_pos]
            assert not (next_node.is_goal and not is_forward)
            assert next_node is not node
        else:
            next_node = Node(next_node_pos)
            nodes[next_node_pos] = next_node
            for next_pos, neighbour_from_dir, _ in get_neighbours(
                maze, next_node_pos, new_from_dir
            ):
                to_explore.append((next_node, next_pos, neighbour_from_dir))

        if is_forward:
            assert not node.is_goal
            node.add_edge(next_node, length)
        else:
            next_node.add_edge(node, length)

    return src


maze = open("input.txt").read().splitlines()
graph = make_graph(maze)
print(graph.max_distance_to_goal())
