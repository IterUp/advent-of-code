from math import lcm
f = open("input.txt")
path = f.readline().strip()
f.readline()
graph = {}

for line in f.readlines():
    head, tail = line.split('=')
    graph[head.strip()] = [s.strip() for s in tail.strip()[1:-1].split(',')]

starts = [k for k in graph if k.endswith('A')]

def dist(curr):
    count = 0
    while not curr.endswith('Z'):
        for c in path:
            curr = graph[curr][0 if c == 'L' else 1]
            count += 1
    return count

lengths = [dist(k) for k in starts]
print(lengths)
print(lcm(*lengths))
