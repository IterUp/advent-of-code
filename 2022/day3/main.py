def f(line):
    line = line.strip()
    mid = len(line) // 2
    s1, s2 = set(line[:mid]), set(line[mid:])
    c = s1.intersection(s2).pop()
    return (1 + ord(c) - ord("a")) if c >= "a" else (27 + ord(c) - ord("A"))


print(sum(f(line) for line in open("input.txt")))
