ranks = "J23456789TQKA"
class Hand:
    def __init__(self, line):
        x, y = line.split()
        self.hand = x
        self.bid = int(y)
        self.values = [ranks.index(c) for c in self.hand]
        self.frequencies = [self.values.count(value) for value in self.values if value != 0]
        self.frequencies.sort(reverse=True)
        num_wilds = self.values.count(0)
        most_frequent = self.frequencies[0] if self.frequencies else 0
        new_max = most_frequent + num_wilds
        self.frequencies = new_max * [new_max] + self.frequencies[most_frequent:]

hands = [Hand(line) for line in open("input.txt").readlines()]
hands.sort(key = lambda h: (h.frequencies, h.values))

for h in hands:
    print(h.hand, h.bid, h.frequencies, h.values)

print(sum(i*h.bid for i, h in enumerate(hands, 1)))
