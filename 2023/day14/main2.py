m = tuple(tuple(line.strip()) for line in open("input.txt"))

def measure_line(line):
    return sum(len(line) - i for i, c in enumerate(line) if c == 'O')

def measure(m):
    return sum(measure_line(line) for line in m)

def slide_line(line):
    line = list(line)
    pos = 0
    for i, c in enumerate(line):
        if c == 'O':
            line[i] = '.'
            line[pos] = 'O'
            pos += 1
        elif c == '#':
            pos = i + 1
    return tuple(line)

def slide(m):
    return [slide_line(line) for line in m]

def rotate(m):
    return tuple(zip(*m[::-1]))

def print_map(m):
    print(m)
    return
    for line in m:
        print(''.join(line))

for i in range(3):
    m = rotate(m)

visited = set()
cycle_start = None
cycle_start_index = None
cycle = []

index = 0
while m != cycle_start:
    if cycle_start is None:
        if m in visited:
            cycle_start = m
            cycle_start_index = index
        else:
            visited.add(m)

    if cycle_start:
        cycle.append(measure(m))
    index += 1
    for i in range(4):
        m = slide(m)
        m = rotate(m)

print(cycle_start_index, index, cycle)
print(cycle[(1000000000-cycle_start_index)%len(cycle)])
