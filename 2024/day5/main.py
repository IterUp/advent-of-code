def check_update(rules, update):
    for rule in rules:
        try:
            i0 = update.index(rule[0])
            i1 = update.index(rule[1])
            if i1 < i0:
                return 0
        except ValueError:
            pass

    return int(update[(len(update) - 1) // 2])


f = open("input.txt")
lines = [line.strip() for line in f.readlines()]
gap = lines.index("")
rules = [line.split("|") for line in lines[:gap]]
updates = [line.split(",") for line in lines[gap + 1 :]]

print("Part 1 =", sum(check_update(rules, update) for update in updates))
print(
    "Part 2 =",
)
