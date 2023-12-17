m = list(zip(*[line.strip() for line in open("input.txt")]))

def process(line):
    total = 0
    v = len(line)
    for i, c in enumerate(line):
        if c == 'O':
            total += v
            v -= 1
        elif c == '#':
            v = len(line) - i - 1
    return total


print(sum(process(line) for line in m))
