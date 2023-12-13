def find_horizontal_mirror(m, original):
    for i in range(1, len(m)):
        left, right = m[i-1::-1], m[i:2*i]
        if all(a==b for a,b in zip(left, right)) and (i != original):
            return i
    return 0

def process_map(m, original):
    return 100*find_horizontal_mirror(m, original//100) + find_horizontal_mirror(list(zip(*m)), original)

def get_smudges(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = '.' if m[i][j] == '#' else '#'
            yield m
            m[i][j] = '.' if m[i][j] == '#' else '#'

def process_smudges(m):
    original = process_map(m, 0)
    print("original:", original)

    for smudge in get_smudges(m):
        v = process_map(smudge, original)
        if v:
            print(v)
            return v

def get_maps(f):
    m = []
    for line in f:
        line = list(line.strip())
        if not line:
            yield m
            m=[]
        else:
            m.append(line)
    yield m

if False:
    for i, m in enumerate(get_maps(open("test_input.txt"))):
        print(i, process_smudges(m))

print(sum(process_smudges(m) for m in get_maps(open("input.txt"))))
