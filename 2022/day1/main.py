def get_maps():
    m = []
    for line in open("input.txt"):
        line = line.strip()
        if line != "":
            m.append(line)
        else:
            yield m
            m = []
    yield m


print(max(sum(int(v) for v in m) for m in get_maps()))
