def find_horizontal_mirror(m):
    for i in range(1, len(m)):
        left, right = m[i-1::-1], m[i:2*i]
        if all(a==b for a,b in zip(left, right)):
            return i
    return 0

def process_map(m):
    return 100*find_horizontal_mirror(m) + find_horizontal_mirror(list(zip(*m)))

def get_maps(f):
    m = []
    for line in f:
        line = line.strip()
        if not line:
            yield m
            m=[]
        else:
            m.append(line)
    yield m

print(sum(process_map(m) for m in get_maps(open("input.txt"))))
