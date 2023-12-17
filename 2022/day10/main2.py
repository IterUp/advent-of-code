register = 1
cycle = 0
pixels = ""


def advance_cycle():
    global cycle
    global pixels
    pixels += "#" if abs((cycle % 40) - register) <= 1 else "."
    cycle += 1


for line in open("input.txt"):
    advance_cycle()
    if line.startswith("addx"):
        value = int(line.split()[-1])
        advance_cycle()
        register += value

for i in range(len(pixels) // 40):
    print(pixels[i * 40 : (i + 1) * 40])
