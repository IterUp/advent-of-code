from math import prod, sqrt, floor, ceil
times, distances = open("input.txt")
times = [int(v) for v in times.split()[1:]]
distances = [int(v) for v in distances.split()[1:]]

def num_solutions(time, distance):
    v = sqrt(time**2 - 4*distance)
    lower = floor((time - v)/2.0 + 1)
    upper = ceil((time + v)/2.0 - 1)
    return upper - lower + 1


print(prod(num_solutions(*args) for args in zip(times, distances)))
