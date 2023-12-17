def f(line):
    pair = line.strip().split(",")
    ranges = [[int(x) for x in range.split("-")] for range in pair]
    return not (ranges[0][1] < ranges[1][0] or ranges[1][1] < ranges[0][0])


print(sum(f(line) for line in open("input.txt")))
