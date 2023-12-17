register = 1
cycle = 0
total = 0
pixels = ""


def advance_cycle():
    global cycle
    global total
    cycle += 1
    if ((cycle + 20) % 40) == 0:
        total += cycle * register


for line in open("input.txt"):
    advance_cycle()
    if line.startswith("addx"):
        value = int(line.split()[-1])
        advance_cycle()
        register += value

print(total)
