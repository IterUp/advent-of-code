from math import prod, sqrt, floor, ceil
times, distances = open("input.txt")
time = int(''.join(times.split()[1:]))
distance = int("".join(distances.split()[1:]))

def num_solutions(time, distance):
    v = sqrt(time**2 - 4*distance)
    lower = floor((time - v)/2.0 + 1)
    upper = ceil((time + v)/2.0 - 1)
    return upper - lower + 1


print(num_solutions(time, distance))
