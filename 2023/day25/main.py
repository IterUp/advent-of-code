from collections import defaultdict, deque
from itertools import combinations

graph = defaultdict(list)
for line in open("input.txt").read().splitlines():
    src, dsts = line.split(": ")
    for dst in dsts.split():
        graph[src].append(dst)
        graph[dst].append(src)

nodes = graph.keys()


def search(graph, s, t, total_edges):
    edges = total_edges.copy()
    queue = deque()
    queue.append((s, ()))
    while queue:
        src, path = queue.popleft()
        if src == t:
            prev = None
            for curr in path:
                if prev:
                    total_edges.add((prev, curr))
                prev = curr
            return

        for dst in graph[src]:
            if (src, dst) not in edges:
                queue.append((dst, path + (dst,)))
                if (dst, src) in edges:
                    edges.remove((dst, src))
                else:
                    edges.add((src, dst))


def flood(graph, src, edges, is_reversed):
    print("flood")
    visited = set()
    queue = deque()
    queue.append(src)
    visited.add(src)
    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            if next not in visited:
                edge = (next, curr) if is_reversed else (curr, next)
                if edge not in edges:
                    queue.append(next)
                    visited.add(next)
    return len(visited)


def split(graph, s, t):
    edges = set()
    for i in range(3):
        print("search")
        search(graph, s, t, edges)
    n1 = flood(graph, s, edges, False)
    n2 = flood(graph, t, edges, True)
    if n1 + n2 == len(graph):
        print(n1, n2, n1 * n2)
        return True


def main():
    for s, t in combinations(nodes, 2):
        if split(graph, s, t):
            return


main()
