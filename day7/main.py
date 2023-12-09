ranks = "23456789TJQKA"
class Hand:
    def __init__(self, line):
        x, y = line.split()
        self.hand = x
        self.bid = int(y)
        self.values = [ranks.index(c) for c in self.hand]
        self.frequencies = [self.values.count(value) for value in self.values]
        self.frequencies.sort(reverse=True)

hands = [Hand(line) for line in open("input.txt").readlines()]
hands.sort(key = lambda h: (h.frequencies, h.values))

for h in hands:
    print(h.hand, h.bid)

print(sum(i*h.bid for i, h in enumerate(hands, 1)))
