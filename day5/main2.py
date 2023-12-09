from bisect import bisect_left, bisect_right

def find_min_location_for_maps(seed_interval, maps):
    if not maps:
        return seed_interval[0]
    orig_interval = seed_interval

    locations = []

    remaining_maps = maps[1:]
    for dst, src, count in maps[0].data:
        map_interval = (src, src + count)
        if (seed_interval[0] < map_interval[1]) and (seed_interval[0] < seed_interval[1]):
            if seed_interval[0] < map_interval[0]:
                locations.append(find_min_location_for_maps((seed_interval[0], map_interval[0]), remaining_maps))
                seed_interval = (map_interval[0], seed_interval[1])

            if seed_interval[0] < seed_interval[1]:
                offset = dst - src
                upper = min(seed_interval[1], map_interval[1])
                locations.append(find_min_location_for_maps((seed_interval[0]+offset, upper+offset), remaining_maps))
                seed_interval = (upper, seed_interval[1])

    if seed_interval[0] < seed_interval[1]:
        locations.append(seed_interval[0])
    return min(locations)

class Maps:
    def __init__(self):
        self.maps = []

    def add(self, new_map):
        new_map.sort()
        self.maps.append(new_map)

    def find_min_location(self, seed_range):
        return find_min_location_for_maps(seed_range.get_interval(), self.maps)

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

class SeedRange:
    def __init__(self, start, range):
        self.start = start
        self.range = range

    def get_interval(self):
        return (self.start, self.start+self.range)

lines = open("input.txt").readlines()
seed_line_parts = [int(value) for value in lines[0].split()[1:]]
seed_ranges = [SeedRange(*args) for args in zip(seed_line_parts[::2], seed_line_parts[1::2])]

maps = Maps()
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

print(min(*[maps.find_min_location(seed_range) for seed_range in seed_ranges]))
