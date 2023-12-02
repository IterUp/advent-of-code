f = open("input.txt")
lines = [[c for c in line if c.isdigit()] for line in f.readlines()]
print(sum(10*int(line[0])+int(line[-1]) for line in lines))
