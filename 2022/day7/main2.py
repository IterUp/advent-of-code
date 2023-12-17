from collections import defaultdict
import copy

cwd = ()
sizes = defaultdict(int)

for line in open("input.txt"):
    line = line.strip()
    if line.startswith("$ cd "):
        next_dir = line[5:].strip()
        if next_dir == "/":
            cwd = ()
        elif next_dir == "..":
            cwd = cwd[:-1]
        else:
            cwd += (next_dir,)
    elif not line.startswith("$") and not line.startswith("dir "):
        size, _ = line.split()
        sizes[cwd] += int(size)

total_sizes = copy.copy(sizes)
for k in sizes:
    for i in range(len(k)):
        total_sizes[k[:i]] += sizes[k]

needed = 30000000 - (70000000 - total_sizes.get((), 0))
print(min(size for size in total_sizes.values() if size >= needed))
