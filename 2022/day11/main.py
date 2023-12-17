class Monkey:
    def __init__(self, f):
        self.inspections = 0
        _, items_str = f.readline().split(":")
        self.items = [int(x) for x in items_str.split(",")]
        _, self.operation = f.readline().split("=")
        self.divisible_by = int(f.readline().split()[-1])
        self.true_monkey = int(f.readline().split()[-1])
        self.false_monkey = int(f.readline().split()[-1])

    def take_turn(self, monkeys):
        items = self.items
        self.inspections += len(items)
        self.items = []
        for old in items:
            new = eval(self.operation)
            new = new // 3
            dest = (
                self.true_monkey
                if (new % self.divisible_by) == 0
                else self.false_monkey
            )
            monkeys[dest].items.append(new)


def read_monkeys(f):
    while f.readline():
        yield Monkey(f)
        f.readline()


f = open("input.txt")
monkeys = list(read_monkeys(f))
for i in range(20):
    for monkey in monkeys:
        monkey.take_turn(monkeys)

inspections = [m.inspections for m in monkeys]
inspections.sort()
print(inspections[-1] * inspections[-2])
