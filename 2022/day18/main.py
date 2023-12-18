def neighbours(block):
    for sign in (-1, 1):
        for i in range(3):
            yield tuple(b + sign*(j==i) for j, b in enumerate(block))

blocks = set(eval(line) for line in open("input.txt"))
print(sum(sum((neighbour not in blocks) for neighbour in neighbours(block)) for block in blocks))
