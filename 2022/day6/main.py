def f(line):
    size = 14
    for i in range(len(line)):
        if len(set(line[i : i + size])) == size:
            return i + size


for line in open("input.txt"):
    print(f(line))
