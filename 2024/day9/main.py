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

    return cal_total(result)


def cal_total(result):
    total = 0
    pos = 0
    for r in result:
        for i in range(r[1]):
            if r[0] != -1:
                total += r[0] * (pos + i)
        pos += r[1]
    return total


def find_gap(blocks, size):
    for i, block in enumerate(blocks):
        if (block[0] == -1) and (block[1] >= size):
            return i
    return None


def part2():
    blocks = [[i // 2 if i % 2 == 0 else -1, int(c)] for i, c in enumerate(line)]
    pos = len(blocks) - 1
    while pos > 0:
        curr = blocks[pos]
        if curr[0] != -1:
            gap = find_gap(blocks, curr[1])
            if (gap is not None) and (gap < pos):
                blocks = (
                    blocks[:gap]
                    + [blocks[pos]]
                    + blocks[gap:pos]
                    + [[-1, blocks[pos][1]]]
                    + blocks[pos + 1 :]
                )
                blocks[gap + 1][1] -= curr[1]
            else:
                pos = pos - 1
        else:
            pos = pos - 1
    return cal_total(blocks)


print("Part 1 =", part1())
print("Part 2 =", part2())
