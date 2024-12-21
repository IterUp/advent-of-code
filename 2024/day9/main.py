f = open("input.txt")
line = f.readline().strip()


def part1():
    blocks = [(i, int(c)) for i, c in enumerate(line[0::2])]
    gaps = [int(c) for c in line[1::2]]
    result = [blocks[0]]
    blocks = blocks[1:]
    while gaps and blocks:
        curr_gap = gaps[0]
        back = blocks[-1]
        if back[1] >= curr_gap:
            result.append((back[0], curr_gap))
            if back[1] == curr_gap:
                blocks = blocks[:-1]
            else:
                blocks = blocks[:-1] + [(back[0], back[1] - curr_gap)]
            gaps = gaps[1:]
            result.append(blocks[0])
            blocks = blocks[1:]
        else:
            result.append(back)
            gaps[0] = curr_gap - back[1]
            blocks = blocks[:-1]
    print(result)
    total = 0
    pos = 0
    for r in result:
        for i in range(r[1]):
            total += r[0] * (pos + i)
        pos += r[1]
    return total


def part2():
    return 0


print("Part 1 =", part1())
print("Part 2 =", part2())
