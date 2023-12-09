f = open("input.txt")
path = f.readline().strip()
f.readline()
graph = {}

for line in f.readlines():
    head, tail = line.split('=')
    graph[head.strip()] = [s.strip() for s in tail.strip()[1:-1].split(',')]

curr = "AAA"
print(graph)
count = 0
while curr != "ZZZ":
    for c in path:
        count += 1
        curr = graph[curr][0 if c == 'L' else 1]

print(count)
