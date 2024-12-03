def is_safe(report):
    diffs = [x - y for x, y in zip(report[:-1], report[1:])]
    x = min(diffs)
    y = max(diffs)
    return ((-3 <= x) and (y <= -1)) if x < 0 else ((1 <= x) and (y <= 3))

def is_safer(report):
    return any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))

f = open("input.txt")
reports = [[int(x) for x in line.split()] for line in f.readlines()]
print(sum(is_safe(report) for report in reports))
print(sum(is_safer(report) for report in reports))
