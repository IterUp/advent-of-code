def extrapolate(s):
    stack = [s]
    curr = s
    while any(v != 0 for v in curr):
        curr = [a-b for a,b in zip(curr[1:], curr[:-1])]
        stack.append(curr)
    curr = 0
    for v in stack[::-1]:
        curr = v[0] - curr

    return curr


sequences = [[int(value) for value in line.split()] for line in open("input.txt").readlines()]

print(sum(extrapolate(s) for s in sequences))
