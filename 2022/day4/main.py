def f(line):
    pair = line.strip().split(",")
    ranges = [[int(x) for x in range.split("-")] for range in pair]
    return (ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]) or (
        ranges[1][0] <= ranges[0][0] and ranges[1][1] >= ranges[0][1]
    )


print(sum(f(line) for line in open("input.txt")))
