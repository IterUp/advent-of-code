lines = open("input.txt").readlines()
seeds = [int(value) for value in lines[0].split()[1:]]

maps = []
has_started = False
current_map = {}
for line in lines[2:]:
    line = line.strip()
    if not has_started:
        assert "map" in line, line
        has_started = line
    elif line:
        dst, src, count = line.split()
        count = int(count)
        src = int(src)
        dst = int(dst)
        # print("#", src, dst, count)
        for i in range(count):
            current_map[src+i] = dst+i
    else:
        # print(has_started)
        # print(current_map)
        has_started = False
        maps.append(current_map)
        current_map = {}
maps.append(current_map)

def find_location(seed, maps):
    for m in maps:
        seed = m.get(seed, seed)
    print(seed)
    return seed

print(min(*[find_location(s, maps) for s in seeds]))
