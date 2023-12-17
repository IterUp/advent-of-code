def read_stacks(f):
    lines = []
    while True:
        line = f.readline()
        if line.startswith(" 1 "):
            stacks = zip(*[line[1::4] for line in lines])
            return ["".join(stack[::-1]).strip() for stack in stacks]
        lines.append(line)


def move(stacks, count, from_id, to_id):
    if from_id != to_id:
        stacks[to_id - 1] += stacks[from_id - 1][-count:]
        stacks[from_id - 1] = stacks[from_id - 1][:-count]


f = open("input.txt")
stacks = read_stacks(f)
f.readline()
for line in f:
    _, count, _, from_id, _, to_id = line.split()
    move(stacks, int(count), int(from_id), int(to_id))
print("".join(stack[-1] for stack in stacks))
