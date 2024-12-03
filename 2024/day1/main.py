f = open("input.txt")
lines = [line.split() for line in f.readlines()]
lines = list(zip(*lines))
list_a = sorted(lines[0])
list_b = sorted(lines[1])
print(sum(abs(int(a) - int(b)) for a, b in zip(list_a, list_b)))
print(sum(int(a) * list_b.count(a) for a, b in zip(list_a, list_b)))
