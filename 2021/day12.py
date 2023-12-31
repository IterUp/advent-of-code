is_test = False


class Node:
    def __init__(self, label):
        self.label = label
        self.neighbours = []

    def add(self, neighbour):
        if neighbour.label != "start":
            self.neighbours.append(neighbour)

    def __repr__(self):
        return self.label


def find_paths(node, nodes, visited, path, num_spares=0):
    if node.label == "end":
        return 1

    num_paths = 0
    for neighbour in node.neighbours:
        has_visited = neighbour in visited
        if not has_visited or (num_spares > 0):
            new_num_spares = num_spares - 1 if has_visited else num_spares

            should_remove = False

            if neighbour.label.islower() and not has_visited:
                should_remove = True
                visited.add(neighbour)

            num_paths += find_paths(
                neighbour, nodes, visited, path + (neighbour.label,), new_num_spares
            )

            if should_remove:
                visited.remove(neighbour)
    return num_paths


def part1(nodes):
    visited = set()
    start = nodes["start"]
    visited.add(start)
    return find_paths(nodes["start"], nodes, visited, ())


def part2(nodes):
    visited = set()
    start = nodes["start"]
    visited.add(start)
    return find_paths(nodes["start"], nodes, visited, (), 1)


def main(input):
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


def read_input(filename):
    nodes = {}
    for line in open(filename).read().splitlines():
        src_label, dst_label = line.split("-")
        src = nodes.get(src_label, Node(src_label))
        dst = nodes.get(dst_label, Node(dst_label))
        src.add(dst)
        dst.add(src)
        nodes[src_label] = src
        nodes[dst_label] = dst

    return nodes


main(read_input("test_input/day12.txt" if is_test else "input/day12.txt"))
