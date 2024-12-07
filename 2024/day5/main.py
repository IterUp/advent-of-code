def is_ordered(rules, update):
    for rule in rules:
        try:
            i0 = update.index(rule[0])
            i1 = update.index(rule[1])
            if i1 < i0:
                return False
        except ValueError:
            pass

    return True


def check_update(rules, update):
    return int(update[(len(update) - 1) // 2]) if is_ordered(rules, update) else 0


def compare(x, y, rules):
    if [x, y] in rules:
        return -1
    if [y, x] in rules:
        return 1

    return 0


def find_middle(rules, update):
    left_count = 0
    right_count = 0
    while update:
        left = []
        right = []
        middle = []
        pivot = update.pop()
        for page in update:
            v = compare(pivot, page, rules)
            if v < 0:
                right.append(page)
            elif v > 0:
                left.append(page)
            else:
                middle.append(page)
        left_total = left_count + len(left)
        right_total = right_count + len(right)
        if middle:
            left_count += len(left)
            right_count += len(right)
            update = [pivot] + middle
        elif left_total == right_total:
            return int(pivot)
        elif left_total < right_total:
            update = right
            left_count = left_total + 1
        else:
            update = left
            right_count = right_total + 1
    assert False


def part2(rules, updates):
    result = 0
    for update in updates:
        if not check_update(rules, update):
            result += find_middle(rules, update)

    return result


f = open("input.txt")
lines = [line.strip() for line in f.readlines()]
gap = lines.index("")
rules = [line.split("|") for line in lines[:gap]]
updates = [line.split(",") for line in lines[gap + 1 :]]

print("Part 1 =", sum(check_update(rules, update) for update in updates))
print("Part 2 =", part2(rules, updates))
