from bisect import bisect_right
class Maps:
    def __init__(self):
        self.maps = []

    def add(self, new_map):
        new_map.sort()
        self.maps.append(new_map)

    def find_location(self, seed):
        for m in self.maps:
            seed = m.get(seed, seed)
        return seed

class Map:
    def __init__(self):
        self.data = []

    def add(self, dst, src, count):
        self.data.append((dst, src, count))

    def sort(self):
        self.data.sort(key = lambda x: x[1])

    def get(self, key, default):
        upper_index = bisect_right(self.data, key, key=lambda x: x[1])
        dst, src, count = self.data[upper_index-1]
        return dst + key - src if key < src+count else default

maps = Maps()
lines = open("input.txt").readlines()
seeds = [int(value) for value in lines[0].split()[1:]]

has_started = False
current_map = Map()
for line in lines[2:]:
    line = line.strip()
    if not has_started:
        assert "map" in line, line
        has_started = line
    elif line:
        dst, src, count = line.split()
        current_map.add(int(dst), int(src), int(count))
    else:
        has_started = False
        maps.add(current_map)
        current_map = Map()
maps.add(current_map)
del current_map

print(min(*[maps.find_location(s) for s in seeds]))
