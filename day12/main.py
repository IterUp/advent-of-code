from itertools import combinations

def is_valid(s, sizes):
    split = [len(x) for x in s.split('.') if x]
    return split == sizes

def gen_string(pattern_parts, hit_locations):
    s = ''
    for i, part in enumerate(pattern_parts):
        s += part
        if i < len(pattern_parts) - 1:
            s += '#' if i in hit_locations else '.'
    return s

def f(line):
    pattern, hit_sizes = line.split()
    hit_sizes = [int(size) for size in hit_sizes.split(',')]
    total_hits = sum(hit_sizes)
    pattern_parts = pattern.split('?')
    missing = len(pattern_parts) - 1
    missing_hits = total_hits - pattern.count('#')
    return sum(is_valid(gen_string(pattern_parts, c), hit_sizes) for c in combinations(range(missing), missing_hits))

print(sum(f(line.strip()) for line in open("input.txt")))
