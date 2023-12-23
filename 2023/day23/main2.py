moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
directions = {0: "<", 1: "^", 2: ">", 3: "v"}
best = 0


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

        assert len(self.edges) <= 3
        self.edges.append((dst, length))

    def remove_edge(self, dst):
        new_edges = [edge for edge in self.edges if edge[0] is not dst]
        assert len(new_edges) + 1 == len(self.edges)
        self.edges = new_edges

    def __repr__(self):
        return f"N({self.pos})"

    def max_distance_to_goal(self, visited, cache, so_far=0):
        if self.is_goal:
            global best
            if so_far > best:
                best = so_far
                print("Best:", best)
            return 0
        else:
            value = 0
            visited.add(self.pos)
            for edge in self.edges:
                if edge[0].pos not in visited:
                    new_value = (
                        edge[0].max_distance_to_goal(visited, cache, so_far + edge[1])
                        + edge[1]
                    )
                    value = max(value, new_value)
            visited.remove(self.pos)
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

        node.add_edge(next_node, length)
        next_node.add_edge(node, length)

    return src, nodes


def dump_dot_file(nodes):
    num_edges = 0
    print("graph day23 {")
    for node in nodes.values():
        for edge in node.edges:
            if node.pos < edge[0].pos:
                num_edges += 1
                print(
                    f"  x{node.pos[0]}y{node.pos[1]} -- x{edge[0].pos[0]}y{edge[0].pos[1]} [label={edge[1]}]"
                )
    print("}")
    print(f"{len(nodes)=} {num_edges=}")


maze = open("input.txt").read().splitlines()
graph, nodes = make_graph(maze)
cache = {}
# dump_dot_file(nodes)

paths_to_remove = (
    (
        (131, 123),
        (137, 107),
        (123, 75),
        (131, 67),
        (137, 33),
        (101, 11),
        (75, 17),
        (57, 15),
        (29, 11),
        (13, 7),
    ),
    (
        (131, 123),
        (103, 129),
        (85, 125),
        (55, 127),
        (31, 127),
        (13, 99),
        (9, 79),
        (11, 53),
        (11, 41),
        (13, 7),
    ),
)

for path in paths_to_remove:
    prev = None
    for node_pos in path:
        node = nodes[node_pos]
        if prev is not None:
            prev.remove_edge(node)
        prev = node
print(graph.max_distance_to_goal(set(), cache, 0))
