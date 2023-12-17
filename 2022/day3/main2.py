def f(group):
    x, y, z = [set(a.strip()) for a in group]
    c = x.intersection(y).intersection(z).pop()
    return (1 + ord(c) - ord("a")) if c >= "a" else (27 + ord(c) - ord("A"))


lines = list(open("input.txt").readlines())
groups = zip(lines[0::3], lines[1::3], lines[2::3])

print(sum(f(group) for group in groups))
