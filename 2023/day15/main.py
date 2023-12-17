def f(input):
    v = 0
    for c in input:
        v = ((v + ord(c)) * 17) % 256
    return v


print(sum(f(v) for v in open("input.txt").readline().strip().split(",")))
